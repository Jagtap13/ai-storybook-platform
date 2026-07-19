import { useState } from 'react'
import { Route,Routes } from 'react-router-dom'
import Login from './pages/login'
import Dashboard from './pages/dashboard'
import Register from './pages/register'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Routes>
      <Route path="/login" element={<Login/>}></Route>
      <Route path="/register" element={<Register/>}></Route>
      <Route path="/dashboard" element={<Dashboard/>}></Route>
    </Routes>
    </>
  )
}
export default App
