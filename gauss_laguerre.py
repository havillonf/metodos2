def laguerre5(x):
    return (1/120) * (-(pow(x, 5)) + 25(pow(x,4)) - 200(pow(x,3)) + 600(pow(x,2)) - 600*x + 120)

x = [0.32255, 1.7458, 4.5366, 9.3951]
w = [0, 0, 0, 0]

for i in range(4):
    w[i] = (x[i] / (25*pow(laguerre5(x[i]),2)))

print(w)