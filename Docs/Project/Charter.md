# Project Charter

## Business background

* (Who is the client, what business domain the client is in.) The "clients" are two baseline XGBoost models that were 
trained on the Bank Marketing Dataset and the German Credit Risk Dataset.  
* (What business problems are we trying to address?) This project aims to dynamically improve the models' overall 
performance. 

## Scope
* What data science solutions are we trying to build?<br>
We were trying to implement a post-hoc framework by IBM, called Uncertainty Quantification 360.
The UQ360 takes the predictions of the costumers model (i.e. base model), and trains a metamodel to predict on what samples the base model is going to predict wrong.<br><br>
* What will we do? <br>
The frameworp adds the metamodel as a wrapper to the base model, which is pre-trained and whose parameters are inaccessible.<br><br>
* How is it going to be consumed by the customer?<br>
We provide the costumer with an API that uses the UQ360 and implements an additional step that may be used instead of their existing model.<bR>
An example notebook is provided at: [baseline-impl-bank-marketing-dataset](https://github.com/mayalinetsky/YData-MLOps-Automatic-Improvement/blob/1389f8bebf4eccd8e390ecbd7c7b6e4ae9161a29/Code/notebooks/baseline-impl-bank-marketing-dataset.ipynb)

## Personnel
* Team:
    * Project Lead: Eran.
    * Product Manager: Adir. Responsible about directing the project to meet the need of the hypothetical clients.
    * Data Scientist: Avital. EDA, model understanding.
    * Data Engineer: Ben. Data Expert. Loading and processing.
    * Architect: Maya. Repository structure, Code reviews, code design.
* Client:
    * Data scientists, software developers and companies that have a working model that sub-performs, but can't or wish to avoid re-training and changing the model.
	
## Metrics
Both baseline models were evaluated using Accuracy.
The performance of our automatic improvement step will be measured by the % change of the model's accuracy, from before 
applying the step and after: (acc_after-acc_before)/acc_before*100. 

## Architecture
* Data... TBD
* Model... TBD
* Metamodel... TBD


## Communication
* A Slack channel with all team members
* Task-oriented work meetings
