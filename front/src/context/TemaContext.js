// src/context/TemaContext.js
import { createContext, useEffect, useState } from "react";

export const TemaContext = createContext();

export const TemaProvider = ({ children }) => {
  const [temaClaro, setTemaClaro] = useState(() => {
    return localStorage.getItem("temaClaro") === "true";
  });

  useEffect(() => {
    const root = document.documentElement;

    if (temaClaro) {
      root.classList.add("tema-claro");
      root.classList.remove("tema-oscuro");
    } else {
      root.classList.add("tema-oscuro");
      root.classList.remove("tema-claro");
    }

    localStorage.setItem("temaClaro", temaClaro);
  }, [temaClaro]);

  return (
    <TemaContext.Provider value={{ temaClaro, setTemaClaro }}>
      {children}
    </TemaContext.Provider>
  );
};
