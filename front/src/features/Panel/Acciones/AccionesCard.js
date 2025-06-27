

export default function MercadoenVivo({ icono, ticker, cambio, mercado, volumen24h, precio }) {
  return (
    <div className="AccionesCard">
      <div className="TextoAccionesCard">
        <img className="Icono" src={icono} alt={ticker} />
        <div>
          <h3>{ticker}</h3>
          <p>Cambio: <span className={cambio.startsWith("-") ? "negativo" : "positivo"}>{cambio}</span></p>
          <p>Mercado: {mercado}</p>
          <p>Volumen 24h: {volumen24h}</p>
          <p>Precio: {precio}</p>
        </div>
      </div>
    </div>
  );
}

/*
[
  {
    "icono": "/images/aapl.png",
    "titulo": "AAPL",
    "empresa": "Apple Inc.",
    "valor": "$52,291",
    "diferencia": "+0.25%"
  },
*/ 