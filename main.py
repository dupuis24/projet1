import requests


print(open("requete.xml","r"))
response = requests.post("https://creator.zoho.com/api/670083415/xml/gestion/form/event/record/add",open("requete.xml","r"))
print(response.text)
