import pandas as pd


def get_results(model, cols, scaler):
    upcoming = pd.read_csv('csv-files/upcoming-event.csv')
    selected = upcoming.loc[:, cols].drop("Winner", axis=1).dropna(axis=0)

    if len(selected) < 5:
        upcoming = pd.read_csv('csv-files/most-recent-event.csv')
        selected = upcoming.loc[:, cols].drop("Winner", axis=1).dropna(axis=0)

    fighters = upcoming.loc[selected.index, ["R_fighter", "B_fighter"]]

    scaled_features = scaler.transform(selected)
    predictions = model.predict(scaled_features)

    formatted = pd.DataFrame(
        data={
            "Red Fighter": fighters.loc[:, "R_fighter"],
            "Blue Fighter": fighters.loc[:, "B_fighter"],
            "Predictions": [f"{color} Fighter" for color in predictions]
        },

        index=fighters.index
    )

    formatted.loc[:, "Predictions"] = formatted.index.map(lambda idx: formatted.loc[idx, formatted.Predictions.loc[idx]])

    return [{
        f"{formatted.loc[idx, 'Red Fighter']} vs. "
        f"{formatted.loc[idx, 'Blue Fighter']}": formatted.loc[idx, 'Predictions']
    } for idx in formatted.index]
