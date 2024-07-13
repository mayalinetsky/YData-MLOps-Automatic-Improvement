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
    * Trained XGBoost models?
	
## Metrics
Both baseline models were evaluated using Accuracy.
The performance of our automatic improvement step will be measured by the % change of the model's accuracy, from before 
applying the step and after: (acc_after-acc_before)/acc_before*100. 

## Plan
* Phases (milestones), timeline, short description of what we'll do in each phase.

## Architecture
* Data
  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)
* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
  * all the data, 
  * after some pre-aggregation on-prem,
  * Sampled data enough for modeling 

* What tools and data storage/analytics resources will be used in the solution e.g.,
  * ASA for stream aggregation
  * HDI/Hive/R/Python for feature construction, aggregation and sampling
  * AzureML for modeling and web service operationalization
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Communication
* How will we keep in touch? Weekly meetings?
* Who are the contact persons on both sides?
