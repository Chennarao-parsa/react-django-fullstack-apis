import '../css/EventHandling.css';
function EventHandling({name}){
        let cnt=0
        let alertmsg=(event)=>{
            
           // alert('Button is clicked');
           //console.log(event)
           //alert(event.target.innerText+ ' is clicked');
            cnt=cnt+1;
            console.log(cnt);
        }
    return(
        <div className="eventhandling">
            <button onClick={alertmsg}>{name}</button>
            <p>{cnt}</p>
        </div>
    );
} 
export default EventHandling;