from kaggle.api.kaggle_api_extended import KaggleApi
from os.path import join, dirname
from dotenv import load_dotenv
import os


def download_data():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    api_client = {
        "username": os.environ.get('KAGGLE_USERNAME'),
        "key": os.environ.get('KAGGLE_KEY')
    }

    api = KaggleApi(api_client=api_client)
    api.authenticate()

    api.dataset_download_file(
        'mdabbert/ultimate-ufc-dataset',
        file_name='upcoming-event.csv',
    )
