import TransaccionesTarjetas from "./TransaccionesTarjetas/TransaccionesTarjetas"
import Sidebar from "../../componentes/SideBar/Sidebar";
import Header from "../../componentes/Header/Header";
import './Transacciones.css';
export default function Transacciones() {
    return(
        <div className="Transacciones">
        <div className="TransaccionesSidebar">
            <Sidebar />
        </div>
        <div className="TransaccionesContent">
            <Header titulo="Transacciones" />
            <div className="TransaccionesHistorial">
                <div className="TransaccionesTitulo">
                    <p>Movimiento</p>
                    <p>Fecha/Hora</p>
                    <p>Cantidad</p>
                    <p>Comisión</p>
                    <p>Método de pago</p>
                </div>
                <TransaccionesTarjetas  
                Movimiento="Compra Acción"
                Fecha="Ene 29, 2025"
                Hora="8:00 AM"
                Cantidad="$15,850"
                Comision="$1.2"
                MetodoPago="Tarjeta de Crédito" />
                <TransaccionesTarjetas  
                Movimiento="Compra Acción"
                Fecha="May 29, 2025"
                Hora="8:00 AM"
                Cantidad="$1,585"
                Comision="$1"
                MetodoPago="Tarjeta de Crédito" />
                <TransaccionesTarjetas  
                Movimiento="Venta"
                Fecha="Feb 29, 2025"
                Hora="8:00 AM"
                Cantidad="$15,850"
                Comision="$1.2"
                MetodoPago="Cuenta Bancaria" />
                
            </div>
        </div>   

    </div>

    );
    
}