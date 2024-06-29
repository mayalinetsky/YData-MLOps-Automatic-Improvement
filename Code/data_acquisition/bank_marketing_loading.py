import pandas as pd
from ucimlrepo import fetch_ucirepo


def load_bank_marketing_dataset() -> pd.DataFrame:
    """
    Column 'y' is the target column.
    :return:
    """
    bank_marketing_raw_data = fetch_ucirepo(id=222)

    bank_marketing_features_df = bank_marketing_raw_data.data.features

    bank_marketing_target_df = bank_marketing_raw_data.data.targets

    bank_marketing_raw_data_df = bank_marketing_features_df.join(bank_marketing_target_df)

    return bank_marketing_raw_data_df
