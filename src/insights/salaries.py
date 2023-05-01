from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    salary = read(path)
    unique_salary = set()
    for max_val in salary:
        salary_type = max_val.get("max_salary")
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
    if ('min_salary' not in job or 'max_salary' not in job):
        raise ValueError
    if (type(salary) != int and type(salary) != str):
        raise ValueError
    if (type(job['min_salary']) != int or type(job['max_salary']) != int):
        raise ValueError
    if (job['min_salary'] > job['max_salary']):
        raise ValueError

    return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])


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
