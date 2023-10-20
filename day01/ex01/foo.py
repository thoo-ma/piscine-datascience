csv=[
  'day00/subject/customer/data_2022_oct.csv',
  'day00/subject/customer/data_2022_nov.csv',
  'day00/subject/customer/data_2022_dec.csv',
  'day00/subject/customer/data_2023_jan.csv',
  'day01/subject/customer/data_2023_feb.csv'
]

# for file in csv:
  # print(f'{file} {sum(1 for _ in open(file))} lines')
  # print(len(set(line for line in open(file))))

# print(len(list(line for line in open(csv[0]))))
# print(len(set(line for line in open(csv[0]))))

a = list(line for line in open('test.csv'))
b = set(line for line in open('test.csv'))

print(len(list(line for line in open('test.csv'))))
print(len(set(line for line in open('test.csv'))))

# for line in file1 & file2:
#     if line:
#         print line


