import React, { useState } from 'react';

import Navbar from "./NavBar";
import Home from './Home';                    //pages
import Image_Upload from './image_upload';    //more page
import './App.css';


import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

function App() {

  return (
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/image_upload" element={<Image_Upload />} />
        </Routes>
      </Router>
  );

}

export default App;
