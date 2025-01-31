import openai
import sys
from config import OPENAI_API_KEY
from services.market_data import get_crypto_prices, get_glassnode_data


def summarize_text(text):
    """Summarizes tweets & includes real-time market data in context."""
    prices = get_crypto_prices()  # Fetch real-time BTC & ADA prices
    whale_data = get_glassnode_data()  # Fetch whale transaction data

    # Debug: Print market data
    print(f"🔹 Market Prices: BTC=${prices['BTC']}, ADA=${prices['ADA']}")
    if whale_data:
        print(f"🐋 Whale Transaction: {whale_data} BTC")
    # Build market context for AI
    market_context = f"Current Market: BTC=${prices['BTC']}, ADA=${prices['ADA']}."
    if whale_data:
        market_context += f" Latest Bitcoin Whale Transaction: {whale_data} BTC."

    # Debug: Print final AI input prompt
    print(f"📝 AI Prompt Context: {market_context}")

    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"Analyze the tweet and provide a summary. If relevant, include insights on how it relates to the current market. {market_context}"},
            {"role": "user", "content": text}
        ]
    )
    # Debug: Print AI-generated summary
    summary = response.choices[0].message.content
    print(f"✅ AI Summary Generated: {summary}")

    return summary


    # return response.choices[0].message.content
