import random

def fake_file():
    return random.choice([
        "passwords.txt",
        "bank_data.csv",
        "admin_credentials.json"
    ])

def fake_creds():
    return {
        "username": "admin",
        "password": "pass" + str(random.randint(1000,9999))
    }