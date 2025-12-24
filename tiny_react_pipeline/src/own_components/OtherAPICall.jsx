import React, {useState} from "react"

export default function OtherAPICall(){
    const [data,setData]=useState({});
    
    const handleSubmit = () => {
        alert("I'm bein' pressed I am")
        
        fetch("http://127.0.0.1:8000/lastName")
        .then(
            (response)=>{
                r = JSON.stringify(response.json);
                alert(r)
            })
    }
    
    return (
        <>
        <button
        onClick={handleSubmit}
        >Press Me to Test An API Call</button>
        </>
    )
}