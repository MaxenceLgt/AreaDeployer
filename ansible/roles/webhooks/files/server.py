import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/deploy', methods=['POST'])
def webhook():
    return "sucess", 200

if __name__ == "__main__":
    app.run()
