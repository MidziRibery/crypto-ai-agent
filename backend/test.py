import tweepy
from config import (
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET
)

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    user = api.verify_credentials()
    if user:
        print(f"✅ Authentication successful! Logged in as {user.screen_name}")
    else:
        print("❌ Authentication failed.")
except tweepy.Unauthorized:
    print("❌ ERROR: Twitter API authentication failed. Check your API keys and tokens!")
