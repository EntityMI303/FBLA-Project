// ======== Perlin Noise Generator ========
const noise = (() => {
  const perm = new Uint8Array(512);
  const grad = [[1,1], [-1,1], [1,-1], [-1,-1], [1,0], [-1,0], [0,1], [0,-1]];
  let seed = 1337;
  const rand = () => ((seed = seed * 16807 % 2147483647) / 2147483647);
  for (let i = 0; i < 256; i++) perm[i] = i;
  for (let i = 0; i < 256; i++) {
    const j = Math.floor(rand() * 256);
    [perm[i], perm[j]] = [perm[j], perm[i]];
    perm[i + 256] = perm[i];
  }
  const fade = t => t*t*t*(t*(t*6-15)+10);
  const lerp = (a,b,t) => a + t * (b - a);
  const grad2 = (h,x,y) => {
    const g = grad[h & 7];
    return g[0]*x + g[1]*y;
  };
  const perlin2 = (x,y) => {
    const xi = Math.floor(x) & 255, yi = Math.floor(y) & 255;
    const xf = x - Math.floor(x), yf = y - Math.floor(y);
    const u = fade(xf), v = fade(yf);
    const aa = perm[perm[xi] + yi];
    const ab = perm[perm[xi] + yi + 1];
    const ba = perm[perm[xi + 1] + yi];
    const bb = perm[perm[xi + 1] + yi + 1];
    const x1 = lerp(grad2(aa, xf, yf), grad2(ba, xf - 1, yf), u);
    const x2 = lerp(grad2(ab, xf, yf - 1), grad2(bb, xf - 1, yf - 1), u);
    return (lerp(x1, x2, v) + 1) / 2;
  };
  return { perlin2 };
})();

// ======== Terrain and Chunk System ========
const chunkSize = 16;
const blockSize = 0.25;
const elevationScale = 0.07;
const loadedChunks = new Set();
const playerStart = { ready: false, x: 0, y: 0, z: 0 };

function generateChunk(cx, cz) {
  const scene = document.getElementById("scene");
  const key = `${cx},${cz}`;
  const container = document.createElement("a-entity");
  container.setAttribute("id", `chunk-${key}`);

  for (let x = 0; x < chunkSize; x++) {
    for (let z = 0; z < chunkSize; z++) {
      const worldX = cx * chunkSize + x;
      const worldZ = cz * chunkSize + z;
      const height = Math.floor(noise.perlin2(worldX * elevationScale, worldZ * elevationScale) * 12);
      const riverNoise = noise.perlin2(worldX * 0.52 + 99, worldZ * 0.52 + 99);
      const isRiver = riverNoise < 0.45;
      const topY = isRiver ? 1 : height;

      for (let y = 0; y <= topY; y++) {
        const cave = noise.perlin2(worldX * 0.50, y * 0.50 + 999 + worldZ) < 0.5;
        if (y < height - 7 && cave) continue;

        const yPos = y * blockSize + blockSize / 2;
        const box = document.createElement("a-box");
        box.setAttribute("width", blockSize);
        box.setAttribute("height", blockSize);
        box.setAttribute("depth", blockSize);
        box.setAttribute("position", `${worldX * blockSize} ${yPos} ${worldZ * blockSize}`);

        let color = "#777";
        if (isRiver) color = y === topY ? "#3A9BD9" : "#2B5FA6";
        else if (y === topY) color = "#228B22";
        else if (y >= topY - 2) color = "#A0522D";
        else color = "#444";

        box.setAttribute("color", color);
        container.appendChild(box);

        if (!playerStart.ready && !isRiver && y === topY && cx === 0 && cz === 0) {
          playerStart.ready = true;
          playerStart.x = worldX * blockSize;
          playerStart.y = yPos + blockSize;
          playerStart.z = worldZ * blockSize;
        }
      }
    }
  }

  scene.appendChild(container);
}

