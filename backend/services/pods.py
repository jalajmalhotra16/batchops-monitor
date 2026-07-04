from backend.services.kube_client import kube_client


class PodService:

    def __init__(self):
        #self.core_api = kube_client.core_api
        pass
    @property
    def core_api(self):
        return kube_client.core()

    def get_all(self, namespace="default"):

        pods = self.core_api.list_namespaced_pod(namespace)

        response = []

        for pod in pods.items:

            job_name = None

            if pod.metadata.owner_references:

                for owner in pod.metadata.owner_references:

                    if owner.kind == "Job":
                        job_name = owner.name
                        break

            response.append({

                "podName": pod.metadata.name,

                "jobName": job_name,

                "namespace": pod.metadata.namespace,

                "phase": pod.status.phase,

                "node": pod.spec.node_name,

                "podIP": pod.status.pod_ip,

                "hostIP": pod.status.host_ip,

                "startTime": (
                    pod.status.start_time.isoformat()
                    if pod.status.start_time
                    else None
                )
            })

        return response


pod_service = PodService()