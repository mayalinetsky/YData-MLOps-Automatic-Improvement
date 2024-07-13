

class AutoImproveStepPreTraining:
    """
    Use this step as a part of a sklearn pipeline in order to improve model performance automatically:

    ```python
    pipe = Pipeline(steps=[('autoimprove', AutoImproveStepPreTraining()),
                        ('yourmodel', YourModel())])
    ```
    """
    def __init__(self, *args, **kwargs):
        pass

    def fit(self, X, y):
        pass

    def transform(self, X, y):
        pass


class AutoImproveStepPostTraining:
    """
    Use this step as a part of a sklearn pipeline in order to improve model performance automatically,
    after you've already trained your base model:

    ```python
    pipe = Pipeline(steps=[('autoimprove', AutoImproveStepPostTraining(base_model=your_model))])
    ```
    """
    def __init__(self, *args, **kwargs):
        pass

    def fit(self, X, y):
        pass

    def predict(self, X, y):
        pass
