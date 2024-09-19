import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['diff'] = employees['out_time'] - employees['in_time']
    return employees.groupby(by=['event_day', 'emp_id']).sum().reset_index().drop(['in_time', 'out_time'], axis=1).rename({'event_day': 'day', 'diff': 'total_time'}, axis=1)