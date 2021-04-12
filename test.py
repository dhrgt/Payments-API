import requests

BASE = "http://127.0.0.1:5000/"
response = requests.post(BASE + "customer/", {
    "name": "Dhruv",
    "address": "5511 Caspian Falls Ln",
    "phone": "3467581150",
    "email": "dhruvg06@gmail.com",
    "description": "Dhruvs details"
})
print(response)
