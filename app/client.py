import requests

# response = requests.get('http://127.0.0.1:5000/advertisements/1',
#                          # json={"title": "adv_1", "description": "Sale books", "owner": "user_1"},
#                          )
# print(response.status_code)
# print(response.text)


# response = requests.patch('http://127.0.0.1:5000/advertisements/1',
#                          json={"description": "Sale good books"},
#                          )
# print(response.status_code)
# print(response.text)

# response = requests.post('http://127.0.0.1:5000/advertisements',
#                          json={"title": "adv_3", "description": "Sale good books3", "owner": "user_3"},
#                          )
# print(response.status_code)
# print(response.text)

response = requests.delete('http://127.0.0.1:5000/advertisements/3')
print(response.status_code)
print(response.text)

response = requests.get('http://127.0.0.1:5000/advertisements/3',
                         # json={"title": "adv_1", "description": "Sale books", "owner": "user_1"},
                         )
print(response.status_code)
print(response.text)
