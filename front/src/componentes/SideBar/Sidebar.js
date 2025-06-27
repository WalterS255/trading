import './Sidebar.css';
import { useLocation } from 'react-router-dom'; // Hook para obtener la ruta actual
import {
  LayoutGrid,
  User,
  CreditCard,
  Briefcase,
  MessageCircle,
  Settings,
  LogOut
} from 'lucide-react';

export default function Sidebar() {
  const { pathname } = useLocation(); // Extrae la ruta actual

  // Función para marcar como activa la opción del menú correspondiente a la ruta actual
  const isActive = (ruta) => pathname === ruta ? 'active' : '';

  return (
    <div className="sidebar">
      {/* Menú principal */}
      <div className="sidebar-menu">
        <a href="/panel" className={isActive("/panel")}><LayoutGrid size={18} /> Panel</a>
        <a href="/asesor-financiero" className={isActive("/asesor-financiero")}><User size={18} /> Asesor Financiero</a>
        <a href="/comprar-vender" className={isActive("/comprar-vender")}><CreditCard size={18} /> Comprar / Vender</a>
        <a href="/transacciones" className={isActive("/transacciones")}><Briefcase size={18} /> Transacciones</a>
        <a href="/mercados" className={isActive("/mercados")}><MessageCircle size={18} /> Mercados</a>
      </div>

      {/* Pie de menú */}
      <div className="sidebar-footer">
        <a href="/ajustes" className={isActive("/ajustes")}><Settings size={18} /> Configuración</a>
        <a href="#"><LogOut size={18} /> Salir</a>
      </div>
    </div>
  );
}
