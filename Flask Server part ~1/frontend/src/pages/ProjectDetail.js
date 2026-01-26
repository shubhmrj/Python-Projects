import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';

export default function ProjectDetail() {
  const { id } = useParams();
  const [project, setProject] = useState(null);
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/');
      return;
    }
    axios.get(`http://localhost:8000/project/${id}`, { headers: { Authorization: `Bearer ${token}` } })
      .then(res => setProject(res.data))
      .catch(() => navigate('/projects'));
  }, [id, navigate]);

  const handleRun = async () => {
    setOutput('');
    setError('');
    const token = localStorage.getItem('token');
    try {
      const res = await axios.post(`http://localhost:8000/run/${id}`, {}, { headers: { Authorization: `Bearer ${token}` } });
      setOutput(res.data.stdout);
      setError(res.data.stderr);
    } catch {
      setError('Failed to run project');
    }
  };

  if (!project) return null;

  return (
    <div style={{ maxWidth: 800, margin: 'auto', marginTop: 40 }}>
      <h2>{project.name}</h2>
      <p>{project.description}</p>
      <h4>Code:</h4>
      <pre style={{ background: '#f5f5f5', padding: 12, borderRadius: 6, maxHeight: 300, overflow: 'auto' }}>{project.code}</pre>
      <button onClick={handleRun}>Run Project</button>
      <h4>Output:</h4>
      <pre style={{ background: '#222', color: '#fff', padding: 12, borderRadius: 6, minHeight: 60 }}>{output}{error && `\nError: ${error}`}</pre>
      <button onClick={() => navigate('/projects')} style={{ marginTop: 16 }}>Back to Projects</button>
    </div>
  );
}
