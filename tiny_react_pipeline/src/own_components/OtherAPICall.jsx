import React, {useState} from "react"

export default function OtherAPICall({path, whatIDo}){
    const [data,setData]=useState({});
    
    const handleSubmit = () => {
        console.log("I'm bein' pressed I am")
        const p = `http://127.0.0.1:8000/${path}`
        console.log(p)
        fetch(p)
        .then(
            (response)=>{
                console.log("Response being parsed")
                return response.json();
            })
        .then((data)=>{
            const r = JSON.stringify(data);
            alert(r);
            })
    }
    
    return (
        <>
        <button
        onClick={handleSubmit}
        >{whatIDo}</button>
        </>
    )
}