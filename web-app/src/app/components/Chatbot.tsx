'use client'

import React, { useState } from 'react';
import axios from 'axios';

const Chatbot = () => {
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([{
    sender: '',
    text: ''
  }]);

  const handleSend = async () => {
    if (!message.trim()) return;

    // Add user message to the chat history
    setChatHistory([...chatHistory, { sender: 'user', text: message }]);

    try {
      // Send user message to Flask API
      const response = await axios.post('http://localhost:5000/bot', {
        message: message
      });

      // Add chatbot's reply to the chat history
      setChatHistory([...chatHistory, { sender: 'user', text: message }, { sender: 'bot', text: response.data.reply }]);
    } catch (error) {
      console.error('Error:', error);
    }

    setMessage('');
  };

  return (
    <div>
      <div style={{ border: '1px solid #ccc', padding: '10px', height: '400px', overflowY: 'scroll' }}>
        {chatHistory.map((chat, index) => (
          <div key={index} style={{ marginBottom: '10px' }}>
            <strong>{chat.sender === 'user' ? 'You: ' : 'Bot: '}</strong>
            <span>{chat.text}</span>
          </div>
        ))}
      </div>
      <div style={{ marginTop: '10px' }}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;
