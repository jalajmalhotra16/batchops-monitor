import time
import sys
from kubernetes import client, config
from datetime import datetime, timezone, timedelta


def read_cron_jobs(namespace="default"):
    try:
        config.load_incluster_config()
    except config.ConfigException:
        config.load_kube_config()

    batch_api= client.BatchV1Api()
    cronjobs = batch_api.list_namespaced_cron_job(namespace)
    for cj in cronjobs.items:
        print({
            "name": cj.metadata.name,
            "namespace": cj.metadata.namespace,
            "schedule": cj.spec.schedule,
            "suspend": cj.spec.suspend,
            "concurrency_policy": cj.spec.concurrency_policy,
            "successful_history": cj.spec.successful_jobs_history_limit,
            "failed_history": cj.spec.failed_jobs_history_limit,
            "last_schedule_time": cj.status.last_schedule_time
        })


read_cron_jobs()

    
    
