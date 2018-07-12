import requests
import simplejson as json
from collections import namedtuple

values = {"authtoken":"cbe4f73a6fe66ac0396a5b04941e62dd",
            "scope":"creatorapi",
            "Champs1":"bobby2"}

file = {"Video":open("requete.xml")}
response = requests.post("https://creator.zoho.com/api/clarencedupuis/json/gestion/form/event/record/add" , data = values)
result = json.loads(response.text)

result1 = result["formname"]
result2 = result1[1]
result3 = result2["operation"]
result4 = result3[1]
result5 = result4["values"]
print(result5["ID"])
valuesfile = {"authtoken":"cbe4f73a6fe66ac0396a5b04941e62dd",
            "scope":"creatorapi",
            "applinkname":"gestion",
            "formname":"event",
              "fieldname":"video",
              "recordId":result5["ID"],
              "filename":"chat.mp4"}
responsefile = requests.post("https://creator.zoho.com/api/xml/fileupload/", files = file , data = valuesfile)
print(response.text)
print(responsefile.text)
