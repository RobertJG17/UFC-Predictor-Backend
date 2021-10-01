# UFC Predictor Backend

This repository was created to act as a live backend for the model I evaluated and trained through various jupyter notebooks. I built this using Flask as an intermediary to serve JSON structured predictions for upcoming events. Since this current implementation depends on the availability of data via Kaggle, I implemented a minimum number of non NaN entries that must be satisfied in order to begin showing predictions for the next card. If this minimum is not satisfied, then the information returned from the endpoint will be the predictions from the previous event.

[Live Endpoint](https://bout-predictor.herokuapp.com/)

## Implementation for Python Kaggle Wrapper

```
from kaggle.api.kaggle_api_extended import KaggleApi
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
import os


def download_data():
    load_dotenv(find_dotenv())
    api_client = {
        "username": os.environ.get('KAGGLE_USERNAME'),
        "key": os.environ.get('KAGGLE_KEY')
    }

    api = KaggleApi(api_client=api_client)
    api.authenticate()

    for file in ['most-recent-event.csv', 'upcoming-event.csv']:
        api.dataset_download_file(
            'mdabbert/ultimate-ufc-dataset',
            file_name=file,
            path='csv-files'
        )

```

## Example Predictions from UFC 267

```
[
  {
    "Alexander Volkanovski vs. Brian Ortega": "Alexander Volkanovski"
  },
  {
    "Valentina Shevchenko vs. Lauren Murphy": "Valentina Shevchenko"
  },
  {
    "Nick Diaz vs. Robbie Lawler": "Robbie Lawler"
  },
  {
    "Curtis Blaydes vs. Jairzinho Rozenstruik": "Curtis Blaydes"
  },
  {
    "Jessica Andrade vs. Cynthia Calvillo": "Jessica Andrade"
  },
  {
    "Marlon Moraes vs. Merab Dvalishvili": "Merab Dvalishvili"
  },
  {
    "Dan Hooker vs. Nasrat Haqparast": "Nasrat Haqparast"
  },
  {
    "Shamil Abdurakhimov vs. Chris Daukaus": "Chris Daukaus"
  },
  {
    "Roxanne Modafferi vs. Taila Santos": "Taila Santos"
  },
  {
    "Uros Medic vs. Jalin Turner": "Jalin Turner"
  },
  {
    "Cody Brundage vs. Nick Maximov": "Nick Maximov"
  },
  {
    "Jonathan Pearce vs. Omar Morales": "Omar Morales"
  }
]

```
