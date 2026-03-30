import {Link} from 'react-router-dom';

function SideBar(){
    return(
        <div className="SideBar">
            <ul>
                <li>Home</li>
                <li><Link to="/view">View</Link></li>
                <li><Link to="/add">Add</Link></li>
                <li><Link to="/update">Update</Link></li>
                <li>Delete</li>
            </ul>
        </div>
    );
}
export default SideBar;