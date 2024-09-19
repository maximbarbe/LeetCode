import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    conversion = {'m': 'f', 'f': 'm'}
    salary['sex'] = salary['sex'].map(conversion)
    return salary