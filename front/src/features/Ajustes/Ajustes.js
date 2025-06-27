import { useContext } from "react";
import { TemaContext } from "../../context/TemaContext";
import Sidebar from "../../componentes/SideBar/Sidebar";
import Header from "../../componentes/Header/Header";
import "./Ajustes.css";

export default function Ajustes() {
  const { temaClaro, setTemaClaro } = useContext(TemaContext);

  return (
    <div className="ajustes-layout">
      <Sidebar />
      <div className="ajustes-contenido">
        <Header titulo="Ajustes" />

        <div className="ajustes-switch">
          <label className="switch">
            <input
              type="checkbox"
              checked={temaClaro}
              onChange={() => setTemaClaro(!temaClaro)}
            />
            <span className="slider" />
          </label>
          <p>Modo {temaClaro ? "Claro" : "Oscuro"}</p>
        </div>
      </div>
    </div>
  );
}

