import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function ProjectList() {
  const [projects, setProjects] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/');
      return;
    }
    axios.get('http://localhost:8000/projects', { headers: { Authorization: `Bearer ${token}` } })
      .then(res => setProjects(res.data))
      .catch(() => navigate('/'));
  }, [navigate]);

  return (
    <div style={{ maxWidth: 600, margin: 'auto', marginTop: 40 }}>
      <h2>Python Projects</h2>
      <ul>
        {projects.map(p => (
          <li key={p.id} style={{ margin: '16px 0' }}>
            <b>{p.name}</b><br />
            {p.description}<br />
            <button onClick={() => navigate(`/project/${p.id}`)}>View & Run</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
