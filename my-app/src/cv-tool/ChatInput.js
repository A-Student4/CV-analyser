// In src/ChatInput.js

import React, { useState } from 'react';
import { IoPaperPlaneOutline } from 'react-icons/io5';

const ChatInput = ({ onSendMessage, disabled }) => {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!inputValue.trim()) return; // Don't send empty messages

    // Call the function passed down from the parent component
    onSendMessage(inputValue);

    // Clear the input field after sending
    setInputValue('');
  };

  return (
    <footer className="input-area">
      <form className="chat-input-form" onSubmit={handleSubmit}>
        <textarea
          placeholder="Message..."
          className="input-field"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={(e) => {
            // Send message on Enter key, but allow new lines with Shift+Enter
            if (e.key === 'Enter' && !e.shiftKey) {
              e.preventDefault();
              handleSubmit(e);
            }
          }}
          disabled={disabled} // Disable input while the AI is responding
        />
        <button type="submit" className="send-button" disabled={disabled}>
          <IoPaperPlaneOutline size={24} />
        </button>
      </form>
    </footer>
  );
};

export default ChatInput;