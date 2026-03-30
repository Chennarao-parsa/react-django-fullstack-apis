import axios from 'axios';
import '../css/PostEmployee.css';
import {useEffect, useRef} from 'react';
import { useContext } from 'react';
import { mycontext } from '../App';
import { useNavigate } from 'react-router-dom';
function PostEmployee(){
    let [isLoggedin,setIsLoggedin]=useContext(mycontext);
    let empnoRef=useRef();
    let empnameRef=useRef();
    let empsalaryRef=useRef();
    let empdeptRef=useRef();
    let emppicRef=useRef();
    let empvideoRef=useRef();
    let navigate=useNavigate();
    useEffect(()=>{
        if(isLoggedin==false)
            navigate('/');

    },[]);
    let senddata=()=>{
        let input_data,post_url;
        input_data={
            "empno":empnoRef.current.value,
            "ename":empnameRef.current.value,
            "salary":empsalaryRef.current.value,
            "dept":empdeptRef.current.value,
            "profile_pic":emppicRef.current.files[0],
            "video":empvideoRef.current.files[0]

        }
        post_url="http://127.0.0.1:8000/apis/getemployeesapi/";
        axios.post(post_url,input_data,{
            "headers":{
                "Content-Type":"multipart/form-data"
            }
        }).then((resp)=>{
            console.log(resp);


        }).catch((err)=>{
            console.log(err);
        })

    }
    return(
        <div>
        <div className="postemployee">
            <div className="left">
                <label htmlFor="">
                    Employee No
                    <input ref={empnoRef} type="number"/>
                </label><br /> <br />
                <label htmlFor="">
                    Employee Name
                    <input ref={empnameRef} type="text"/>
                </label><br /> <br />
                  <label htmlFor="">
                    Employee salary
                    <input ref={empsalaryRef} type="number"/>
                </label><br /> <br />
            </div>
            <div className="right">
                 <label htmlFor="">
                    Employee Dept
                    <input ref={empdeptRef} type="number"/>
                </label><br /> <br />
                 <label htmlFor="">
                    Employee picture
                    <input ref={emppicRef} type="file"/>
                </label><br /> <br />
                 <label htmlFor="">
                    Employee video
                    <input ref={empvideoRef} type="file"/>
                </label><br /> <br />
            </div>
        </div>
        <button onClick={senddata}>POST</button>
        </div>
    );
}
export default PostEmployee;