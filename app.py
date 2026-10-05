from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <h1>Tandory Downloader</h1>
    <p>Servidor funcionando correctamente.</p>
    """

@app.post("/test")
def test():
    data = request.get_json(silent=True) or {}
    return jsonify({
        "ok": True,
        "url": data.get("url", "")
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
