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

    # Simple simulated values for predicted and actual sales
    predicted_sales = round(previous_sales * (1.1 + marketing_budget * 0.001), 2)
    actual_sales = round(predicted_sales * (0.95 + 0.1), 2)  # add variation

    # Add them into the data dictionary so Jinja can render them
    data['predicted_sales'] = predicted_sales
    data['actual_sales'] = actual_sales

    # Generate AI-style feedback (your existing logic)
    feedback_options = []
    if marketing_budget < previous_sales * 0.1:
        feedback_options.append("Increase your marketing budget to boost visibility and sales.")
    else:
        feedback_options.append("Your marketing budget looks strong — focus on optimizing campaign targeting.")

    if float(data.get('price', 0)) > previous_sales * 0.05:
        feedback_options.append("Your product price may be high relative to past sales. Explore discounts or bundles.")
    else:
        feedback_options.append("Your pricing strategy seems competitive. Highlight value to maintain momentum.")

    if data.get('season') == "summer":
        feedback_options.append("Summer sales often peak — consider seasonal promotions to maximize revenue.")
    elif data.get('season') == "winter":
        feedback_options.append("Winter sales can dip — plan holiday campaigns to sustain demand.")
    else:
        feedback_options.append("Seasonal impact is moderate. Focus on consistent customer engagement.")

    feedback = " ".join(random.sample(feedback_options, min(3, len(feedback_options))))

    return render_template('improvement.html', data=data, feedback=feedback)

@app.route('/update-sales-data', methods=['POST'])
def update_sales_data():
    updated = request.get_json()
    file_path = os.path.join(os.path.dirname(__file__), 'sales_data.json')
    with open(file_path, 'w') as f:
        json.dump(updated, f, indent=2)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)