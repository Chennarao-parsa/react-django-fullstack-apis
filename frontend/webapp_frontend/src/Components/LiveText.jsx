import '../css/LiveText.css' ;
import { useState } from 'react';
function LiveText(){
    let [data,setData]=useState('');
    let readdata=(event)=>{
        setData(event.target.value);
        
    }
    return(
    <div className="LiveText">
        <input type="text" onChange={readdata}/>
        <p> {data}</p>
    </div>
    );
} 
export default LiveText;