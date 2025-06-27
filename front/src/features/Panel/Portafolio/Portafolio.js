import TarjetaPortafolio from "./TarjetasPortafolio/TarjetaPortafolio";
import './Portafolio.css';

export default function Portafolio({ portafolio }) {
  return (
    <div className="portafolio-container">
      <h1>Mi Portafolio</h1>
      {portafolio.map((item, index) => ( // <-LOS DATOS DEL PORTAFOLIO DEBEN VENIR DE LA BASE DE  DATOS
        <TarjetaPortafolio
          key={index}
          icono={item.icono}
          empresa={item.empresa}
          valor={item.valor}
          diferencia={item.diferencia}
          total={item.total}
        />
      ))}
    </div>
  );
}

/*[
  {
    "icono": "/images/google.png",
    "empresa": "Google",
    "valor": 324503,
    "diferencia": -13.40,
    "total": 52244
  },
  ...
]
  */