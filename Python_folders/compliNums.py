x = int(input("Enter a number:"))

bin_output = bin(x)[2:]
oct_output = oct(x)[2:]
hex_output = hex(x)[2:]

output = f"""
Binary: {bin_output}
Octal: {oct_output}
Hexadecimal: {hex_output}
"""

print(output.strip())