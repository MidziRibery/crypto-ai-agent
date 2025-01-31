import React, { useState, useEffect } from "react";
import TweetCard from "./TweetCard";

const Dashboard = () => {
  const [tweets, setTweets] = useState([]); // Store fetched tweets
  const [loading, setLoading] = useState(true); // Loading state

  useEffect(() => {
    const fetchTweets = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/crypto-news");
        const data = await response.json();
        setTweets(data);
      } catch (error) {
        console.error("Error fetching tweets:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchTweets();
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold text-gray-800">
        📊 AI-Summarized Crypto News
      </h2>

      {loading ? (
        <p className="text-gray-500">⏳ Loading tweets...</p>
      ) : (
        tweets.map((t, index) => (
          <TweetCard key={index} tweet={t.tweet} summary={t.summary} />
        ))
      )}
    </div>
  );
};

export default Dashboard;
