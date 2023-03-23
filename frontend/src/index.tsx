import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Input from './Input';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  /* Div the centers content */
  <div style={{display: 'flex', justifyContent: 'center', width: '100vw'}}>
  
    <Input />

  </div>
    
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
