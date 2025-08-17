import pandas as pd
import matplotlib.pyplot as plt
import re

def parse_log(file_path):
    pattern = r'^\[(.*?)\]\s+(\w+)\s+-\s+(.*)$'
    records = []

    with open(file_path, 'r') as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                timestamp, level, message = match.groups()
                records.append({'timestamp': timestamp, 'level': level, 'message': message})

    return pd.DataFrame(records)

def summarize_logs(df):
    return df['level'].value_counts()

def plot_summary(summary):
    summary.plot(kind='bar', title='Log Level Frequency')
    plt.xlabel('Log Level')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    log_file = 'sample_log.txt'  # Placeholder log file
    df_logs = parse_log(log_file)
    summary = summarize_logs(df_logs)
    plot_summary(summary)
