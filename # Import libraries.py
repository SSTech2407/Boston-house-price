<<<<<<< HEAD
# Import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load from CSV
df = pd.read_csv("BostonHousing.csv")

# Separate features and target
X = df.drop('price', axis=1)   # Features
y = df['price']                # Target

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the model
pickle.dump(model, open('model.pkl', 'wb'))

print("Model trained and saved successfully.")

=======
# Import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load from CSV
df = pd.read_csv("BostonHousing.csv")

# Separate features and target
X = df.drop('price', axis=1)   # Features
y = df['price']                # Target

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the model
pickle.dump(model, open('model.pkl', 'wb'))

print("Model trained and saved successfully.")

>>>>>>> d54ee14d440e3f1d820118828453e620fc6d549a
