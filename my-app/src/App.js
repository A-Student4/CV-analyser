import React from 'react';
import ChatPage from './cv-tool/ChatPage';
import {BrowserRouter as Router, Routes, Route, Navigate} from 'react-router-dom';


import { Hero } from './landing-page/Hero'; 
import { Features } from './landing-page/Features';
import { Cta } from './landing-page/CTA';

const LandingPage = () => {
    return (
      <div className="landing-root min-h-screen bg-white">
        <Hero />
        <Features />
        <Cta />
      </div>
    );
}


function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          {/* Route for the Landing Page */}
          <Route path="/" element={<LandingPage />} />
          
          {/* Route for the CV Tool */}
          <Route path="/app" element={<ChatPage />} />
          
          {/* Catch-all redirect */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;