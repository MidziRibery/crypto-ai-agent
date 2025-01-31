import tweepy
import time
from config import (
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_BEARER_TOKEN,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET
)
from utils.filters import is_valid_tweet, is_important_tweet  # Import Spam & Market Filtering

# ✅ Correct Authentication Setup for Tweepy v1.1 (Handles Rate Limits)
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# ✅ Tweepy v2 for Fetching Tweets
client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def fetch_crypto_tweets(max_results=10):
    """
    Fetches latest crypto-related tweets with a focus on BTC & ADA.
    Filters out scams, shills, and irrelevant content.
    """
    query = """
    (crypto OR bitcoin OR cardano OR ADA OR defi OR blockchain OR market) 
    -is:retweet lang:en 
    (from:balajis OR from:ErikVoorhees OR from:aantonop OR from:CamiRusso OR from:CathieDWood 
    OR from:saylor OR from:100trillionUSD OR from:WClementeIII OR from:CryptoCobain 
    OR from:IOHK_Charles OR from:CardanoCF OR from:CardanoLive)
    """

    try:
        # Fetch tweets
        tweets = client.search_recent_tweets(query=query, max_results=max_results)

        # ✅ Apply Spam & Market Filtering
        filtered_tweets = [
            {"text": tweet.text, "author_id": tweet.author_id}
            for tweet in tweets.data if is_valid_tweet(tweet.text) and is_important_tweet(tweet.text)
        ]

        print(f"✅ Retrieved {len(filtered_tweets)} quality tweets.")
        return filtered_tweets

    except tweepy.TooManyRequests as e:
        reset_time = int(e.response.headers.get("x-rate-limit-reset", time.time() + 60))
        wait_time = max(reset_time - time.time(), 60)
        print(f"🚨 Rate limit hit! Waiting {int(wait_time)} seconds before retrying...")
        time.sleep(wait_time)
        return fetch_crypto_tweets()

    except tweepy.Unauthorized:
        print("❌ ERROR: Twitter API authentication failed. Check API keys!")
        return []


    except tweepy.TooManyRequests as e:
        reset_time = int(e.response.headers.get("x-rate-limit-reset", time.time() + 60))
        wait_time = max(reset_time - time.time(), 60)
        print(f"🚨 Rate limit hit! Waiting {int(wait_time)} seconds before retrying...")
        time.sleep(wait_time)
        return fetch_crypto_tweets()

    except Exception as e:
        print(f"⚠ ERROR: {e}")
        return []
