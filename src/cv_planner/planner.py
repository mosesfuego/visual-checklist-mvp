from typing import List
from cv_planner.job import CVJob


def plan_jobs(contract: dict) -> List[CVJob]:
    jobs = []

    for obj in contract["objects"]:
        job = CVJob(
            object_name=obj["name"],
            expected_count=obj["expected_count"],
            attributes=obj["attributes"],
            region_of_interest=contract["verification"]["region_of_interest"],
            min_confidence=contract["confidence"]["minimum_confidence"],
            critical=obj["critical"]
        )
        jobs.append(job)

    return jobs
