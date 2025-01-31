import logging
from flask import Flask, jsonify
from flask_cors import CORS  # ✅ Import CORS
from utils.twitter_fetch import fetch_crypto_tweets
from utils.summarize import summarize_text
from utils.database import save_tweet_summary

# ✅ Initialize Flask app
app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all routes

# ✅ Configure logging to track issues in terminal & save to a file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("crypto_news.log"),  # Save logs to a file
        logging.StreamHandler()  # Also print logs in terminal
    ]
)

@app.route('/crypto-news', methods=['GET'])
def crypto_news():
    logging.info(" Endpoint /crypto-news hit!")

    # Step 1: Fetch tweets
    try:
        tweets = fetch_crypto_tweets()
        if not tweets:
            logging.warning(" No tweets fetched.")
            return jsonify({"warning": "No tweets available"}), 200

        logging.info(f" Fetched {len(tweets)} tweets.")

    except Exception as e:
        logging.error(f" Error fetching tweets: {e}")
        return jsonify({"error": "Failed to fetch tweets"}), 500

    summaries = []

    # Step 2: Process each tweet
    for i, t in enumerate(tweets):
        try:
            summary = summarize_text(t["text"])
            logging.info(f" {i+1}/{len(tweets)} Summarized: {summary}")

            summaries.append({"tweet": t["text"], "summary": summary})

            # ✅ Print tweet & summary for immediate verification
            print(f"\n🔹 Original Tweet: {t['text']}")
            print(f"✏️ Summarized: {summary}")

            # Step 3: Save to Firebase
            try:
                save_tweet_summary(t["text"], summary)
                logging.info(f" Saved to Firebase: {t['text'][:50]}...")
            except Exception as e:
                logging.error(f" Firebase save failed: {e}")

        except Exception as e:
            logging.error(f" Error summarizing tweet {i+1}: {e}")

    # ✅ Save to log file for later review
    with open("summarized_tweets.log", "a", encoding="utf-8") as log_file:
        for item in summaries:
            log_file.write(f"\n Tweet: {item['tweet']}\n")
            log_file.write(f" Summary: {item['summary']}\n")
            log_file.write("-" * 50 + "\n")

    logging.info(" Returning summarized tweets!")
    return jsonify(summaries)

if __name__ == "__main__":
    app.run(debug=True)
