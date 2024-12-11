from kaggle.api.kaggle_api_extended import KaggleApi
import os

os.makedirs('../data', exist_ok=True)

api = KaggleApi()
api.authenticate()


api.dataset_download_files('aungpyaeap/supermarket-sales', path='../data', unzip=True)
print("Data downloaded and extracted to data folder.")
