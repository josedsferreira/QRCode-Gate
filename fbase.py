import firebase_admin
from firebase_admin import credentials, db
import random
import string
import time

# Initialize Firebase app (replace with your Firebase project credentials)
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-id.firebaseio.com'
})

# Function to generate a random authorization code
def generate_code(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to update authorization codes in Firebase
def update_codes():
    # Generate new authorization codes
    new_codes = [generate_code() for _ in range(5)]  # Generate 5 new codes
    
    # Update authorization codes in Firebase
    ref = db.reference('authorization_codes')
    ref.set(new_codes)

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
