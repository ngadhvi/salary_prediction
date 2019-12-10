# Salary Prediction (In Progress)
The goal of the project is to develop an Advanced Predictive Model for salary predictions. Here, we are given train_features.csv and train_salaries.csv. Crunching these in our model to predict salaries for the job descriptions given in the test_features.csv.

For simplicity and better understanding, the project has been segmented into 4 sections as separate [Jupyter notebooks](https://jupyter.org). Raw data is kept separate from the data we would be using and playing with during the development process.

>The directory structure is as follows:
```bash
salary_prediction
           ├── raw_data                   # Contains the untouched downloaded data [Avoided in Git due to space requirements by Git]
           ├── derived_data               # Unzipped files from the raw data. We will use files in this folder to work with
           ├── models                     # Has the trained model to do test/inference with
           ├── 01_Data_Prep.ipynb         # Load the data in the panda frame and get the context of the data 
           ├── 02_Data_Exploration.ipynb  # Perform EDA on the given data
           ├── 03_Preprocessing.ipynb     # We will perform preprocessing on the data like cleaning, summarizing feature variable, target variable, finding correlation
           ├── 04_Model_Tuning.ipynb      # Setting up a base line model and further comparing with a few more to improve the performance
	   ├── README.md
           └── extras.ipynb
```                    
