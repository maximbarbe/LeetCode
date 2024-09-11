import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    bonuses = list(map(lambda el:el*2, employees.salary))
    employees.insert(loc=2,column="bonus", value=bonuses)
    return employees