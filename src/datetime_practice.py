from datetime import datetime, timedelta

# getting the current date and time:
now = datetime.now()
#print(now)

# -------------------------------------
# formatting datetime
formatted = now.strftime("%Y-%m-%d")
time_formatted = now.strftime("%H:%M")

print(f"Today is {formatted}, and the time is {time_formatted}")

# -------------------------------------
# date arithmetics
seven_days_from_now = now + timedelta(days=7)
thirty_days_ago = now - timedelta(days=30)

print("7 days from now:", seven_days_from_now.strftime("%Y-%m-%d"))
print("30 days ago:", thirty_days_ago.strftime("%Y-%m-%d"))

