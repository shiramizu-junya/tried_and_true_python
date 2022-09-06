from turtle import color


fruits = ['apple', 'orange', 'apple', 'banana', 'mango', 'grape', 'orange']
temp = set(fruits)
fruits = list(temp)
fruits
# => ['mango', 'orange', 'banana', 'apple', 'grape']

# ==============================================

colors_1 = ['red', 'green', 'blue', 'white', 'black']
colors_2 = ['yellow', 'magenta', 'cyan', 'black', 'white']

colors = colors_1 + colors_2

colors
# => ['red', 'green', 'blue', 'white', 'black', 'yellow', 'magenta', 'cyan', 'black', 'white']

# ==============================================

colors_1 = ['red', 'green', 'blue', 'white', 'black']
colors_2 = ['yellow', 'magenta', 'cyan', 'black', 'white']
colors = set(colors_1) | set(colors_2)
colors
# => {'black', 'blue', 'red', 'yellow', 'cyan', 'magenta', 'white', 'green'}
colors = list(colors)
colors
# => ['black', 'blue', 'red', 'yellow', 'cyan', 'magenta', 'white', 'green']
