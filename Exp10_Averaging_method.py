import numpy as np
import matplotlib.pyplot as plt

# Time series data
data = [10, 12, 13, 15, 18, 20, 22, 25]

# Calculate average
avg = np.mean(data)

print(avg)

print("Average value:", avg)

# Predict next 3 values using average
forecast = [avg, avg, avg]
print("Forecast:", forecast)


# Plot
plt.plot(data)


plt.plot(forecast, label="Forecast")

plt.show()