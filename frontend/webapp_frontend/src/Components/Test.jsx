function Test(){
    /*
    let name1='raju';
    let name2="siva";
    */
   //let names=['raju','siva','anu','venkat','krishna']
    let students=[
        {
            name:"raju",
            age:"36",
            gender:"Male"
        },
            {
            name:"siva",
            age:"37",
            gender:"Male"
        },
            {
            name:"anu",
            age:"34",
            gender:"FeMale"
        },
    ]
    return(
        <div className="test">
            {
            students.map((obj)=>{
                return <h1>{obj.name} - {obj.age} - {obj.gender}</h1>
            })
        }

        </div>
    );
}
export default Test;