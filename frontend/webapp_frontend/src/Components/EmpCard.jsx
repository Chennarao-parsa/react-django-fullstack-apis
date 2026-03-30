import '../css/EmpCard.css';
import { useNavigate } from 'react-router-dom';
function EmpCard(props){
    let navigate=useNavigate();
    let callupdate = (empno)=>{
        navigate('/update/'+empno);
    }
    return(
        <div className="empcard">
            <button onClick={()=>callupdate(props.empno)}> update</button>
            {props.img_url? <img src={"http://127.0.0.1:8000"+props.img_url }alt=""/>:'' }
            <p>Empno:{props.empno}</p>
            <p>EmpName:{props.ename}</p>
            <p>Empsalary:{props.esal}</p>
            {props.video_url? <video src={"http://127.0.0.1:8000"+props.video_url} autoPlay controls></video>:''}
        </div>
    );
}
export default EmpCard;