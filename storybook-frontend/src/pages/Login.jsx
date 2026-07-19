import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handlesubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const response = await api.post("/auth/login/", {
        username,
        password,
      });
      localStorage.setItem("refresh", response.data.access);
      localStorage.setItem("refresh", response.data.access);
      navigate("/dashboard");
    } catch (err) {
      setError("Invalid username or password");
    }
  };
  return (
      <>
    <div className="min-h-screen flex items-center justify-center bg-slate-100">
      <form
        onSubmit={handlesubmit}
        className="bg-white p-8 rounded-lg shadow-md w-80"
        >
        <h1 className="text-2xl font-bold mb-6">Login</h1>
        {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          />
        <input
          type="password"
          placeholder="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          />

        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
          >
          Login
        </button>
      </form>
    </div>
  </>
);

}
export default Login;
