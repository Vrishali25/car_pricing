from flask import Flask, render_template, request
from utils import predict_price  # Make sure you have this function in your 'utils' module

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.form

        product_id = float(data['product_id'])
        sale = float(data['sale'])
        weight = float(data['weight'])
        resolution = float(data['resolution'])
        ppi = float(data['ppi'])
        cpu_core = float(data['cpu_core'])
        cpu_freq = float(data['cpu_freq'])
        ram = float(data['ram'])
        rear_cam = float(data['rear_cam'])
        internal_mem = float(data['internal_mem'])
        front_cam = float(data['front_cam'])
        battery = float(data['battery'])
        thickness = float(data['thickness'])

        # Assuming predict_price is a function that takes these parameters and returns the prediction
        prediction = predict_price(product_id, sale, weight, resolution, ppi, cpu_core, cpu_freq, internal_mem, ram,
                                   rear_cam, front_cam, battery, thickness)

        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
