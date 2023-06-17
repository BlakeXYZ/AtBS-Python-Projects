#! python3


numbers = """1
18
53
5
138
255
205
10
202
136
44
103
15"""

num_list = numbers.split('\n')

total_sum = sum(int(value) for value in num_list)

print(num_list)
print(total_sum)