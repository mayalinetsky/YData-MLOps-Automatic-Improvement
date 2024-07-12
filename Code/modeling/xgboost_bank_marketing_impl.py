"""
Module implementing the ML pipeline which solves the bank marketing classification problem:

- Feature Engineering
- preprocessing
- model selection
- training
"""
from pathlib import Path
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from data_acquisition.bank_marketing_constants import DEPOSIT, DEPOSIT_NO, DEPOSIT_YES, CATEGORICAL_COLUMNS
import pandas as pd
import xgboost

DEPOSIT_YES_INT = 1
DEPOSIT_NO_INT = 0


def preprocess_data(bank_marketing_raw_data_df: pd.DataFrame):
    """

    :param bank_marketing_raw_data_df:
    :return: X_features, y_labels which are ready for XGBoost
    """
    object_feature_cols = bank_marketing_raw_data_df.select_dtypes(include='object').columns.drop(DEPOSIT,
                                                                                                  errors='ignore').values
    bank_marketing_dummy_df = pd.get_dummies(bank_marketing_raw_data_df, columns=object_feature_cols)

    data_y = pd.DataFrame(preprocess_labels(bank_marketing_dummy_df[DEPOSIT]))
    data_X = bank_marketing_dummy_df.drop([DEPOSIT], axis=1)

    return data_X, data_y


def get_feature_preprocessor_step():
    """

    :return: pipeline step which preprocesses the features of the bank marketing dataset
    """
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', categorical_transformer, CATEGORICAL_COLUMNS)
        ])
    return preprocessor


def preprocess_labels(deposit: pd.Series):
    return deposit.replace(to_replace={DEPOSIT_YES: 1, DEPOSIT_NO: 0})


def train_model(X: pd.DataFrame, y: pd.DataFrame):
    """
    Train XGBoost model on the given data as done so in the Kaggle notebook
    :param X:
    :param y:
    :return: model with a predict method which returns class probabilities
    """
    dtrain = xgboost.DMatrix(X, label=y)
    params = {
        'objective': 'multi:softprob',
        'max_dept': 4,
        'silent': 1,
        'eta': 0.3,
        'gamma': 0,
        'num_class': 2
    }
    num_rounds = 20
    XGB_Model = xgboost.train(params, dtrain, num_rounds)
    return XGB_Model


def evaluate_predictions_roc_auc_score(y_true: np.ndarray | pd.DataFrame, predicted_probas: np.ndarray):
    """

    :param y_true: shape (n_samples,)
    :param predicted_probas: shape (n_samples, 2) where predicted_probas[:, 1] are predicted probabilities for the positive class DEPOSIT_YES_INT
    :return:
    """
    predicted_proba_of_positive = predicted_probas[:, 1]
    roc_auc_score_val = roc_auc_score(y_true, predicted_proba_of_positive)
    return roc_auc_score_val


def load_trained_bank_marketing_model() -> xgboost.Booster:
    model = xgboost.Booster(model_file=Path(__file__).parent / 'baseline_bank_marketing.json')
    return model


if __name__ == '__main__':
    model = load_trained_bank_marketing_model()
    print(model)
