from turtle import color


colors = {'red', 'green', 'blue'}
colors.add('yellow')
colors
# => {'red', 'yellow', 'blue', 'green'}

# ==============================================

colors = {'red', 'green', 'blue'}
colors.add('red')
colors
# => {'red', 'blue', 'green'}

# ==============================================

colors = {'red', 'green', 'blue'}
print(colors.pop())
colors

# ==============================================

colors = {'red', 'green', 'blue'}
colors.remove('red')
colors
# => {'blue', 'green'}

colors.remove('pink')
# => KeyError: 'pink'

# ==============================================

colors = {'red', 'green', 'blue'}
colors.discard('yellow')
colors
# => {'red', 'blue', 'green'}

colors.discard('red')
colors
# => {'blue', 'green'}

