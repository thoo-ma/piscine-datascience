import os
import pandas as pd

csv=[
  '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/customer/data_2022_oct.csv',
  '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/customer/data_2022_nov.csv',
  '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/customer/data_2022_dec.csv',
  '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/customer/data_2023_jan.csv',
  '/sgoinfre/goinfre/Perso/trobin/piscine-datascience/subject/customer/data_2023_feb.csv'
]

total_lines_count = 0
total_lines_dup = 0

# TODO line.strip()
# for file in csv:
#   lines_count = sum(1 for _ in open(file))
#   lines_dup = lines_count - len(set(line for line in open(file)))
#   print(f'{os.path.basename(file)}: {lines_count} lines ({lines_dup} duplicates)')
#   total_lines_count += lines_count
#   total_lines_dup += lines_dup

# print(f'Total of {total_lines_count} lines for {total_lines_dup} duplicates ({total_lines_count - total_lines_dup} unique lines)')

total_lines = 0
total_rows = 0
total_unique_rows = 0
for file in csv:
  lines = sum(1 for _ in open(file))
  total_lines += lines
  df = pd.read_csv(file, on_bad_lines='skip')
  print(f'{os.path.basename(file)}: {lines} lines, {df.shape[0]} rows ({lines - df.shape[0]} diff)', end=', ')
  total_rows += df.shape[0]
  df.drop_duplicates(inplace=True)
  total_unique_rows += df.shape[0]
  print(f'{df.shape[0]} unique rows')

# df = pd.concat([pd.read_csv(a, on_bad_lines='skip') for a in csv])
# print(f'total shape {df.shape}')
# print(f'total lines {total_lines}')
print(f'Total: {total_lines} lines, {total_rows} rows, {total_unique_rows} unique rows')