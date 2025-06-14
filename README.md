# 🏠Boston House Price Predictor
  A simple machine learning web application built using **Flask** that predicts house prices in Boston based on input features. The model is trained using the Boston Housing Dataset.
---
#📌Features
- Linear Regression model trained on 14 input features
- Flask web app for user interaction
- Clean HTML + CSS interface
- Predicts house prices based on input data
- Ready for deployment on platforms like Render

---

# Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas, NumPy
- HTML5 + CSS3

---

## Project Structure

project/
├── app.py                  # Flask backend
├── model.pkl               # Trained ML model
├── BostonHousing.csv       # Dataset (optional)
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html          # Input form page
│   └── result.html         # Output result page
└── README.md               # Project details


---

## Input Features (User Enters 14 Values)

Each input corresponds to a real estate feature:

1. CRIM – crime rate
2. ZN – residential land zoned
3. INDUS – non-retail business acres
4. CHAS – bounds Charles River (0/1)
5. NOX – nitrogen oxide levels
6. RM – average rooms per dwelling
7. AGE – % built before 1940
8. DIS – distance to employment centers
9. RAD – accessibility to highways
10. TAX – property tax
11. PTRATIO – pupil-teacher ratio
12. B – diversity index
13. LSTAT – % lower income

---

## How to Run the Project Locally

1. Clone this repository.
    git clone (https://github.com/SSTech2407/Boston-house-price)
    cd boston-house-price 

2. Install dependencies.
  pip install -r requirements.txt

3. Run the app.
   python app.py

4. Open in browser.
   Go to: http://127.0.0.1:5000

---

Example Output,
Predicted House Price: $25,346.45

---

🧠 Model Info
- Algorithm: Linear Regression
- Library: scikit-learn
- Model trained using 13 features
- Saved using pickle as model.pkl

---

✨ Final Version
This is the final cleaned and updated version of the project, completed on 14 June 2025, with all features working and design polished.

---
🧑‍💻Author
Developed by Sparsh Sharma
GitHub: SSTech2407

 📸 Screenshot
 First page. 
 ![image](https://github.com/user-attachments/assets/b4f51c62-9307-4b4a-aed9-99b7bc88f219)
 Entering the Values.
 ![image](https://github.com/user-attachments/assets/733f4f8a-bfba-4265-b307-2ee8b64822ed)
 Result i.e the predicted price 
![image](https://github.com/user-attachments/assets/fae82ff8-512b-4a25-9df6-1523d3e43ddc)

