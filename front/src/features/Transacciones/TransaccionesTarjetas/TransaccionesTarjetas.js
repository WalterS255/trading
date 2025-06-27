import './TransaccionesTarjetas.css';
import { Triangle } from 'lucide-react'
export default function TransaccionesTarjetas({Movimiento, Fecha, Hora, Cantidad, Comision, MetodoPago}) {
    return (
        <div className="TransaccionesTarjetas">
            <div className='Movimiento'>
                <Triangle className="IconoMovimiento" size={18} />
                <p className="MovimientoTexto">{Movimiento}</p>
            </div>
            <div className="FechaHora">
                <p className="Fecha">{Fecha}</p>
                <p className="Hora">{Hora}</p>
            </div>
            <p className="Cantidad">{Cantidad}</p>
            <p className="Comision">{Comision}</p>
            <p className="MetododePago">{MetodoPago}</p>
        </div>
    );
}
