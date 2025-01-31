import React from "react";

const TweetCard = ({ tweet, summary }) => {
  return (
    <div className="bg-white shadow-md rounded-lg p-4 my-4">
      <p className="text-gray-700 font-semibold">📢 {tweet}</p>
      <p className="text-blue-600 mt-2">🔍 {summary}</p>
    </div>
  );
};

export default TweetCard;
