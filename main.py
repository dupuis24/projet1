import requests


response = requests.post("https://creator.zoho.com/api/clarencedupuis/xml/gestion/form/event/record/add", data =
{"authtoken":"cbe4f73a6fe66ac0396a5b04941e62dd",
 "scope":"creatorapi",
 "Champs1":'bobby1'})

print(response)