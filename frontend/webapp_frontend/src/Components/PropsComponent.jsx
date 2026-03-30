import '../css/PropsComponent.css';
function PropsComponent({name,age}){
    return(
        <div className="propscomponent">
            
                <p>{name} </p>
                <p>{age}</p>
        
        </div>
    );
}
export default PropsComponent;