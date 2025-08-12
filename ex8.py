from datetime import datetime

now = datetime.now()
print("Current date and time :",now)
print("Current date:",now.date())
print("Current Time:",now.time())
formulated_time = now.strftime("%Y-%m-%d %H:%M:%S")

print("Formulated date and time:", formulated_time)
