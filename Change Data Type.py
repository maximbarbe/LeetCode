import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = pd.Series(map(int, students["grade"]))
    return students