budget = 1500.0 # answer shoudl be 1400
exchange_rate = 0.84
spread = 25
denomination = 40

actual_exchange_rate = exchange_rate + exchange_rate * (spread / 100)
exchange_value = budget / actual_exchange_rate
exchange_value = int(exchange_value / denomination) * denomination
#exchange_value = exchange_value // denomination
#exchange_value = exchange_value * denomination



print(int(exchange_value))
