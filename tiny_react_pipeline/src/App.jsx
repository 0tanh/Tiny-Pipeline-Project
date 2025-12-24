import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import NameAdder from './own_components/NameAdder'
import OtherAPICall from './own_components/OtherAPICall'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <div>
      <NameAdder />
    </div>
      
    <div>
      <OtherAPICall />
    </div>
      
    </>
  )
}

export default App
