import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import AOS from 'aos';

import './index.css';
import App from './App';
import 'aos/dist/aos.css'; // You can also use <link> for styles

axios.defaults.baseURL = 'http://127.0.0.1:8000';

ReactDOM.render(<App />, document.getElementById('root'));
AOS.init();
