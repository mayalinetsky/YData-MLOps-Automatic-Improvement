"""
Functions matching the various implementation steps of the baseline model 'XGBoost 1b'
"""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder

from data_acquisition.german_credit_loading import GERMAN_CREDIT_CATEGORICAL_COLS, GERMAN_CREDIT_NUMERICAL_COLS
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier


def get_feature_preprocessor_step():
    """

    :return: pipeline step which preprocesses the features of the bank marketing dataset
    """
    preprocessor = ColumnTransformer(
        transformers=[
            ('numerical_scaler', StandardScaler(), GERMAN_CREDIT_NUMERICAL_COLS),
            ('onehot', OneHotEncoder(handle_unknown='ignore', sparse=False), GERMAN_CREDIT_CATEGORICAL_COLS)
        ])
    return preprocessor


def preprocess_labels(target_col: pd.Series):
    return target_col.replace([1, 2], [1, 0])


def get_model_for_training(X_train, y_train, X_test, y_test):
    params2 = {
        'n_estimators': 3000,
        'objective': 'binary:logistic',
        'learning_rate': 0.005,
        # 'gamma':0.01,
        'subsample': 0.555,
        'colsample_bytree': 0.7,
        'min_child_weight': 3,
        'max_depth': 8,
        # 'seed':1024,
        'n_jobs': -1
    }
    eval_set = [(X_train, y_train), (X_test, y_test)]
    fit_params = dict(eval_set=eval_set,
                      eval_metric='auc', early_stopping_rounds=100)
    # todo the original notebook fits the model two times, how to integrate it?
    return XGBClassifier(**params2), fit_params


# fit, train and cross validate Decision Tree with training and test data
def xgbclf(params, X_train, y_train, X_test, y_test):
    eval_set = [(X_train, y_train), (X_test, y_test)]

    model = XGBClassifier(**params).fit(X_train, y_train, eval_set=eval_set,
                                        eval_metric='auc', early_stopping_rounds=100, verbose=100)

    # todo why did the original developer fit the model again?
    model.set_params(**{'n_estimators': model.best_ntree_limit})
    model.fit(X_train, y_train)

    # Predict target variables y for test data
    y_pred = model.predict(X_test, ntree_limit=model.best_ntree_limit)

    # Predict probabilities target variables y for test data
    # y_pred_proba = model.predict_proba(X_test, ntree_limit=model.best_ntree_limit)[:, 1]  # model.best_iteration
    return model
