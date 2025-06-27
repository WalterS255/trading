import './MercadoenVivo.css';
import google from '../../../componentes/images/google.png'
export default function MercadoenVivo() {
    return (
        <div className="mercado-container">
        <div className="mercado-header">
            <h2>Mercado en Vivo</h2>
            <button className="ver-mas">Ver Más</button>
        </div>

        <div className="mercado-titulos">
            <span>Acción</span>
            <span>Cambio</span>
            <span>Mercado</span>
            <span>24h Volumen</span>
            <span>Precio</span>
        </div>

        <div className="mercado-dato">
            <div className="mercado-accion">
            <img src={google} alt="GOOGL" />
            <span>GOOGL</span>
            </div>
            <span className="positivo">+12.00%</span>
            <span>$3.560M</span>
            <span>$65.20M</span>
            <span>$48,032.32</span>
            <span className="menu-icon">⋯</span>
        </div>
        </div>
  );
}
/*
  [
  {
    "icono": "/images/google.png",
    "ticker": "GOOGL",
    "cambio": "+12.00%",
    "mercado": "$3.560M",
    "volumen24h": "$65.20M",
    "precio": "$48,032.32"
  },
  */