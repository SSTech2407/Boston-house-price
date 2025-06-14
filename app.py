<<<<<<< HEAD
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = [float(x) for x in request.form.values()]
        if len(input_data) != 13:
            return "❌ Error: Please enter exactly 13 values."

        final_input = [np.array(input_data)]
        prediction = model.predict(final_input)
        price = f"${prediction[0]:,.2f}"

        return render_template('result.html', prediction_text=price)

    except Exception as e:
        return f"⚠️ An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [float(x) for x in request.form.values()]
    final_input = [np.array(input_data)]
    prediction = model.predict(final_input)[0]
    return render_template('index.html', prediction_text=f'Predicted Price: ${prediction:.2f}')

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> d54ee14d440e3f1d820118828453e620fc6d549a
