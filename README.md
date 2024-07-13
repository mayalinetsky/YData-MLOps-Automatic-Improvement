YData-MLOps-Automatic-Improvement
=================================
MLOps project of a pipeline which contains an automatic step which improves a model's performance.

# Usage

## Dependencies
This project's dependencies are managed using [poetry](https://python-poetry.org/).
To install dependencies, see [installing dependencies](https://python-poetry.org/docs/basic-usage/#installing-dependencies).

## API
Say you have an XGBoost model you've already trained, and you want to increase its log loss metric automatically. 
You've come to the right place.

The only class you need is MetamodelClassification.

See [example usage notebook](Code/notebooks/auto_improve_example_usage.ipynb).



# Credits
Project template was taken from [Azure-TDSP-ProjectTemplate](https://github.com/Azure/Azure-TDSP-ProjectTemplate/blob/master/Docs/Model/Baseline/Baseline%20Models.md).
