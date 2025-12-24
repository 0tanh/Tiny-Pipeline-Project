import { useState, useEffect } from "react"

export default function NameAdder(){
    const validUserName = '\w{5,10}';
    
    const [name, setName] = useState('WOWO');
    
    const handleChange = ({target}) => {setName(target.value)

    }
    
    const handleSubmit= (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);
        console.log(formData)
        fetch('http://127.0.0.1:8000/new_name',{
            method:'POST',
            body:formData
        })
        .then((response)=>{
            response.json();
            alert(response);
        
        }, alert('Womp Womp Fetch failed'))
        
        .then((result)=>{
            setName(result)
            alert(`CONGRATS YOU HAVE RECEIVED
                ${JSON.stringify(result)}`)}
      )
    }

    return (
        <>
          <form onSubmit={handleSubmit}>
            <input 
            id="nameInputBox"
            className="nameInputBox"
            type='text' 
            value={name}
            onChange={handleChange}/>
            <button type="submit">add username</button>
        </form>
        </>
    )
}