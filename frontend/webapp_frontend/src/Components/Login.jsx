 import '../css/Login.css';
 import axios from 'axios';
 import {useRef} from "react";
 import { useNavigate } from 'react-router-dom';
 import { useContext } from 'react';
 import { mycontext } from '../App';
 function Login(){
    let [isLoggedin,setIsLoggedin]=useContext(mycontext)
    let uname=useRef();
    let pwd=useRef();
    let navigate=useNavigate();
    let checkuser=()=>{
        let credentials,login_url;
        credentials={
            "username":uname.current.value,
            "password":pwd.current.value
        }
        console.log(credentials);
        login_url='http://127.0.0.1:8000/apis/loginapi/';
        axios.post(login_url,credentials).then((resp)=>{
            console.log("login success")
            console.log(resp.data);
            setIsLoggedin(true);
            localStorage.setItem('token',resp.data.access)
            navigate('/view');
        }).catch((err)=>{
            console.log(err);
            setIsLoggedin(false);
        })
    }
    return (
        <div  className="login">
        <label htmlFor="">
            UserName
            <input ref={uname} type="text"/>
        </label><br /><br />
        <label htmlFor="">
            Password
            <input ref={pwd} type="text"/>

        </label><br /><br />
        <input type="button" value="Login" onClick={checkuser}/>


        </div>
    );
    
 }
 export default Login;