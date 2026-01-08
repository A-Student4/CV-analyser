// In src/Sidebar.js

import React from 'react';
// We'll use an icon from the react-icons library you already have
import { FaPlus } from 'react-icons/fa';

const Sidebar = () => {
  // For now, the sidebar is a static placeholder.
  // In the future, this component would receive props from ChatPage.js,
  // such as the list of past conversations and a function to start a new chat.

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <button className="new-chat-button">
          <FaPlus size={12} /> New Analysis
        </button>
      </div>
      <div className="chat-history">
        <h2>History</h2>
        <div className="history-list">
          <p className="history-placeholder">
            Your past analyses will appear here.
          </p>
          {/* In the future, we would map over chat history data and render links here */}
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;