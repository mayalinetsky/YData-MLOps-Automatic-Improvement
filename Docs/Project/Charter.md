# Project Charter

## Business background

* (Who is the client, what business domain the client is in.) The "clients" are two baseline XGBoost models that were 
trained on the Bank Marketing Dataset and the German Credit Risk Dataset.  
* (What business problems are we trying to address?) This project aims to dynamically improve the models' overall 
performance. 

## Scope
* What data science solutions are we trying to build?
* What will we do?
* How is it going to be consumed by the customer?
The project's scope will be to design and implement a basic ML pipeline for each model, that would contain an automatic 
step that would improve the overall performance of the model in any method that does not involve changing the model's
type or hyperparameters and is not dataset-specific.

## Personnel
* Team:
    * Product Manager: (name). Will be responsible about directing the project to meet the need of the hypothetical clients.
    * Data Scientist: (name). EDA, model understanding.
    * Data Engineer (name). Data Expert. Loading and processing.
    * Architect (name). Repository structure, Code reviews, code design.
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
