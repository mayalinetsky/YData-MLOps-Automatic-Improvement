"""
Module for loading the trained model.
"""
from pathlib import Path
import xgboost


def load_trained_bank_marketing_model() -> xgboost.Booster:
    model = xgboost.Booster(model_file=Path(__file__).parent / 'baseline_bank_marketing.json')
    return model


if __name__ == '__main__':
    model = load_trained_bank_marketing_model()
    print(model)
