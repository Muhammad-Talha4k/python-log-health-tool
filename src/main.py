from loader import load_logs
from analyzer import count_logs
from reporter import print_total

df = load_logs("data/app_logs.csv")
print_total(count_logs(df))
