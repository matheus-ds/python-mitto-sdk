"""
Updating an existing job credentials in Mitto instance.
"""
import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")

JOB_TYPE = "io"
INPUT_USE = "sfdc.iov2#SalesforceInput"
INPUT_CREDS = "Salesforse - aziz.abibulaiev@zuar.com"


def main(BASE_URL, API_KEY, INPUT_CREDS):  # pylint: disable=R1710
    """updating job credentials"""
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    jobs = mitto.get_jobs(job_type=JOB_TYPE)
    for job in jobs:
        job = mitto.get_job(job["id"])
        conf = job["conf"]

        # update conf
        if conf.get("input") and conf.get("input").get("use") == INPUT_USE:
            conf["input"]["credentials"] = str(INPUT_CREDS)
            job["conf"] = conf
            update_crd = mitto.update_job_conf(job_id=job["id"], job_conf=job)
            return update_crd


if __name__ == "__main__":
    sys.exit(main(BASE_URL, API_KEY, INPUT_CREDS))
