important_keywords = [
    "Bitcoin", "Cardano", "BTC", "ADA", "bullish", "bearish", "whale", "dump", 
    "pump", "market", "FUD", "SEC", "regulation"
]

def is_important_tweet(tweet_text):
    """Keeps only tweets with market insights."""
    return any(word in tweet_text for word in important_keywords)
