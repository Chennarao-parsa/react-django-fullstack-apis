import { useEffect,useState,useRef } from "react";
import { useParams} from "react-router-dom";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import '../css/UpdateEmployee.css';
function UpdateEmployee(){
    let { empno }=useParams();
    let [data,setData]=useState();
    let empnoRef=useRef();
    let enameRef=useRef();
    let esalRef=useRef();
    let navigate=useNavigate();
    useEffect(()=>{
        let p_url;
        p_url='http://127.0.0.1:8000/apis/modifyemployeesapi/'+empno+'/';
        axios.get(p_url).then((resp)=>{
            console.log(resp);
            //setData(resp.data);
            empnoRef.current.value=resp.data.empno;
            enameRef.current.value=resp.data.ename;
            esalRef.current.value=resp.data.salary;
        }).catch((err)=>{
            console.log(err);
        })
    },[])
   
    let updateData = ()=>{
        let upd_url,input_data;
        upd_url='http://127.0.0.1:8000/apis/modifyemployeesapi/'+empno+'/';
        input_data={
            "empno":empnoRef.current.value,
            "ename":enameRef.current.value,
            "salary":esalRef.current.value,
            "dept":null,
           "profile_pic":null,
           "video":null

        }
        axios.put(upd_url,input_data).then((resp)=>{
            console.log(resp);
            navigate('/view');


        })

    }
    return (
        <div className="updateemployee">
            <label htmlFor="">
                Employee no
                <input ref={empnoRef} type="text"  />
            </label>
            <br>
            </br>
            <br></br>
            <label htmlFor="">
                Employee name
                <input ref={enameRef} type="text" />
            </label>
            <br>
            </br>
            <br></br>
            <label htmlFor="">
                Employee salary
                <input ref={esalRef} type="text" />
            </label>
            <br>
            </br>
            <br></br>
            <button onClick={updateData}>Update</button>

           
        </div>
    );

}
export default UpdateEmployee;