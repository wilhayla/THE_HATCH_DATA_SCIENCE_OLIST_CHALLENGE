import pandas as pd

def convert_dates(df: pd.DataFrame, date_cols: list) -> pd.DataFrame:

    '''Convierte una lista de columnas a formato datetime de Pandas.'''

    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coarce')
            
    return df