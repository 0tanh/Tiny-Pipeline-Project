import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import NameAdder from './own_components/NameAdder'
import OtherAPICall from './own_components/OtherAPICall'


function App() {

  return (
    <>
    <div>
      <NameAdder prod={true}/>
    </div>
      
    <div>
      <OtherAPICall host="" path="hw" whatIDo="Hello World"/>
    </div>
    
    <div>
      <OtherAPICall host="" path="lastName" whatIDo="LastName"/>
    </div>

      
    </>
  )
}

export default App
