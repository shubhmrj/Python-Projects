import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';

export default function Signup() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8000/signup', { username, password });
      setSuccess('Account created! You can now log in.');
      setTimeout(() => navigate('/'), 1200);
    } catch (err) {
      setError('Signup failed');
    }
  };

  return (
    <div style={{ maxWidth: 350, margin: 'auto', marginTop: 80 }}>
      <h2>Sign Up</h2>
      <form onSubmit={handleSignup}>
        <input type="text" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} required /><br />
        <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} required /><br />
        <button type="submit">Sign Up</button>
      </form>
      {error && <div style={{ color: 'red', marginTop: 8 }}>{error}</div>}
      {success && <div style={{ color: 'green', marginTop: 8 }}>{success}</div>}
      <div style={{ marginTop: 16 }}>
        Already have an account? <Link to="/">Login</Link>
      </div>
    </div>
  );
}
