import pandas as pd

def load_logs(path):
    import pandas as pd
    try:
        return pd.read_csv(path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()

