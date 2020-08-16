import matplotlib.pyplot as p
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
a = [1, 2, 3, 4]
b = [2, 4, 6, 8]
lines = p.plot(x, y, a, b)
p.setp(lines[0], color='r')   # x y line
p.setp(lines[1], color='g')   # a b line
p.ylabel("y-axis")
p.xlabel("x-axis")
p.title("graph1")
p.plot(x, y, linewidth=6)  # thick line
p.grid()
p.show()