import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("../firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Write test data
doc_ref = db.collection("test").document("connection_check")
doc_ref.set({"message": "Firebase connected successfully!"})

# Read test data
doc = doc_ref.get()
print(f"🔥 Firebase Read Test: {doc.to_dict()}")
