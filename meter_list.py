from google.cloud import firestore
import pandas as pd

contatori = pd.read_csv("dataset/contatori.csv", sep=",")

db = firestore.Client.from_service_account_json('credentials.json')
for item, row in contatori.iterrows():
    db.collection("lista contatori").document(str(int(row.n_serie))).set({
        "lat": str(row.lat), "long": str(row.long)
    })
