import { useState, useEffect } from "react"

export default function NameAdder(){
    const [name, setName] = useState({});
    
    const handleSubmit= (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);

        fetch('http://127.0.0.1:8000/new_name',{
            method:'POST',
            body:formData
        })
        .then((response)=>response.json())
        .then((result)=>{
            setName(result)
            alert(`CONGRATS YOU HAVE RECEIVED
                ${JSON.stringify(result)}`)}
      )
    }

    return (
        <>
          <label className="nameInput"/>
          <form onSubmit={handleSubmit}>
            <input className="nameInputBox"
            type='text' 
            value={name} 
            onInput={handleChange}/>
            <button type="submit">submit</button>
        </form>
        </>
    )
}