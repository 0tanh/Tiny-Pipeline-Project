import { useState, useEffect } from "react"
import axios from "axios";

export default function NameAdder({prod}){
    const validUserName = '\\w{5,10}';
    
    const [name, setName] = useState('put in a username');

    const handleSubmit= async (event) => {
        event.preventDefault();
        const data = {
            "name": name
        }
        const host_url = prod?"https://tiny-pipeline-project.onrender.com":"http://127.0.0.1"
        try {
            console.log(data);
            const response = await axios.post(`${host_url}/new_name`,data)
            alert(response.data)
        
        } catch (error) {
            console.error("Error", error)
        }
        }

    return (
        <>
          <form onSubmit={handleSubmit}>
            <input 
            
            id="nameInputBox"
            className="nameInputBox"
            type='text' 
            onChange={(e)=>{setName(e.target.value)}}
            value={name}/>
            
            <button type="submit">add username</button>
        </form>
        </>
    )
}