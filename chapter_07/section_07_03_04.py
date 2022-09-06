set_a = {2, 4, 6, 8}
set_b = {3, 6, 9}
result_1 = set_a | set_b
print(result_1)
# => {2, 3, 4, 6, 8, 9}

result_2 = set_a.union(set_b)
print(result_2)
# => {2, 3, 4, 6, 8, 9}

# ==============================================

set_a = {2, 4, 6, 8}
list_b = [3, 6, 9]
set_c = set_a.union(list_b)
print(set_c)
# => {2, 3, 4, 6, 8, 9}

# ==============================================

set_a = {2, 4, 6, 8}
set_b = {3, 6, 9}
result_1 = set_a & set_b
print(result_1)
# => {6}

result_2 = set_a.intersection(set_b)
print(result_2)
# => {6}

# ==============================================

set_a = {2, 4, 6, 8}
set_b = {3, 6, 9}

result_1 = set_a - set_b
print(result_1)
# => {8, 2, 4}

result_2 = set_b - set_a
print(result_2)
# => {9, 3}

# ==============================================

set_a = {2, 4, 6, 8}
set_b = {3, 6, 9}

result = set_a ^ set_b
print(result)
# => {2, 3, 4, 8, 9}

result = set_a.symmetric_difference(set_b)
print(result)
# => {2, 3, 4, 8, 9}
