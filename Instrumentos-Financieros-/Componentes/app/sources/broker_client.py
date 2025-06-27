import os
from datetime import datetime, date, timezone
from dotenv import load_dotenv
import requests
import base64

from app.schemas import UserRequest, orderRequest, activityRequest
load_dotenv()

class BrokerClient:
    def __init__(self):
        self.BROKER_API_KEY = os.getenv("BROKER_API_KEY")
        self.BROKER_SECRET_KEY =os.getenv("BROKER_SECRET_KEY")

        user_pass = f"{self.BROKER_API_KEY}:{self.BROKER_SECRET_KEY}"
        # Codificar en bytes
        user_pass_bytes = user_pass.encode("utf-8")

        # Codificar en Base64
        base64_bytes = base64.b64encode(user_pass_bytes)

        # Convertir a string legible
        base64_string = base64_bytes.decode("utf-8")

        authorization = "Basic " + base64_string

        self.headers = {
            "accept": "application/json",
            "authorization": authorization
        }
    '''
    Ejemplo creación usuarios
    {
        "nombre": "Luis",
        "apellido": "Diaz",
        "numero_telefono": "324567891",
        "direccion": "Cra99A Sur",
        "email": "lucho99@gmail.com",
        "ciudad": "Bogotá",
        "codigo_postal": "110711",
        "fecha_nacimiento": "1994-04-07",
        "cedula": "1025603032",
        "fuente_ingresos": "employment_income",
        "nombre_contacto_confianza": "Marta",
        "apellido_contacto_confianza": "Diaz",
        "email_contacto_confianza": "martu@gmail.com",
        "numero_telefono_contacto_confianza": "3192687334",
        "direccion_contacto_confianza": "Cra99A Sur",
        "ciudad_contacto_confianza": "Bogotá",
        "codigo_postal_contacto_confianza": "110711",
        "tipo_cuenta": "trading",
        "documento_codificado_base_64": "/9j/Cg=="
    } 
    '''
    def create_user(self, payload: UserRequest, ip):
        usuario = {
          "contact": {
              "email_address": payload.email,
              "phone_number": payload.numero_telefono,
              "street_address": [payload.direccion],
              "city": payload.ciudad,
              "country": "COL",
              "postal_code": payload.codigo_postal
          },
          "identity": {
              "tax_id_type": "COL_NIT",
              "given_name": payload.nombre,
              "family_name": payload.apellido,
              "date_of_birth": payload.fecha_nacimiento,
              "tax_id": payload.cedula,
              "country_of_tax_residence": "COL",
              "funding_source": [payload.fuente_ingresos] # employment_income, investments, inheritance, business_income, savings, family.
          },
          "disclosures": {
              "is_control_person": False,
              "is_affiliated_exchange_or_finra": False,
              "is_politically_exposed": False,
              "immediate_family_exposed": False
          },
          "trusted_contact": {
            "given_name": payload.nombre_contacto_confianza,
            "family_name": payload.apellido_contacto_confianza,
            "email_address": payload.email_contacto_confianza,
            "phone_number": payload.numero_telefono_contacto_confianza,
            "street_address": [payload.direccion_contacto_confianza],
            "state": payload.departamento_contacto_confianza,
            "city": payload.ciudad_contacto_confianza,
            "postal_code": payload.codigo_postal_contacto_confianza,
            "country": "COL"
          },
          "account_type": payload.tipo_cuenta,
          "agreements": [
              {
                "agreement": "margin_agreement",
                "signed_at": datetime.now(timezone.utc).isoformat(timespec='seconds'),
                "ip_address": ip
              },
              {
                "agreement": "account_agreement",
                "signed_at": datetime.now(timezone.utc).isoformat(timespec='seconds'),
                "ip_address": ip
              },
              {
                "agreement": "customer_agreement",
                "signed_at": datetime.now(timezone.utc).isoformat(timespec='seconds'),
                "ip_address": ip
              }
          ],
          "documents": [
              {
                "document_type": "identity_verification",
                "content": payload.documento_codificado_base_64, #Documento codificado en base_64
                "mime_type": "image/jpeg"
              }
          ]
        }
        # return usuario
        url = "https://broker-api.sandbox.alpaca.markets/v1/accounts"
        
        response = requests.post(url, headers=self.headers, json=usuario)

        if response.status_code == 201:
            print(response.json())
            return "Cuenta creada exitosamente."
                    
        elif response.status_code == 403:
            print(response.json())
            return "Acceso denegado (403 Forbidden): revisa tus claves o el entorno."
        else:
            print(f"Error {response.status_code}:")            
            return response 

    def create_order(self, payload: orderRequest):
        '''
        {
            "account_id": "27421671-1296-4415-9f99-115acf4ecd7d",
            "symbol": "AAPL",
            "qty": "3",
            "side": "buy",
            "type": "market",
            "time_in_force": "day"
        }
        '''
        url = f"https://broker-api.sandbox.alpaca.markets/v1/trading/accounts/{payload.account_id}/orders"        

        if payload.limit_price is not None and payload.stop_price is not None:
            return "Error: No puede poner limit price y stop price al tiempo"
        else:
            order = payload.model_dump(exclude_none = True)
            order.pop("account_id", None)
                
            response = requests.post(url, json=order, headers=self.headers)
            return response
        
    def view_user_trading_activity(self, payload: activityRequest):
        '''
        {
            "account_id": "27421671-1296-4415-9f99-115acf4ecd7d",
            "category": "trade_activity"
        }
        '''
        url = f"https://broker-api.sandbox.alpaca.markets/v1/accounts/activities?account_id={payload.account_id}&category={payload.category}&page_size=100"
        # url = "https://broker-api.sandbox.alpaca.markets/v1/accounts/activities?account_id=27421671-1296-4415-9f99-115acf4ecd7d&category=trade_activity&page_size=100"

        response = requests.get(url, headers=self.headers)
        return response