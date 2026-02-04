def count_logs(df):
    return len(df)
def error_summary(df):
    return df["level"].value_counts().to_dict()

