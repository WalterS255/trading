import './TarjetaPortafolio.css';

export default function TarjetaPortafolio({ icono, empresa, valor, total, diferencia }) {
  const diferenciaEsNegativa = diferencia.toString().includes('-');

  return (
    <div className="TarjetaPortafolio">
      {/* Ícono */}
      <div className="FirstRow">
        <img className="IconoTarjeta" src={icono} alt={`${empresa} logo`} />
      </div>

      {/* Empresa + Total */}
      <div className="SecondRow">
        <p className="empresa">{empresa}</p>
        <p className="total">{total}</p>
      </div>

      {/* Valor + Diferencia */}
      <div className="ThirdRow">
        <p className="valor">{valor}</p>
        <p className={`diferencia ${diferenciaEsNegativa ? 'rojo' : 'verde'}`}>
          {diferencia}
        </p>
      </div>
    </div>
  );
}
/*
[
  {
    "icono": "/images/meta.png",
    "empresa": "META",
    "total": "$3,245.03",
    "valor": "$52,243 USD",
    "diferencia": "-13.40%"
  },
*/