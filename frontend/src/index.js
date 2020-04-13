import React from 'react';
import ReactDOM from 'react-dom';
import AOS from 'aos';

import './index.css';
import App from './App';
import 'aos/dist/aos.css'; // You can also use <link> for styles

ReactDOM.render(<App />, document.getElementById('root'));
AOS.init();
