import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    
    teacher = teacher.groupby(by="teacher_id").nunique().reset_index().drop('dept_id', axis=1).rename(columns={'subject_id': 'cnt'})
    return teacher