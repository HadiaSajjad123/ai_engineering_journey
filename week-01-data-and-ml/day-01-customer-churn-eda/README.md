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

- Dataset dimensions: [Fill in actual result]
- Duplicate records: [Fill in actual result]
- Columns with missing values: [Fill in actual result]
- Observed churn rate: [Fill in actual result]
- Highest-churn contract segment: [Fill in actual result]

## Limitations

This project is descriptive exploratory data analysis. The observed relationships do not establish causation, and no predictive model has been evaluated yet.

## Next Steps

- Investigate missing and inconsistent values.
- Build a reproducible preprocessing pipeline.
- Establish a machine learning baseline.
- Evaluate model performance and error trade-offs.