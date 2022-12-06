from google.cloud import firestore
import pandas as pd

contatori = pd.read_csv("dataset/contatori.csv", sep=",")

db = firestore.Client.from_service_account_json('credentials.json')
for item, row in contatori.iterrows():
    db.collection("lista contatori").document(str(int(row.n_serie))).set({
        "lat": str(row.lat), "long": str(row.long)
    })

# creazione dataframe 'contatori' con ogni contatore e lat e long casuali
# contatori = pd.DataFrame(
#    {'n_serie': df["Numero di serie del contatore"].unique()})
# contatori["lat"] = contatori.apply(lambda row: lat+(0.5-random())/100, axis=1)
# contatori["long"] = contatori.apply(
#    lambda row: long+(0.5-random())/100, axis=1)
