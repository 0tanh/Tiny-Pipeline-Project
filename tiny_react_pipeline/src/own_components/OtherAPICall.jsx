import React, {useState} from "react"
import axios from "axios";

export default function OtherAPICall({host, path, whatIDo}){
    const [data,setData]=useState({});
    
    const handleSubmit = () => {
        console.log("I'm bein' pressed I am")
        const p = `${host}/${path}`
        console.log(p)
        fetch(p)
        .then(
            (response)=>{
                console.log("Response being parsed")
                return response.json();
            })
        .then((data)=>{
            const r = JSON.stringify(data);
            console.log(r)
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