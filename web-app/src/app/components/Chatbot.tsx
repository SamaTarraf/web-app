'use client'

import React, {useState} from 'react';
import axios from 'axios';

export default function Chatbot() {
  const [question, setQuestion] = useState('');
  const [history, setHistory] = useState([{
    role: '',
    text: ''
  }]);

  const getResponse = async () => {
    //question into history
    setHistory([...history, {role: 'user', text: question}]);

    //get response
    const response = await axios.post('http://localhost:5000/bot', {query: question});

    //response into history
    setHistory([...history, {role: 'user', text: question}, {role: 'bot', text: response.data.text}]);

    setQuestion('');

  };

  return(
      <div className="flex flex-col justify-center w-3/4 h-screen bg-slate-400 absolute left-1/2 -translate-x-1/2">
        <div className="h-5/6 grow-0 bg-slate-400 overflow-auto">  
          {history.map((message, i) => (
            <div key = {i}>
              <strong>{message.role}:</strong>
              <span>{message.text}</span>
            </div>
          ))}
        </div>
        <input type="text" onChange={(e) => setQuestion(e.target.value)} value={question} className="h-1/6 bg-slate-200 rounded-lg"/>
        <button className="h-10 w-20" onClick={getResponse}>
          Send
        </button>
      </div>
  );
};