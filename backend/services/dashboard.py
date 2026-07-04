from backend.services.cronjobs import cronjob_service
from backend.services.jobs import job_service
from backend.services.pods import pod_service


class DashboardService:

    def __init__(self):
        pass

    def get_dashboard(self, namespace="default"):

        cronjobs = cronjob_service.get_all(namespace)
        jobs = job_service.get_all(namespace)
        pods = pod_service.get_all(namespace)

        #
        # Build Job Lookup
        #
        jobs_by_cronjob = {}

        for job in jobs:

            cronjob_name = job["cronJob"]

            if cronjob_name is None:
                continue

            jobs_by_cronjob.setdefault(cronjob_name, []).append(job)

        #
        # Sort Jobs (Newest First)
        #
        for cronjob_name in jobs_by_cronjob:

            jobs_by_cronjob[cronjob_name].sort(
                key=lambda x: x["startTime"] or "",
                reverse=True
            )

        #
        # Build Pod Lookup
        #
        pods_by_job = {}

        for pod in pods:

            if pod["jobName"] is None:
                continue

            pods_by_job[pod["jobName"]] = pod

        #
        # Build Dashboard
        #
        dashboard = []

        for cronjob in cronjobs:

            latest_job = None
            latest_pod = None

            cronjob_jobs = jobs_by_cronjob.get(
                cronjob["name"],
                []
            )

            if cronjob_jobs:
                latest_job = cronjob_jobs[0]

                latest_pod = pods_by_job.get(
                    latest_job["jobName"]
                )

            dashboard.append({

                "cronJob": cronjob["name"],

                "namespace": cronjob["namespace"],

                "schedule": cronjob["schedule"],

                "lastScheduleTime": cronjob["lastScheduleTime"],

                "suspend": cronjob["suspend"],

                "lastExecution": latest_job,

                "pod": latest_pod

            })

        return dashboard


dashboard_service = DashboardService()