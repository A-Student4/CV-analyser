// In src/Message.js

import React from 'react';
// We'll use icons from the 'react-icons' library. Make sure it's installed: npm install react-icons
import { FaUserCircle, FaRobot } from 'react-icons/fa';

const Message = ({ message }) => {
  const { sender, text } = message;
  const isUser = sender === 'user';

  // Conditionally apply a CSS class based on the sender
  const messageClass = isUser ? 'user-message' : 'ai-message';


  return (
    <div className={`message-container ${messageClass}`}>
      <div className="icon-container">
        {/* Conditionally render the icon based on the sender */}
        {isUser ? <FaUserCircle /> : <FaRobot />}
      </div>
      <div className="text-container">
        <p>{text}</p>
      </div>
    </div>
  );
};

export default Message;