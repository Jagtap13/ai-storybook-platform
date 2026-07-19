import { useState } from "react"
import { useNavigate, Link } from "react-router-dom"
import api from "../api/axios"


function Register() {
    const [username,setUsername] = useState('')
    const [email,setEmail] = useState('')
    const [password,setPassword] = useState('')
    const [role,setRole] = useState('student')
    const [error,setError] = useState('')
    const navigate = useNavigate('')

    const handlesubmit = async (e) => {
        e.preventDefault();
        setError("");
    
    try {
      await api.post("/auth/register/", {
        username,
        email,
        password,
        role,
      });
      navigate("/login");
    } catch (err) {
      setError("Registration failed. Try a different username.");
    }
  };

    return (
        <>
        <div className="min-h-screen flex items-center justify-center">
            <form action="" onSubmit={handlesubmit} 
            className="bg-white p-8 shadow-md rounded-lg w-80">
                <h1 className="text-2xl font-bold mb-6 bg-black">
                    Register
                </h1>
                {error && <p className="text-red-500 text-sm mb-4">{error}</p>}

                <input 
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)} 
                className="w-full border rounded px-3 py-2 mb-4"/>
                
                <input 
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)} 
                className="w-full border rounded px-3 py-2 mb-4"/>
                
                <input 
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)} 
                className="w-full border rounded px-3 py-2 mb-4"/>

                <select name="" id=""
                value={role}
                onChange={(e)=>{setRole(e.target.value)}}
                className ="w-full rouunded border px-3 py-2 mb-4"
                >
                    <option value="student">Student</option>
                    <option value="parent">Parent/Teacher</option>

                </select>
                <button
                type="submit"
                className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700">
                    Register
                </button>
                <p
                className="text-sm mt-4 text-center">
                    Already have an account?{" "}
                    <Link to="/login" className="text-blue-600" >
                    Login
                    </Link>
                </p>
            </form>
        </div>
        </>
    )
}
export default Register