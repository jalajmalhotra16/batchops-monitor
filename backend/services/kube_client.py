import logging

from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


logging.basicConfig(level=logging.INFO)


class KubernetesClient:
    """
    Factory class for creating Kubernetes API clients.

    The configuration is loaded only when an API client is requested,
    allowing the Flask application to start even if the Kubernetes
    cluster is temporarily unavailable.
    """
    _config_loaded = False


    @classmethod
    def _load_config(cls):
        """
        Load Kubernetes configuration.

        Priority:
        1. In-cluster configuration (when running inside Kubernetes)
        2. Local kubeconfig (when running locally)
        """
        if cls._config_loaded:
            return
        try:
            config.load_incluster_config()
            logging.info("Loaded in-cluster Kubernetes configuration")

        except ConfigException:
            config.load_kube_config()
            logging.info("Loaded local kubeconfig")
        cls._config_loaded= True

    @classmethod
    def batch(cls):
        """
        Returns BatchV1Api client.
        """
        cls._load_config()
        return client.BatchV1Api()

    @classmethod
    def core(cls):
        """
        Returns CoreV1Api client.
        """
        cls._load_config()
        return client.CoreV1Api()


kube_client = KubernetesClient()