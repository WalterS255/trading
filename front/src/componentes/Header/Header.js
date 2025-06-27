import './Header.css';
import user from '../images/user.png';
import useIsMobile from '../../hooks/useIsMobile';
import { useState } from 'react';
import { useLocation } from 'react-router-dom';

export default function Header({ titulo }) {
  const [sidebarAbierto, setSidebarAbierto] = useState(false);
  const isMobile = useIsMobile();

  // Función que alterna el estado de visibilidad del sidebar
  const toggleSidebar = () => {
    const sidebar = document.querySelector('.sidebar');
    sidebar?.classList.toggle('mostrar'); // Agrega o quita la clase que despliega el menú
  };

  return (
    <div className="Header">
      {isMobile ? (
        <>
          {/* Menú + Notificación + Avatar agrupados */}
          <div className="HeaderTopRow">
            <button className="HeaderMenuButton" onClick={toggleSidebar}>
              ☰ MENÚ
            </button>

            <a href="#" className="HeaderNotification">
              <span className="notification-icon">🔔</span>
            </a>

            <img src={user} alt="User Avatar" className="HeaderAvatar" />
          </div>

          {/* Título y búsqueda debajo */}
          <h1 className="HeaderTitle">{titulo}</h1>
          <div className="HeaderSearch">
            <input type="text" placeholder="Buscar..." />
          </div>
        </>
      ) : (
        <>
          <button className="HeaderMenuButton" onClick={toggleSidebar}>
            ☰ MENÚ
          </button>

          <h1 className="HeaderTitle">{titulo}</h1>

          <div className="HeaderSearch">
            <input type="text" placeholder="Buscar..." />
          </div>

          <a href="#" className="HeaderNotification">
            <span className="notification-icon">🔔</span>
          </a>

          <img src={user} alt="User Avatar" className="HeaderAvatar" />
        </>
      )}
    </div>
  );
}
