from flask import Flask, render_template, request, redirect, url_for, session, send_file
import json, os, requests
import random

app = Flask(__name__)
app.secret_key = 'business25'

@app.route('/')
def home():
    return render_template('index.html', name="Sprite Blue Jet")

@app.route('/predict-future-sales', methods=['GET', 'POST'])
def sales():
    if request.method == 'POST':
        data = {
            'previous_sales': request.form.get('previous_sales'),
            'product': request.form.get('product'),
            'price': request.form.get('price'),
            'marketing_budget': request.form.get('marketing_budget'),
            'season': request.form.get('season'),
            'year': request.form.get('year'),
            'month': request.form.get('month'),
            'weeks': request.form.get('weeks'),
            'days': request.form.get('days')
        }
        session['sales_data'] = data
        file_path = os.path.join(os.path.dirname(__file__), 'sales_data.json')
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        return '', 204

    return render_template('sales.html')

@app.route('/download-sales-data')
def download_sales():
    file_path = os.path.join(os.path.dirname(__file__), 'sales_data.json')
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return "sales_data.json not found", 404

import random

@app.route('/business-improvement-guide')
def improvement():
    data = session.get('sales_data')
    if not data:
        return redirect(url_for('sales'))

    previous_sales = float(data.get('previous_sales', 0))
    marketing_budget = float(data.get('marketing_budget', 0))

    predicted_sales = round(previous_sales * (1.1 + marketing_budget * 0.001), 2)
    actual_sales = round(predicted_sales * (0.95 + 0.1), 2)

    data['predicted_sales'] = predicted_sales
    data['actual_sales'] = actual_sales

    # Call AI API for feedback
    headers = {"Authorization": f"Bearer YOUR_API_KEY"}
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a business consultant giving constructive improvement advice."},
            {"role": "user", "content": f"Sales data: {data}. Provide improvement suggestions."}
        ]
    }
    r = requests.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)
    ai_feedback = r.json()["choices"][0]["message"]["content"]

    return render_template('improvement.html', data=data, feedback=ai_feedback)

@app.route('/update-sales-data', methods=['POST'])
def update_sales_data():
    updated = request.get_json()
    file_path = os.path.join(os.path.dirname(__file__), 'sales_data.json')
    with open(file_path, 'w') as f:
        json.dump(updated, f, indent=2)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
