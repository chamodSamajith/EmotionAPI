from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Flask API is running 1."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))  # Use Azure-assigned port
    app.run(debug=True, host="0.0.0.0", port=port)
