import os
import pandas as pd

input_dir = '/input'
output_dir = '/output'

reports = []
report_path_list = []

pattern = r'[0-9]*_000[0-9]'

for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith('.xlsx') or file.endswith('.xls'):
            report_path_list.append(os.path.join(root, file))

for i, report_path in enumerate(report_path_list):
    df = pd.read_excel(report_path, skiprows=0, usecols=[3, 4])
    matched_pattern = df.iloc[:, 0].str.match(pattern)
    reports.append(df.where(matched_pattern).dropna())

final_reports = pd.concat(reports).drop_duplicates()
final_reports.to_csv(os.path.join(output_dir, 'report.csv'), index=False, header=False)
