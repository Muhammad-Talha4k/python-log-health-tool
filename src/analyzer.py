def count_logs(df):
    return len(df)
def error_summary(df):
    return df["level"].value_counts().to_dict()

def group_by_time(df):
    df["hour"] = df["timestamp"].str[:13]
    return df.groupby("hour").size()
    return df.groupby("hour").size()

