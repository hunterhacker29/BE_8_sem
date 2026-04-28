import matplotlib.pyplot as plt
import math
# Static Poisson-like data (λ ≈ 3)
data = [0,1,1,2,2,2,3,3,3,3,3,4,4,4,5,5,6]


lam = 0.1

p0 = math.exp(-lam)* (lam**0)/math.factorial(0)
p1 = math.exp(-lam)* (lam**1)/math.factorial(1)


p = 1-(p0+p1)
print("P(X>1) =", p)

plt.hist(data, bins=range(0,8), edgecolor='black')

plt.title("Poisson Distribution (λ ≈ 3)")
plt.xlabel("Number of Events")
plt.ylabel("Frequency")

plt.show()
