from cmath import nan
from flask import Flask, request, render_template
import numpy as np
import pickle


# Create the Flask application instance with the custom template folder
app = Flask(__name__)

filename = 'foodandRestaurantLinearRegression.pkl'
dict1 = nan  # Default value for dict1


try:
    with open(filename, 'rb') as f:
        dict1 = pickle.load(f)
except EOFError:
    print(
        f"Error: Unable to load data from {filename}. The file might be empty or corrupted.")
    # Handle the error appropriately, e.g., by exiting the script or providing a default value for `dict1`.


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    feature2_value, feature2_label = request.form['feature2'].split('|')
    feature3_value, feature3_label = request.form['feature3'].split('|')
    feature4_value, feature4_label = request.form['feature4'].split('|')
    # Extract input features from the request
    feature1 = int(request.form['feature1'])
    feature2 = int(feature2_value)
    feature3 = int(feature3_value)
    feature4 = int(feature4_value)

    # Preprocess the input features
    # Make predictions using the loaded model
    if dict1:
        x = np.array(dict1.predict([[feature1, feature2, feature3, feature4]]))
        value = round(x.item(), 1)
        selectedValues = [feature1, feature2_label, feature3_label, feature4_label]
        prediction = [value, selectedValues]
    else:
        # Handle the scenario where dict1 is not loaded
        return "Error: Model not loaded."

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
