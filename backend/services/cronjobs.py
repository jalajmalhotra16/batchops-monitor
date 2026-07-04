from datetime import datetime
from backend.services.kube_client import kube_client


class CronJobService:

    def __init__(self):
        #self.batch_api = kube_client.batch_api
        pass

    @property
    def batch_api(self):
        return  kube_client.batch()

    def get_all(self, namespace="default"):

        cronjobs = self.batch_api.list_namespaced_cron_job(namespace)

        response = []

        for cj in cronjobs.items:

            response.append({
                "name": cj.metadata.name,
                "namespace": cj.metadata.namespace,
                "schedule": cj.spec.schedule,
                "suspend": cj.spec.suspend,
                "concurrencyPolicy": cj.spec.concurrency_policy,
                "lastScheduleTime": (
                    cj.status.last_schedule_time.isoformat()
                    if cj.status.last_schedule_time
                    else None
                ),
                "activeJobs": len(cj.status.active or [])
            })

        return response


cronjob_service = CronJobService()