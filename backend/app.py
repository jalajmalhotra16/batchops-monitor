from flask import Flask, jsonify
import logging

from backend.services.cronjobs import cronjob_service
from backend.services.jobs import job_service
from backend.services.pods import pod_service
from backend.services.dashboard import dashboard_service
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    origins=["http://localhost:5173","http://localhost:8080","http://batchops.local:8080","http://batchops.local"]
)

logging.basicConfig(level=logging.INFO)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "application": "BatchOps",
        "message": "Batch Operations Monitoring Platform"
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP"
    }), 200


@app.route("/version", methods=["GET"])
def version():
    return jsonify({
        "application": "BatchOps",
        "version": "1.0.0",
        "environment": "local"
    }), 200


@app.route("/cronjobs", methods=["GET"])
def get_cronjobs():

    try:
        cronjobs = cronjob_service.get_all()
        return jsonify(cronjobs), 200

    except Exception as e:
        logging.exception(e)
        return jsonify({"error": str(e)}), 500


@app.route("/jobs", methods=["GET"])
def get_jobs():

    try:
        jobs = job_service.get_all()
        return jsonify(jobs), 200

    except Exception as e:
        logging.exception(e)
        return jsonify({"error": str(e)}), 500


@app.route("/pods", methods=["GET"])
def get_pods():

    try:
        pods = pod_service.get_all()
        return jsonify(pods), 200

    except Exception as e:
        logging.exception(e)
        return jsonify({"error": str(e)}), 500


@app.route("/dashboard", methods=["GET"])
def get_dashboard():

    try:
        dashboard = dashboard_service.get_dashboard()
        return jsonify(dashboard), 200

    except Exception as e:
        logging.exception(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )