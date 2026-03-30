import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './css/App.css'
import Header from './Components/Header';
import SideBar from './Components/SideBar';
import Mainpage from './Components/Mainpage';
import Footer from './Components/Footer';
import { BrowserRouter } from 'react-router-dom';
import { createContext } from 'react';
export const mycontext = createContext();
function App() {
  let [isLoggedin,setIsLoggedin]=useState(false);
  return (
    <div className='app'>  
    <BrowserRouter>
    <mycontext.Provider value={[isLoggedin,setIsLoggedin]}>
    <Header />
    <SideBar/>
    <Mainpage/>
    <Footer/>
    </mycontext.Provider>
    </BrowserRouter>  
    </div>
  )
}
export default App;
