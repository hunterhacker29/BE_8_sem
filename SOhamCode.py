
#Bowley's Skewness

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
tips = sns.load_dataset('tips')
data = tips['total_bill']

q1, q2, q3 = np.percentile(data, [25, 50, 75])
bowley_skew = (q1 + q3 - 2 * q2) / q3 - q1

print(f"Q1: {q1:.2f} | Median (Q2): {q2:.2f} | Q3: {q3:.2f}")
print(f"Bowley Skewness: {bowley_skew:.3f}")

plt.figure(figsize=(8, 2.8))
ax = sns.boxplot(x=data)
ax.set_title("Boxplot with Bowley Skewness", pad=10)
ax.set_xlabel("Data")
plt.tight_layout()
plt.show()



#Normal Distribution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean, std = 150, 20
x = np.linspace(50, 250, 500)
y = norm.pdf(x, mean, std)

plt.figure(figsize=(11, 5))
plt.plot(x, y, label=f"Normal Distribution (mean={mean}, sd={std})")

regions = [
    ((x >= 140) & (x <= 160), "orange", "Between 140 and 160 g"),
    (x > 170, "green", "More than 170 g"),
    (x < 120, "red", "Less than 120 g"),
]
for mask, color, label in regions:
    plt.fill_between(x, 0, y, where=mask, color=color, alpha=0.45, label=label)

plt.xlabel("Weight (grams)")
plt.ylabel("Probability Density")
plt.title("Normal Distribution of Apple Weights")
plt.grid(alpha=0.3)
plt.legend()
plt.show()

p_140_160 = norm.cdf(160, mean, std) - norm.cdf(140, mean, std)
p_gt_170 = 1 - norm.cdf(170, mean, std)
p_lt_120 = norm.cdf(120, mean, std)

print(f"P(140 <= X <= 160): {p_140_160:.4f}")
print(f"P(X > 170): {p_gt_170:.4f}")
print(f"P(X < 120): {p_lt_120:.4f}")