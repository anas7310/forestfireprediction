🌳 Wildfire Danger Prediction Application

This is a web application designed to predict the Fire Weather Index (FWI) using a trained machine learning model (Ridge Regression) integrated via a Flask API. The front end is a single, responsive HTML page that collects meteorological and environmental data from the user.

✨ Features

Responsive UI: Single-file HTML interface (home.html) styled with Tailwind CSS, ensuring optimal display on mobile, tablet, and desktop devices.

API Integration: Uses asynchronous fetching mechanisms to send user data as JSON to the Flask backend.

Machine Learning Backend: Utilizes a pre-trained Ridge Regression model and a StandardScaler for predicting the FWI value.

Real-time Risk Display: Classifies the predicted FWI value into Low, Moderate, or High-Risk categories for clear user feedback.

🚀 Setup and Usage

Prerequisites

You need Python and Flask installed, along with the necessary machine learning libraries (scikit-learn, joblib, etc.).

Backend Files: Ensure you have the following files in your Flask application directory:

app.py (or similar, containing the Flask application instance)

index.html (the web form)

scaler.pkl (The fitted data preprocessor)

model.pkl (The trained prediction model)

Model Loading: The application loads the fitted data preprocessor (scaler.pkl) and the trained prediction model (model.pkl) when the application starts. Error handling is in place to print a message if these essential files are not found.

Run the Application:

Run the application using the standard Flask command.

Access the application in your browser (usually http://127.0.0.1:5000/).

📥 Data Input Fields

The application requires 9 input features, which are sent to the model for FWI prediction. Ensure the user inputs respect the data types (float/int) for accurate scaling and prediction.

Index

Field Name

Data Type

Description

0

Temperature

float

Temperature in degrees Celsius.

1

RH

float

Relative Humidity (%).

2

Ws

float

Wind Speed (km/h).

3

Rain

float

Amount of Rain (mm).

4

FFMC

float

Fine Fuel Moisture Code.

5

DMC

float

Duff Moisture Code.

6

ISI

float

Initial Spread Index.

7

Classes

float

Fire occurrence indicator (e.g., 0 or 1).

8

Region

float

Geographic Region indicator (e.g., 1 or 2).

⚙️ Prediction Endpoint (/predictdata)

The Flask function handling predictions executes the following steps:

Retrieves data from the request body.

Converts all input values to floating-point numbers.

Scales the data using the loaded preprocessor.

Predicts the FWI value using the trained model.

Returns the result as a standard JSON object containing the predicted FWI value.

Any error during the process will result in a client-side 400 Bad Request status with an error message to help debug the data flow.
