# Customer Churn — Exploratory Data Analysis

## Overview

This project investigates customer churn in a telecommunications dataset using Python. The goal is to understand data quality, customer characteristics, and observed churn patterns before developing a machine learning model.

## Problem Statement

Customer churn can affect recurring revenue and customer retention. Before building a predictive system, we need to understand the available data, identify quality issues, and investigate which customer segments show different churn rates.

## Objectives

- Inspect dataset structure and data types.
- Identify missing values and duplicate records.
- Analyze the target variable and observed churn rate.
- Compare churn rates across contract types.
- Produce reusable reports and visualizations.

## Tech Stack

- Python
- pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Git and GitHub

## Project Structure

- `data/` — locally stored dataset
- `notebooks/` — interactive exploratory analysis
- `src/` — reusable analysis code
- `reports/` — generated summaries and charts

## How to Run

1. Create and activate a Python virtual environment.
2. Install dependencies using `pip install -r requirements.txt`.
3. Download the dataset from the source linked below and place it in `data/`.
4. Run `python src/eda.py`.
5. Open the notebook in Jupyter to explore the findings.

## Dataset

Telco Customer Churn dataset: [Public dataset repository](https://github.com/fenago/datasets/blob/main/WA_Fn-UseC_-Telco-Customer-Churn.csv).

Check the dataset's original provenance and applicable license or terms before redistribution.

## Findings

- Dataset dimensions: Shape: (7043, 21)
- Duplicate records: Duplicate rows: 0
- Columns with missing values: <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>missing_values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>customerID</th>
      <td>0</td>
    </tr>
    <tr>
      <th>gender</th>
      <td>0</td>
    </tr>
    <tr>
      <th>SeniorCitizen</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Partner</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Dependents</th>
      <td>0</td>
    </tr>
    <tr>
      <th>tenure</th>
      <td>0</td>
    </tr>
    <tr>
      <th>PhoneService</th>
      <td>0</td>
    </tr>
    <tr>
      <th>MultipleLines</th>
      <td>0</td>
    </tr>
    <tr>
      <th>InternetService</th>
      <td>0</td>
    </tr>
    <tr>
      <th>OnlineSecurity</th>
      <td>0</td>
    </tr>
    <tr>
      <th>OnlineBackup</th>
      <td>0</td>
    </tr>
    <tr>
      <th>DeviceProtection</th>
      <td>0</td>
    </tr>
    <tr>
      <th>TechSupport</th>
      <td>0</td>
    </tr>
    <tr>
      <th>StreamingTV</th>
      <td>0</td>
    </tr>
    <tr>
      <th>StreamingMovies</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Contract</th>
      <td>0</td>
    </tr>
    <tr>
      <th>PaperlessBilling</th>
      <td>0</td>
    </tr>
    <tr>
      <th>PaymentMethod</th>
      <td>0</td>
    </tr>
    <tr>
      <th>MonthlyCharges</th>
      <td>0</td>
    </tr>
    <tr>
      <th>TotalCharges</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Churn</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
- Observed churn rate: 26.54%
- Highest-churn contract segment: month-month

## Limitations

This project is descriptive exploratory data analysis. The observed relationships do not establish causation, and no predictive model has been evaluated yet.

## Next Steps

- Investigate missing and inconsistent values.
- Build a reproducible preprocessing pipeline.
- Establish a machine learning baseline.
- Evaluate model performance and error trade-offs.