import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './HomePage';
import SignIn from './SignIn';
import SignUp from './SignUp';

// Inside your Routes component:


function App() {
  return (
    <Router>
        <Routes>
        <Route exact path="/" element={<SignIn />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/signup" element={<SignUp />} />

        </Routes>
    </Router>
  );
}

export default App;
