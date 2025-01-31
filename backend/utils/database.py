import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def save_tweet_summary(tweet, summary):
    db.collection("tweets").add({"tweet": tweet, "summary": summary})
