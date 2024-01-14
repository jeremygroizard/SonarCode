print("SonarCode")
print("Hello Jeremy ! Have a good day learning Python !")
from datetime import datetime

# Asking user to enter the limit date :
limit_date_input = input("Enter the limit date : (format YYYY-MM-DD HH:MM): ")

# Convert limit_date in datetime object :
limit_date = datetime.strptime(limit_date_input, "%Y-%m-%d %H:%M")

# Obtain date and actual hour :
now = datetime.now()

# Calculate the différence :
time_left = limit_date - now

# Extract days, hours and minutes :
days = time_left.days
hours, remainder = divmod(time_left.seconds, 3600)
minutes, secondes = divmod(remainder, 60)

# Display the time left :
print(f"Time left : {days} days, {hours} hours and {minutes} minutes.")




