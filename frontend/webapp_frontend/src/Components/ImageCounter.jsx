import chenna from '../assets/Chenna_2.jpg'
import '../css/ImageCounter.css';
import { useEffect,useState } from 'react';
function ImageCounter(){
    let [data,setData]=useState('');
    useEffect(()=>{
            console.log('component mounted');
            return ()=>{
                console.log('component Unmounted')

            }
    },[data]);

    return(
        <div  className='imagecounter'>
            <img src={chenna} alt="" />
            <input type='text' onChange={(event)=>setData(event.target.value)} />
        </div>
    );
}
export default ImageCounter;