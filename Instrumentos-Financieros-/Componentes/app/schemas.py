from pydantic import BaseModel
from typing import Optional

class activityRequest(BaseModel):
    account_id: str
    category: str

class orderRequest(BaseModel):
    account_id: str
    symbol: str
    qty: str
    side: str
    type: str
    time_in_force: str
    limit_price: Optional[str] = None
    stop_price: Optional[str] = None

class UserRequest(BaseModel):
    nombre: str
    apellido: str
    numero_telefono: str
    direccion: str
    email: str
    ciudad: str
    codigo_postal: str
    fecha_nacimiento: str
    cedula: str
    fuente_ingresos: str
    nombre_contacto_confianza: str
    apellido_contacto_confianza: str
    email_contacto_confianza: str
    numero_telefono_contacto_confianza: str
    direccion_contacto_confianza: str
    departamento_contacto_confianza: str
    ciudad_contacto_confianza: str
    codigo_postal_contacto_confianza: str
    tipo_cuenta: str
    documento_codificado_base_64: str