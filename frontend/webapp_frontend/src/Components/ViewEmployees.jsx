import {  useEffect,useRef,useState } from "react";
import axios from "axios";
import EmpCard from "./EmpCard";
import "../css/ViewEmployees.css";
import { useContext } from "react";
import { mycontext } from "../App";
import { useNavigate } from "react-router-dom";
function ViewEmployees(){
    let [isLoggedin,setIsLoggedin]=useContext(mycontext);
    let [data,setData] = useState([]);
    let nexturl = useRef();
    let prevurl= useRef();
    let navigate=useNavigate();
    useEffect(()=>{
      let get_url;
      if(isLoggedin==false)
        navigate('/')
      get_url='http://127.0.0.1:8000/apis/getemployeesapi/'
      axios.get(get_url,{
        "headers":{
          "Authorization":"Bearer "+localStorage.getItem('token')
        }
      }).then(
        (resp)=>{
          console.log(resp)
          nexturl.current=resp.data.next;
          prevurl.current=resp.data.previous;
          setData(resp.data.results);
        }
      ).catch((err)=>{
        console.log(err);
      });
    },[])
    let getdata = (url)=>{
      axios.get(url,{
        "headers":{
          "Authorization":"Bearer "+localStorage.getItem('token')
        }
        }).then((resp)=>{
        console.log(resp)
        nexturl.current=resp.data.next;
        prevurl.current=resp.data.previous;
        setData(resp.data.results)
      })
    }
    return(
        <div className="viewemployees">
          <div className="empdata">
               
           {
            data.map((obj)=>{
              return <EmpCard
                    empno={obj.empno}
                    ename={obj.ename}
                    esal={obj.salary}
                    img_url={obj.profile_pic}
                    video_url={obj.video}
                  /> })
          }
          </div>
          <div className="navigationbar" >
            <button onClick={()=>getdata(prevurl.current)} disabled={prevurl.current==null}>Previous</button>
            <button onClick={()=>getdata(nexturl.current)} disabled={nexturl.current==null}>Next</button>

          </div>

       
        </div>
    );

}
export default ViewEmployees;