
import '../css/Counter.css';
import {useState} from 'react';
function Counter(){
    let [cnt,setCnt]=useState(0)
    let increament = ()=>{
        setCnt(cnt+1);

    }
    let decreament = ()=>{
        setCnt(cnt-1)
    }
    return(
        <div className="counter">
            <button onClick={increament}>+</button>
            <p>{cnt}</p>
            <button onClick={decreament}>
                -
            </button>
        </div>
    )
}
export default Counter;