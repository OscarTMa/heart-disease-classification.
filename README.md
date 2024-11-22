# Heart Disease Classification
## Table of Contents
1. [Description](#description)
2. [Dataset](#dataset)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Contributing](#contributing)
7. [License](#license)
8. [Analysis](#analysis)
9. [Heart Disease Prediction Dashboard](#heart-disease-prediction-dashboard).
    
## Description                                                      
This project aims to classify the presence of heart disease using the Heart Disease UCI dataset. It explores various machine learning algorithms to predict whether a patient is likely to have heart disease based on medical attributes such as age, cholesterol levels, blood pressure, and more.

The goal is to demonstrate expertise in:

- Data preprocessing and exploratory data analysis (EDA).
- Building and evaluating classification models.
- Developing an interactive dashboard for visualizing predictions.

## Dataset

The dataset is sourced from Kaggle: Heart Disease UCI Dataset.
It contains 14 features, including both numerical and categorical variables, and a target column (target) indicating the presence (1) or absence (0) of heart disease.

## Installation
To run the project locally, follow these steps:

1. Clone this repository:                               
   ```bash
   git clone https://github.com/oscarTMa/heart-disease-classification.git

2. Navigate to the project directory:                                    
   ```bash
   cd heart-disease-classification

3. Install the required Python libraries:                          
   ```bash
   pip install -r requirements.txt

# Usage
   Notebook:                                    
    The initial analysis and modeling will be conducted in a Jupyter Notebook, hosted in Google Colab. The notebook file can be found in the notebooks/ directory.

   Dashboard:
    An interactive dashboard will be built using Streamlit to showcase predictions and insights. Instructions for running the dashboard will be added in later stages.

## Project Structure

heart-disease-classification/                                         
│                                      
├── README.md               # Project documentation                                            
├── .gitignore              # Ignored files and directories                                           
├── requirements.txt        # Python dependencies                                                
├── notebooks/              # Jupyter/Colab notebooks for analysis                               
├── src/                    # Source code for preprocessing and models                            
└── app.py                  # Streamlit app for the interactive dashboard                       

## Contributing                   

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## License                                                           

This project is licensed under the MIT License. See the LICENSE file for details.

## Analysis (see the notebook)

**1. Logistic Regression**
- Accuracy: 0.8533                 
- ROC AUC: 0.8556                 
- Classification Report:               
    - Precision: The model performs well in both classes, with a precision of 0.80 for class 0 and 0.90 for class 1. This indicates good performance in classifying both classes.
    - Recall: The recall for class 0 is high (0.87), meaning the model is correctly identifying many of the negative cases. However, the recall for class 1 is slightly lower (0.84), indicating that some positive cases are being missed.
    - F1-Score: The F1-score for class 1 is higher (0.87) compared to class 0 (0.83), suggesting the model performs slightly better at predicting class 1.  

- Confusion Matrix: The model has some false positives and false negatives, but overall, it is fairly balanced.

**2. Decision Tree**                           
- Accuracy: 0.8370
- ROC AUC: 0.8325
- Classification Report:
    - Precision: Similar to Logistic Regression, the model shows good precision for both classes, with a slight difference (0.81 for class 0 and 0.86 for class 1).
    - Recall: The recall is fairly balanced, with 0.81 for class 0 and 0.86 for class 1. However, recall is not as high as Logistic Regression's for class 1.
    - F1-Score: The F1-score is quite similar for both classes (0.81 for class 0 and 0.86 for class 1), indicating a reasonable but not exceptional performance.
- Confusion Matrix: The model shows some errors (false positives and false negatives), but it is performing reasonably well.

**3. Random Forest**
- Accuracy: 0.8750
- ROC AUC: 0.8725
- Classification Report:
     - Precision: The model shows excellent precision for class 1 (0.90) and good precision for class 0 (0.85).
     - Recall: The recall for class 1 is very high (0.89), and recall for class 0 is 0.86, indicating a good balance in capturing both types of classes.
     - F1-Score: The F1-score is also high for both classes, with 0.85 for class 0 and 0.89 for class 1. The model demonstrates balanced performance across both classes.
- Confusion Matrix: The confusion matrix shows that the model makes few errors, achieving solid performance with minimal false positives and false negatives.

**4. XGBoost**
- Accuracy: 0.8587
- ROC AUC: 0.8603
- Classification Report:
    - Precision: Precision is quite high for class 1 (0.90) and decent for class 0 (0.81). The model performs well in classifying the positive class.
    - Recall: The recall for class 0 is 0.87, and for class 1, it is slightly lower (0.85). This suggests that the model is good at capturing negative cases but may miss some positive cases.
    - F1-Score: The F1-score is 0.88 for class 1, which is the best among all models. For class 0, it is 0.84, which is also very good.
- Confusion Matrix: The confusion matrix shows solid performance, but the model has some errors in predicting the positive class (false negatives).

**Conclusions and Recommendations:**

- **Best Model:** The Random Forest model appears to perform the best overall with the highest accuracy (0.875) and ROC AUC (0.8725). It also maintains a good balance between precision and recall for both classes.
- **Good Model:** XGBoost also provides strong results, with high precision and recall for class 1, though it is slightly inferior to Random Forest in terms of accuracy.
- **Simple Models**: **Logistic Regression** is fast and effective but has a slightly lower recall for class 1 compared to other models. It also has lower **accuracy** compared to Random Forest and XGBoost.
- **Decision Tree**: While the Decision Tree model has a good accuracy, its performance is slightly lower than the other models, particularly in terms of **ROC AUC** and balance between precision and recall.

To improve performance, **Random Forest** or **XGBoost** are the most robust models, which we can explore further, possibly with **hyperparameter tuning** to achieve better results.

## Heart Disease Prediction Dashboard
Explore the interactive dashboard [here](https://heart-disease-classification-tk7y5shpqsbjxenm6sunxm.streamlit.app/).  



