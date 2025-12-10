# En src/data_processing.py

import pandas as pd

# 1. DEFINIR LA CONSTANTE FUERA DEL CUERPO DE LA FUNCIÓN
#    Así es accesible inmediatamente y es una constante del módulo.
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def convert_dates(df: pd.DataFrame, date_cols: list) -> pd.DataFrame:
    """Convierte una lista de columnas a formato datetime de Pandas, especificando el formato."""
    
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(
                df[col], 
                format=DATE_FORMAT, # <-- Se usa la constante definida arriba
                errors='coerce'
            )
    return df
