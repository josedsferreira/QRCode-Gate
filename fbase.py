import firebase_admin
from firebase_admin import credentials, db
import random
import string
import time

# Firebase
cred = credentials.Certificate('qr-code-gate-firebase-adminsdk-ndxh2-efe8148abf.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://qr-code-gate-default-rtdb.europe-west1.firebasedatabase.app/'
})

def generate_code(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def update_code():
    new_code = generate_code()
    ref = db.reference('Gate Code/Code')
    ref.set(new_code)
    print("Updated Gate Code to:", new_code)

# Function to check if the scanned QR code is authorized
def is_authorized(scanned_code):
    ref = db.reference('authorization_codes')
    authorized_codes = ref.get()
    if scanned_code in authorized_codes:
        return True
    else:
        return False

""" if __name__ == "__main__":
    # Run a loop to periodically update authorization codes (e.g., every hour)
    while True:
        update_codes()
        time.sleep(3600)  # Wait for an hour before updating again """

update_code()