// ======== Dynamic Chunk Loading ========
AFRAME.registerComponent("dynamic-chunk-loader", {
  schema: { range: { default: 0.5 } },
  tick() {
    const pos = this.el.object3D.position;
    const cx = Math.floor(pos.x / (chunkSize * blockSize));
    const cz = Math.floor(pos.z / (chunkSize * blockSize));
    const needed = new Set();

    for (let dx = -this.data.range; dx <= this.data.range; dx++) {
      for (let dz = -this.data.range; dz <= this.data.range; dz++) {
        const key = `${cx + dx},${cz + dz}`;
        needed.add(key);
        if (!loadedChunks.has(key)) {
          generateChunk(cx + dx, cz + dz);
          loadedChunks.add(key);
        }
      }
    }

    // Remove chunks no longer needed
    loadedChunks.forEach(key => {
      if (!needed.has(key)) {
        const chunkEl = document.getElementById(`chunk-${key}`);
        if (chunkEl) chunkEl.remove();
        loadedChunks.delete(key);
      }
    });
  }
});

// ======== Player Tracker ========
AFRAME.registerComponent("track-position", {
  init() {
    this.el.sceneEl.addEventListener("loaded", () => {
      if (playerStart.ready) {
        this.el.object3D.position.set(playerStart.x, playerStart.y, playerStart.z);
      }
    });
  },
  tick() {
    const pos = this.el.object3D.position;
    document.getElementById("coordinates").innerText =
      `X: ${pos.x.toFixed(1)} Y: ${pos.y.toFixed(1)} Z: ${pos.z.toFixed(1)}`;
  }
});

// ======== Mode Switching (Survival, Creative, Spectator) ========
AFRAME.registerComponent("mode-switcher", {
  init() {
    this.modes = ["survival", "creative", "spectator"];
    this.current = 0;
    this.player = this.el;
    this.text = document.getElementById("mode");
    this.setMode();
    window.addEventListener("keydown", e => {
      if (e.code === "KeyM") {
        this.current = (this.current + 1) % this.modes.length;
        this.setMode();
      }
    });
  },
  setMode() {
    const mode = this.modes[this.current];
    this.player.removeAttribute("jump-controls");
    this.player.removeAttribute("movement-controls");

    if (mode === "survival") {
      this.player.setAttribute("jump-controls", "");
      this.player.setAttribute("movement-controls", { fly: false });
    } else {
      this.player.setAttribute("movement-controls", { fly: true });
    }

    this.text.textContent = `Mode: ${mode.charAt(0).toUpperCase() + mode.slice(1)}`;
  }
});

// ======== Gravity & Jump (Survival Mode) ========
AFRAME.registerComponent("jump-controls", {
  schema: { gravity: { default: -9.8 }, jumpStrength: { default: 4.5 } },
  init() {
    this.velocityY = 0;
    this.grounded = true;
    window.addEventListener("keydown", e => {
      if (e.code === "Space" && this.grounded) {
        this.velocityY = this.data.jumpStrength;
        this.grounded = false;
      }
    });
  },
  tick(_, dt) {
    const delta = dt / 1000;
    this.velocityY += this.data.gravity * delta;
    const pos = this.el.getAttribute("position");
    pos.y += this.velocityY * delta;
    if (pos.y <= 2) {
      pos.y = 2;
      this.velocityY = 0;
      this.grounded = true;
    }
    this.el.setAttribute("position", pos);
  }
});

AFRAME.registerComponent("shift-controls", {
  schema: { speed: { default: 0.4 } }, // lower = slower descent
  init() {
    this.isShifting = false;

    window.addEventListener("keydown", e => {
      if (e.code === "ShiftLeft" || e.code === "ShiftRight") {
        this.isShifting = true;
      }
    });

    window.addEventListener("keyup", e => {
      if (e.code === "ShiftLeft" || e.code === "ShiftRight") {
        this.isShifting = false;
      }
    });
  },
  tick(_, dt) {
    if (!this.isShifting) return;

    const delta = dt / 1000;
    const pos = this.el.getAttribute("position");
    pos.y -= this.data.speed * delta;

    this.el.setAttribute("position", pos);
  }
});