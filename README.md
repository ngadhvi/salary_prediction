# Salary Prediction
The goal of the project is to develop an Advanced Predictive Model for salary predictions. Here, we are given train_features.csv and train_salaries.csv. Crunching these in our model to predict salaries for the job descriptions given in the test_features.csv.

For simplicity and better understanding, the project has been segmented into 4 sections as seperate [Jupyter notebooks](https://jupyter.org). Raw data is kept seperate from the data we would be using and playing with during the development process.

The directory structure is as follows:

salary_prediction

           |-- raw_data                  <-- Contains the untouched downloaded data 
           |-- derived_data              <-- Unzipped files from the raw data. We will use files in this folder to work with
           |-- models                    <-- Has the trained model to do test/inference with
           |-- 01_Data_Prep.ipynb        <-- 
           |-- 02_Data_Exploration.ipynb
           |-- 03_Preprocessing.ipynb
           |-- 04_Model_Tuning.ipynb
                    
