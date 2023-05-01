from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8")as file:
        dictionary_list = csv.DictReader(file)
        new_list = []
        for row in dictionary_list:
            new_list.append(row)
        return list(new_list)


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    unique_jobs = set()
    for job in jobs:
        unique_jobs.add(job["job_type"])
    return unique_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    new_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            new_list.append(job)
    return new_list
