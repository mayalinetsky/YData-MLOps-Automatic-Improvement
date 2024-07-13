# Baseline Model Report for Bank Marketing Dataset

> The baseline model for this dataset was originally implemented [here](https://www.kaggle.com/code/kevalm/xgboost-implementation-on-bank-marketing-dataset?scriptVersionId=2074012) 

## Analytic Approach
The Bank Marketing Dataset is related with direct marketing campaigns (phone calls) of a Portuguese banking institution. 
The classification goal is to predict if the client will subscribe a term deposit (variable y - boolean).
The chosen baseline model is XGBoost.

## Model Description

* DMatrix from xgboost package
	* See training in [xgboost_bank_marketing_impl.py](../../../Code/notebooks/baseline-impl-bank-marketing-dataset.ipynb)


## Results (Model Performance)
The model was evaluated using the accuracy metric, on 30% of the data.
* Accuracy of 90.76%
* Log Loss: 

## Model Understanding

* Variable Importance (significance): see "baseline_bank_marketing_tree.png"
