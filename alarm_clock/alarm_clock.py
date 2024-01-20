from playsound import playsound
import time
import os


class Alarm:
    def __init__(self):
        """
        Initializes the Alarm object.
        """
        pass

    @staticmethod
    def start_alarm(hours=0, minutes=0, seconds=0):
        """
        Starts the alarm countdown.

        Parameters:
        - hours (int): Number of hours for the alarm (default is 0).
        - minutes (int): Number of minutes for the alarm (default is 0).
        - seconds (int): Number of seconds for the alarm (default is 0).
        """
        total_time = hours * 3600 + minutes * 60 + seconds
        time_elapsed = 0

        # Clear the screen using os.system
        os.system('cls' if os.name == 'nt' else 'clear')

        while time_elapsed < total_time:
            time.sleep(1)
            time_elapsed += 1

            time_left = total_time - time_elapsed
            hours_left = time_left // 3600
            minutes_left = (time_left % 3600) // 60
            seconds_left = time_left % 60

            # Formatting variables {:start with 0 or default value, 2 digits}
            print(f"Remaining time: {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}", end='\r')

        # Print a newline to move to the next line after the alarm is complete
        print()

        # Play the sound using playsound
        playsound('hohoho.mp3')


if __name__ == "__main__":
    # Create an instance of the Alarm class
    alarm_instance = Alarm()

    # Get user input for hours and minutes
    h = int(input("Enter hours: "))
    m = int(input("Enter minutes: "))

    # Start the alarm countdown with a fixed 3 seconds of sound
    alarm_instance.start_alarm(hours=h, minutes=m, seconds=3)

"""
Simplified version
"""
# import time
# import os
#
# def alarm(secs):
#     os.system('cls')
#     for x in range(secs, -1, -1):
#         minutes, seconds = divmod(x, 60)
#         print(f"\r{minutes:02d}:{seconds:02d}", end="\r")
#         time.sleep(1)
#     print("Time Up!")
#
#
# alarm(3)