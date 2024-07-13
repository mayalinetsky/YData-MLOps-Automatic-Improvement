Automatic Improvement Using MetaModelClassification
====
MetaModelClassification Extracts confidence scores from black-box classification models using a meta-model.

# Usage
Import the MetamodelClassification class from the package.
```python
from auto_improve_pipeline import *

auto_improve_model = MetamodelClassification(base_model=your_model,
                                             meta_model=pick_something)
```
And use it as is, or in a sklearn pipeline.
See [example usage notebook](../notebooks/auto_improve_example_usage.ipynb).