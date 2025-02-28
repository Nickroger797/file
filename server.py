from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Get PORT from environment, default to 8080
    app.run(host="0.0.0.0", port=port)  # Run on 0.0.0.0 to accept external connections
