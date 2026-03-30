//import '../css/Mainpage.css';
import Test from "./Test";
import PropsComponent from "./PropsComponent";
import EventHandling from "./EventHandling";
import Counter from "./Counter";
import ImageCounter from "./ImageCounter";
import { useState } from 'react';
import ToDolist from './ToDoList';
import LiveText from './LiveText';
import ViewEmployees from './ViewEmployees';
import PostEmployee from "./PostEmployee";
import {Route,Routes} from "react-router-dom";
import UpdateEmployee from "./UpdateEmployee";
import Login from "./Login";
function Mainpage(){

    return (
        <div className="Mainpage">
            <Routes>
                <Route path="/" element={<Login />}></Route>
                <Route path='/view'  element={<ViewEmployees/>}></Route>
                <Route path='/add' element={<PostEmployee/>}></Route>
                <Route path= '/update/:empno' element={<UpdateEmployee/>}></Route>

            </Routes>
        </div>
      
    );

}
export default Mainpage;