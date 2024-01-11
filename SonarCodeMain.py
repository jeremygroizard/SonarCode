print("SonarCode")
import time

def countdown_timer(seconds):
    while seconds > 0:
        days = seconds // (24 * 3600)
        hours = (seconds // 3600) % 24
        minutes = (seconds // 60) % 60
        seconds_left = seconds % 60
        print(f"Time remaining: {days} days, {hours} hours, {minutes} minutes, {seconds_left} seconds")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

def main():
    try:
        days = int(input("Enter the number of days: "))
        hours = int(input("Enter the number of hours: "))
        minutes = int(input("Enter the number of minutes: "))
        seconds = int(input("Enter the number of seconds: "))

        total_seconds = days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds
        countdown_timer(total_seconds)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
