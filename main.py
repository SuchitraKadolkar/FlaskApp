from flask import Flask, jsonify, render_template

app = Flask(__name__)

data = {
    "order_id": 1234,
    "customer": "Suchitra Kadolkar",
    "items": ["Soap", "Detergent", "Handwash"],
    "total": 350.75
}

processed_data = {}

def process_data(data):
    # Simulate data processing (e.g., uppercase conversion)
    #return [item["value"] * 2 for item in data]
    processed_data = {}
    for key, value in data.items():
        if isinstance(value, str):
            processed_data[key] = value.upper()
        elif isinstance(value, list):
            processed_data[key] = [item.upper() for item in value if isinstance(item, str)]
    return processed_data    

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    return jsonify(data)

@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    global processed_data
    if not processed_data:
        processed_data = process_data(data)
    return jsonify(processed_data)

if __name__ == '__main__':
    app.run(debug=True)
