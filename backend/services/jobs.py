from backend.services.kube_client import kube_client


class JobService:

    def __init__(self):
        pass

    @property
    def batch_api(self):
        return kube_client.batch()

    def get_all(self, namespace="default"):
        """
        Returns all Jobs in a namespace.
        """

        jobs = self.batch_api.list_namespaced_job(namespace)

        response = []

        for job in jobs.items:

            cronjob_name = None

            if job.metadata.owner_references:
                for owner in job.metadata.owner_references:
                    if owner.kind == "CronJob":
                        cronjob_name = owner.name
                        break

            duration = None

            if job.status.start_time and job.status.completion_time:
                duration = (
                    job.status.completion_time -
                    job.status.start_time
                ).total_seconds()

            status = "Unknown"

            if job.status.active:
                status = "Running"

            elif job.status.succeeded:
                status = "Succeeded"

            elif job.status.failed:
                status = "Failed"

            response.append({
                "jobName": job.metadata.name,
                "cronJob": cronjob_name,
                "namespace": job.metadata.namespace,
                "status": status,
                "startTime": (
                    job.status.start_time.isoformat()
                    if job.status.start_time
                    else None
                ),
                "completionTime": (
                    job.status.completion_time.isoformat()
                    if job.status.completion_time
                    else None
                ),
                "durationSeconds": duration,
                "active": job.status.active,
                "succeeded": job.status.succeeded,
                "failed": job.status.failed
            })

        return response


job_service = JobService()