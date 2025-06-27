// src/App.js
import './App.css';
import './index.css'; // Asegúrate de importar tus variables y clases de tema
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Panel from './features/Panel/Panel';
import AsesorFinanciero from './features/AsesorFinanciero/AsesorFinanciero';
import Transacciones from './features/Transacciones/Transacciones';
import Ajustes from './features/Ajustes/Ajustes';
import Login from './features/Log-in/Login';
import { useEffect } from 'react';

function App() {
  // Aplicar tema al cargar la app
  useEffect(() => {
    const temaClaro = localStorage.getItem('temaClaro') === 'true';
    const root = document.documentElement;

    if (temaClaro) {
      root.classList.add("tema-claro");
      root.classList.remove("tema-oscuro");
    } else {
      root.classList.add("tema-oscuro");
      root.classList.remove("tema-claro");
    }
  }, []);

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/panel" element={<Panel />} />
          <Route path="/asesor-financiero" element={<AsesorFinanciero />} />
          <Route path="/transacciones" element={<Transacciones />} />
          <Route path="/ajustes" element={<Ajustes />} />
          <Route path="/" element={<Login />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
