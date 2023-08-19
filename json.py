import json

path = 'company.json'

with open(path, 'r') as jsf:
    company = json.load(jsf)
new_employee = {
    'id': 'E003',
    'name': 'Avraham Stern',
    'position': 'Janitor'
}

company['employees'].append(new_employee)


with open(path, 'w') as jsf:
    json.dump(company, jsf)