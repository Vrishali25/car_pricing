
import pickle
import numpy as np
import config
def predict_price(product_id, sale, weight, resolution, ppi, cpu_core, cpu_freq, internal_mem, ram, rear_cam, front_cam, battery, thickness):
    # Load the linear regression model
    model_file = config.model_file_path
    with open(model_file, 'rb') as f:
        model = pickle.load(f)

    # Prepare input features for prediction
    features = np.array([[product_id,sale, weight, resolution, ppi, cpu_core, cpu_freq, internal_mem, ram,
                          rear_cam, front_cam, battery, thickness]])

    # Make prediction
    price_prediction = model.predict(features)

    return price_prediction[0]
