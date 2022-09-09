def fun_var(a):
  a = 10
  return

num = 5
fun_var(num)
print(num)  # => 5

# ==============================================

def func_list(a):
  a[2] = 10
  return

nums = [1, 2, 3, 4, 5]
func_list(nums)
print(nums)  # => [1, 2, 10, 4, 5]
