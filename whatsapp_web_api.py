from whatsapp_web_js import Client, LocalAuth
import asyncio

# * Estado compartido
cliente = None

def iniciar_bot():
    global cliente
    from whatsapp_web_js import Client, LocalAuth
    import time

    from whatsapp_web_js import Client, LocalAuth
    from qrcode_terminal import draw

    cliente = Client(auth_strategy=LocalAuth())

    @cliente.on("qr")
    def on_qr(qr):
        draw(qr)

    @cliente.on("ready")
    def on_ready():
        print("✅ Bot WhatsApp listo")

    cliente.initialize()

def enviar_mensaje(numero, mensaje):
    try:
        if cliente:
            cliente.send_message(f"{numero}@c.us", mensaje)
            return True
        else:
            print("❌ Bot no inicializado")
            return False
    except Exception as e:
        print("❌ Error al enviar:", str(e))
        return False
