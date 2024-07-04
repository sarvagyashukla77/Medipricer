
![P_lat](https://github.com/digvijaytatrari/MediPricer/assets/37079322/deb5958f-5b22-4fad-9988-e0951740063a)


# Doctor Fee Prediction
Our objective is to develop a user-friendly web interface for predicting doctor consultation fees. The predictive model employed in this project was trained on a meticulously curated dataset derived from web scraping Practo, utilizing Selenium for data acquisition. Python's Pandas library facilitated robust data cleaning and preprocessing, ensuring the reliability and accuracy of our predictions.
<br>

## What our analysis says?

- Based on the dataset extracted from Practo, Bangalore emerges as the city boasting the most significant concentration of healthcare professionals.
<br>

![Screenshot 2024-03-31 163401](https://github.com/digvijaytatrari/MediPricer/assets/37079322/7be954e5-0d28-472d-8365-4d0b17978308)
<br>


- The dataset highlights three primary specialties that dominate among doctors:
  - Dentistry
  - Gynecology
  - Pediatrics

![Screenshot 2024-03-31 163939](https://github.com/digvijaytatrari/MediPricer/assets/37079322/ab974d65-9d12-4588-8820-d366e03f079b)


<br>



<be>

## Steps in Model Creation and Storing

1. Data Collection: Acquired doctor-related data from Practo through web scraping methodologies employing Selenium.

2. Data Preprocessing: Executed meticulous data cleaning processes, handling missing data effectively, and encoding categorical variables into numerical formats.

3. Feature Engineering: Enhanced dataset comprehensiveness by deriving supplementary features, including the extraction of qualifications and specialized certifications.

4. Model Selection: Explored a spectrum of regression algorithms, assessing their suitability based on initial performance metrics.

5. Hyperparameter Tuning: Leveraged GridSearchCV to fine-tune model hyperparameters, optimizing predictive performance for each selected algorithm.

6. Model Training: Conducted comprehensive training sessions for multiple models, integrating tuned hyperparameters to enhance predictive accuracy.

7. Weighted Voting: Implemented a sophisticated Weighted Voting mechanism, amalgamating predictions from diverse models with individualized weights.

8. Model Evaluation: Scrutinized ensemble model performance using pertinent evaluation metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

9. Web App Development: Developed an intuitive web application interface using Flask, HTML, and CSS, facilitating seamless user interaction and parameter input.

<br>

## Doctor Consultation Fee Prediction Web Application

#### User Input Interface
- Here users gives its input for predicting Doctor Fee
<br>

![Screenshot 2024-04-01 083005](https://github.com/digvijaytatrari/MediPricer/assets/37079322/4060776f-1a93-459b-945d-bc807ffe45ad)

- After submitting input Model will predict and show the Doctor Fee
<br>

![Screenshot 2024-04-01 081258](https://github.com/digvijaytatrari/MediPricer/assets/37079322/a8cfdfbe-4859-4c9a-96a6-dc83b8b01338)

## Obstacles and Insights

- Data Retrieval: Initially, we encountered challenges in extracting data from the server, requiring exploration and problem-solving to navigate the process effectively.

- Model Exploration: Delved into various machine learning models to pinpoint the most suitable candidates for our prediction task.

- Hyperparameter Optimization: Tuning hyperparameters proved time-intensive, given the constraints on model development time.

- Webpage Development: The creation of the webpage posed both challenges and excitement as we ventured into this new concept, fostering a rewarding learning experience.

<br>

## Conclusion
- Enhancing Healthcare Accessibility: Providing patients with insights into potential costs empowers them to pursue suitable medical treatment without the hindrance of fee-related uncertainty.

- Building Transparency and Trust: Transparent fee estimates cultivate trust and confidence in medical services, strengthening the bond between doctors and patients and fostering long-lasting relationships built on mutual respect.

- Streamlining Provider Operations: By making fee estimates readily accessible, administrative tasks are streamlined, resulting in smoother processes and ultimately enhancing the overall efficiency of healthcare service delivery.

- Patient Empowerment: Equipping patients with knowledge about healthcare costs enables them to make informed decisions and take charge of their healthcare journey with confidence.

- Strengthening Patient-Provider Communication: Clear fee estimates facilitate open and honest discussions between patients and providers, leading to improved communication and better treatment outcomes.





