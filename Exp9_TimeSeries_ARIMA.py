from statsmodels.tsa.arima.model import ARIMA

data = [10,12,13,15,18,20,22,25]

# Create model
model = ARIMA(data, order=(1,1,1))

# Fit model
model_fit = model.fit()

# Predict (next 3 values)
pred = model_fit.forecast(steps=3)

print(pred)