# Define spammy words to filter out
blacklist_keywords = ["giveaway", "airdrops", "double your money", "100x", "low cap gem", "pump", "shill", "moon", "ponzi"]
important_keywords = ["Bitcoin", "Ethereum", "BTC", "ETH", "bullish", "bearish", "whale", "dump", "pump", "market", "FUD", "SEC", "regulation"]

def is_valid_tweet(tweet_text):
    """Removes scam tweets based on blacklist words."""
    return not any(word in tweet_text.lower() for word in blacklist_keywords)

def is_important_tweet(tweet_text):
    """Keeps only tweets with market insights."""
    return any(word in tweet_text for word in important_keywords)
