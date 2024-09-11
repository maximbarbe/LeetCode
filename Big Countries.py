import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world.area >= 3*10**6) | (world.population >= 25* 10**6)].drop(columns=["continent", "gdp"])