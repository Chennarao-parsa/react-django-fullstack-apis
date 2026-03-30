import '../css/ToDoList.css';
import { useRef,useState } from 'react';

function ToDolist(){
    let inputRef= useRef();
    let [items,setItems]=useState([]);
    let readdata = ()=>{
        setItems([...items,inputRef.current.value]);
        
        console.log(items);
    
    }
    let removeitem=(idx)=>{
        let new_items=items.filter((t,id)=>id != idx)
        setItems(new_items);

    }
    return(
        <div className="todolist">
            <input ref={inputRef} type="text" id="t1"/>
            <button onClick={readdata}>Add</button>
            <ol>
                {
                    items.map((it,idx)=>{
                        return <> <li key={it+idx}>{it}</li> <button onClick={()=>removeitem(idx)}>X</button> <br></br></> 
                    })
                }
            </ol>
    
        </div>
    );
}
export default ToDolist;