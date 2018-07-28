import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App.jsx';
import registerServiceWorker from './registerServiceWorker';
import route from './routes.js'

ReactDOM.render(route, document.getElementById('root'));
registerServiceWorker();
