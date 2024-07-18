# Project Charter

## Business background


* (Who is the client, what business domain the client is in.) 
  
  The potential clients are companies in the financial 
  domain which already employ ML supervised models to classify client behaviour.
  For example a banks marketing branch using xgboost classifier to predict the response to an ad campaign,
  or  a credit risk assessor  using  random forest classifier to predict borrowers probability to default on their loan .  


* (What business problems are we trying to address?) 

  These businesses deal not only with accuracy of their
  accuracy of their predictions but also with the confidence of the prediction , therefore by improving the accuracy
  of the probabilities prediction, the businesses will be able to
  increase its revenue


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
* Data acquisition - Simple modules for fetching the source datasets, extracting the features and the labels and compose a model-suitable raw dataset.
  * bank_marketing_constants: mostly column names
  * bank_marketing_loading: fetching, extracting and composing dataset for bank marketing
  * german_credit_loading: column names; fetching, extracting and composing dataset for bank marketing
* Modeling - implementation of XGBoost model for bank marketing and german credit
  * Loading the model (in bank marketing as a json tree; in german credit direct load)
  * Define functions for preprocessing, training and evaluation
* Auto-improve pipeline - set MetaModelClassification as a meta-model class  
  * Can be used to extract confidence scores from black-box classification
  * Usage can be done importing the class from the package and use it either as is, or in an sklearn pipeline 

## Communication
* A Slack channel with all team members
* Task-oriented work meetings
