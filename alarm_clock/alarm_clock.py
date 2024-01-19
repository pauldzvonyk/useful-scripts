from playsound import playsound
import time


# ANSI escape sequences to manipulate the terminal
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(CLEAR_AND_RETURN)

        # formating variables {:start with 0 or default value, 2 digits}
        print(f"{minutes_left:02d}:{seconds_left:02d}")


alarm(10)
#playsound('hohoho.mp3')

