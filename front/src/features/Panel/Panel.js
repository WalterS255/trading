import { useEffect, useState } from "react";
import Sidebar from "../../componentes/SideBar/Sidebar";
import AccionesCard from "./Acciones/AccionesCard";
import CreditCard from "../../componentes/CreditCard/CreditCard";
import Grafico from "./Grafico/Grafico";
import Header from "../../componentes/Header/Header";
import MercadoenVivo from "./MercadoenVivo/MercadoenVivo";
import Portafolio from "./Portafolio/Portafolio";
import './Panel.css';

export default function Panel() {
  const [acciones, setAcciones] = useState([]);
    const [mercado, setMercado] = useState([]);
    const [portafolio, setPortafolio] = useState([]);


 useEffect(() => {
  const obtenerDatos = async () => {
    try {
      const resAcciones = await fetch("http://localhost:8000/api/acciones/");
      if (!resAcciones.ok) throw new Error("Error al cargar acciones");
      const dataAcciones = await resAcciones.json();
      setAcciones(dataAcciones);

      const resMercado = await fetch("http://localhost:8000/api/mercado"); // Si tienes este endpoint en Django
      if (!resMercado.ok) throw new Error("Error al cargar mercado");
      const dataMercado = await resMercado.json();
      setMercado(dataMercado);

      const resPortafolio = await fetch("http://localhost:8000/api/portafolio"); // Si tienes este endpoint en Django
      if (!resPortafolio.ok) throw new Error("Error al cargar portafolio");
      const dataPortafolio = await resPortafolio.json();
      setPortafolio(dataPortafolio);
    } catch (error) {
      console.error("Fallo en la carga de datos:", error.message);
    }
  };

  obtenerDatos();
}, []);



  return (
    <div>
        <div className="PanelGeneral">
        <div className="PanelSidebar">
            <Sidebar />
        </div>
        <div className="PanelContent">
            <Header titulo="Panel de control" />
            <div className="PanelAcciones">
                {acciones.map((accion) => (  // <- Posible mapeo del json de acciones (Asumiendo que el json llega como un array de varias acciones) SE DEBE TRAER DIRECTAMENTE DESDE LA API
                    <AccionesCard
                        key={accion.id}
                        icono={accion.icono} 
                        titulo={accion.titulo}
                        empresa={accion.empresa}
                        valor={accion.valor}
                        diferencia={accion.diferencia}
                    />
                ))}
            </div>
            </div>
            <div className="PanelMiddle">
            <div className="PanelCreditCard">
                <CreditCard compania="Visa" numero="1234 5678 9012 3456" propietario="John Doe" /> {/*Todavia no se a hecho la logica de la tarjeta*/}
            </div>
            <div className="PanelGrafico">
                <Grafico />
            </div>
            </div>
            <div className="PanelBottom">
            <div className="PanelMercado">
                {mercado.map((accion, index) => ( // <- SE DEBE TRAER DIRECTAMENTE DESDE LA API
                    <MercadoenVivo
                    key={index}
                    icono={accion.icono}
                    ticker={accion.ticker}
                    cambio={accion.cambio}
                    mercado={accion.mercado}
                    volumen24h={accion.volumen24h}
                    precio={accion.precio}
                    />
                ))}
            </div>
            <div className="PanelPortafolio"> 
                <Portafolio portafolio={portafolio} /> {/* <La logica de atrapar los datos esta dentro del componente portafolio*/}
            </div>
            </div>
        </div>
    </div>
  );
}
