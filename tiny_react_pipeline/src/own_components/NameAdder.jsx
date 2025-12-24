import { useState, useEffect } from "react"
import axios from "axios";

export default function NameAdder(){
    const validUserName = '\\w{5,10}';
    
    const [name, setName] = useState('WOWO');
    
    const handleChange=()=> {setName(name)}

    const handleSubmit= async (event) => {
        event.preventDefault();
        const data = {
            "name": name
        }
        
        try {
            console.log(data);
            let i;
            const response = await axios.post("http://127.0.0.1:8000/new_name",data)
            
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