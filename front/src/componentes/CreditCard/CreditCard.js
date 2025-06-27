import './CreditCard.css';
export default function CreditCard({ compania, numero, propietario }) {
    return (
        <div className="CreditCard">
            
                <div className="TextoIzq">
                    <p className='title'>Tarjeta de crédito</p>
                    <p className='number'>{numero}</p>
                    <p className='propiertario'>{propietario}</p>
                </div>
                <div className="TextoDer">
                    <p>{compania}</p>
                </div>
            </div>
        
    );
}