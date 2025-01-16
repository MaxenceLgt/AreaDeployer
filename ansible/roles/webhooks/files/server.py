import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/deploy', methods=['POST'])
def webhook():
    event = request.headers.get("X-GitHub-Event")
    if event == "ping":
        return jsonify({"status": "Success", "message": "Ping Sucess!"}), 200
    if event != "push":
        return jsonify({"status": "Error", "message": "Invalid request!"}), 400
    payload = request.json
    repository = payload.get("repository", {})
    if payload.get("ref", "") != "refs/heads/main" or repository.get("full_name", "") != "mlargeot/Area":
        return jsonify({"status": "Error", "message": "Invalid request!"}), 400
    try:
        command = [
            "ansible-pull",
            "-v",
            "-U", "https://github.com/MaxenceLgt/AreaDeployer",
            "-C", "main",
            "-d", "/tmp/ansible",
            "-i", "ansible/pull/production.yml",
            "ansible/pull/app.yml"
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return jsonify({
                "status": "Success",
                "message": "Ansible Pull executed successfully!",
                "output": result.stdout
            }), 200
        else:
            return jsonify({
                "status": "Error",
                "message": "Ansible Pull failed!",
                "error": result.stderr
            }), 500
    except Exception as e:
        return jsonify({
            "status": "Error",
            "message": "Unexpected Error!",
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run()
