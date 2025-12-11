import pandas as pd

def convert_dates(df: pd.DataFrame, date_cols: list) -> pd.DataFrame:

    '''Convierte una lista de columnas a formato datetime de Pandas.'''

    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(
                df[col], 
                format=DATE_FORMAT,
                errors='coarce'
                )

    return df 