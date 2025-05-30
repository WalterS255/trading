from datetime import datetime

def transform_funding_data(raw_data):
    transformed = []
    for item in raw_data:
        transformed.append({
            "id": item.get("id"),
            "amount": float(item.get("amount", 0)),
            "date": parse_date(item.get("date")),
            "type": item.get("activity_type"),
        })
    return transformed

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        return None
def transform_order_data(raw_data):
    transformed = []
    for item in raw_data:
        transformed.append({
            "id": item.get("id"),
            "symbol": item.get("symbol"),
            "qty": int(item.get("qty", 0)),
            "side": item.get("side"),
            "type": item.get("type"),
            "status": item.get("status"),
            "created_at": parse_date(item.get("created_at")),
        })
    return transformed

# app/services/transformer.py

def transform_stock_data(raw):
    return {
        "titulo": raw.get("symbol", "N/A"),
        "empresa": raw.get("name", "Empresa desconocida"),
        "valor": f"${raw.get('price', 0):,.2f}",
        "diferencia": f"{raw.get('change_percent', 0):+.2f}%",
        "icono": f"https://yourcdn.com/icons/{raw.get('symbol', '').lower()}.png"
    }
