from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

app = Flask(__name__, static_url_path='/static')

# Load the pre-trained model
file_path = 'random_forest_regression_model.pkl'
loaded_model = joblib.load(file_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        years_of_experience = float(request.form['years_of_experience'])
        dp_score = float(request.form['dp_score'])
        speciality = request.form['speciality']
        npv = float(request.form['npv'])
        city = request.form['city']

        # Original data
        data = {
            'Years of Experience': [years_of_experience],
            'DP Score': [dp_score],
            'Speciality': [speciality],
            'NPV': [npv],
            'City': [city] 
        }

        # Extract numerical and categorical data
        numerical_data = {key: value for key, value in data.items() if key != 'Speciality' and key != 'City'}
        categorical_data = {key: value for key, value in data.items() if key == 'Speciality' or key == 'City'}

        # Create new DataFrame for numerical data
        df_numerical = pd.DataFrame(numerical_data)

        # Standardize numerical columns
        scaler = StandardScaler()
        df_numerical_scaled = scaler.fit_transform(df_numerical)
        df_numerical_scaled = pd.DataFrame(df_numerical_scaled, columns=df_numerical.columns)

        # Create new columns for categorical data
        df_categorical = pd.DataFrame(columns=categorical_data.keys())

        # Set values in categorical columns to 1 where the original data has the corresponding value
        for col, val in categorical_data.items():
            unique_values = set(val)
            for unique_val in unique_values:
                df_categorical[f"{col}_{unique_val}"] = [1 if v == unique_val else 0 for v in val]

        # Concatenate numerical and categorical DataFrames
        df_final = pd.concat([df_numerical_scaled, df_categorical], axis=1)

        df_final.drop(columns=['Speciality','City'],axis=1,inplace=True)

        # Create test data for prediction
        raw_data = {
            "Years of Experience": [0],
            "DP Score": [0],
            "NPV": [0],
            "Speciality_Bariatric_Surgeon": [0],
            "Speciality_Cardiologist": [0],
            "Speciality_Chiropractor": [0],
            "Speciality_Dentist": [0],
            "Speciality_Dermatologist": [0],
            "Speciality_Dietetian": [0],
            "Speciality_Gastroenterologist": [0],
            "Speciality_Gynecologist": [0],
            "Speciality_Infertility_Specialist": [0],
            "Speciality_Neurologist": [0],
            "Speciality_Neurosurgeon": [0],
            "Speciality_Ophthalmologist": [0],
            "Speciality_Orthopedist": [0],
            "Speciality_Pediatrician": [0],
            "Speciality_Physiotherapist": [0],
            "Speciality_Psychiatrist": [0],
            "Speciality_Pulmonologist": [0],
            "Speciality_Rheumatologist": [0],
            "Speciality_Urologist": [0],
            "City_Bangalore": [0],
            "City_Delhi": [0],
            "City_Mumbai": [0]
        }

        test_data = pd.DataFrame(raw_data)

        values_to_update = df_final[['Years of Experience', 'DP Score', 'NPV']].values.flatten()
        test_data['Years of Experience'] = [values_to_update[0]]
        test_data['DP Score'] = [values_to_update[1]]
        test_data['NPV'] = [values_to_update[2]]
        test_data[df_final.columns.tolist()[3]] = [1]
        test_data[df_final.columns.tolist()[4]] = [1]

        # Make predictions for the processed data point
        predictions = loaded_model.predict(test_data)

        predicted_fee = int(predictions[0])

        # Render template with form data and predicted fee
        return render_template('result.html', predicted_fee=predicted_fee)
    # If it's a GET request, just render the form template
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
