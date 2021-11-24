import requests

r = requests.get('http://127.0.0.1:5000/employee/riho', data={'name': 'riho'})
print(r.text)

r = requests.post('http://127.0.0.1:5000/employee', data={'name': 'riho'})
print(r.text)

r = requests.put('http://127.0.0.1:5000/employee', data={
    'name': 'riho', 'new_name': 'riwa'})
print(r.text)

r = requests.delete('http://127.0.0.1:5000/employee', data={'name': 'riho'})
print(r.text)