import React, { useState } from 'react';
import './Login.css';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [code, setCode] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Datos:', { email, password, code });
  };

  return (
    <div className="login-container">
      <form className="login-form" onSubmit={handleSubmit}>
        <h2>Iniciar Sesión</h2>

        <label htmlFor="email">Correo Electrónico</label>
        <input
          type="email"
          id="email"
          placeholder="pedro@example.com"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <label htmlFor="password">Contraseña</label>
        <input
          type="password"
          id="password"
          placeholder="••••••••"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Continuar</button>
        <p className="hint">Se ha enviado un código a tu correo electrónico</p>
      </form>
    </div>
  );
}
