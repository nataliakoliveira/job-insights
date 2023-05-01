from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
        salary = read(path)
        unique_salary = set()
        for job in salary:
            salary_type = job.get("max_salary")
            if salary_type != "" and salary_type.isdigit():
                unique_salary.add(int(salary_type))
        return max(unique_salary)


def get_min_salary(path: str) -> int:
        salary = read(path)
        unique_salary = set()
        for job in salary:
            salary_type = job.get("min_salary")
            if salary_type != "" and salary_type.isdigit():
                unique_salary.add(int(salary_type))
        return min(unique_salary)

def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
