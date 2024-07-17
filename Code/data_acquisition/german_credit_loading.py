import pandas as pd
from ucimlrepo import fetch_ucirepo

COLUMN_NAMES = ['existingchecking', 'duration', 'credithistory', 'purpose', 'creditamount',
                'savings', 'employmentsince', 'installmentrate', 'statussex', 'otherdebtors',
                'residencesince', 'property', 'age', 'otherinstallmentplans', 'housing',
                'existingcredits', 'job', 'peopleliable', 'telephone', 'foreignworker', 'classification']

GERMAN_CREDIT_CATEGORICAL_COLS = ['existingchecking', 'credithistory', 'purpose', 'savings', 'employmentsince',
                                  'statussex', 'otherdebtors', 'property', 'otherinstallmentplans', 'housing', 'job',
                                  'telephone', 'foreignworker']

GERMAN_CREDIT_NUMERICAL_COLS = ['creditamount', 'duration', 'installmentrate', 'residencesince', 'age',
                                'existingcredits', 'peopleliable']
"""Numerical columns, except for the target column"""

TARGET_COL = 'classification'


def load_german_credit_risk_dataset() -> pd.DataFrame:
    """
    Column TARGET_COL is the target column.
    :return:
    """
    german_credit_raw_data = fetch_ucirepo(id=144)

    german_credit_features_df = german_credit_raw_data.data.features

    german_credit_target_df = german_credit_raw_data.data.targets

    german_credit_raw_data_df = german_credit_features_df.join(german_credit_target_df)

    german_credit_raw_data_df.columns = COLUMN_NAMES

    return german_credit_raw_data_df


if __name__ == '__main__':
    df = load_german_credit_risk_dataset()
    print(df)
