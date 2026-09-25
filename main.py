import math
import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.duration = None

    def start(self):
        # TODO: getters and setters for these attributes? (and refresh the concepts)
        self.start_time = time.monotonic()
        self.end_time = self.start_time + self.duration

    def pause(self):
        pass

    def stop(self):
        print("\rUser forced the stop of the timer")
        print("Ended with: ", self.end_time - time.monotonic(), " seconds left.")

    def run(self):
        """Does the main countdown logic:
        - Gets the user input from 'input_time()' function.
        - Sets the values of Timer attributes by calling 'start()' function.
        - Runs the main countdown loop.
        """
        self.duration = input_time()
        self.start()
        try:
            while True:
                remaining = self.end_time - time.monotonic()
                if (remaining <= 0):
                    break
                print(f"\rLeft: {math.ceil(remaining)} seconds", end="")
                time.sleep((remaining) % 1)
            print("\nTimer ended successfully")
        except KeyboardInterrupt:
            self.stop()

def input_time():
    """Asks the user for the timer duration.

    Returns:
        float: Total time in seconds.
    """
    # Read user input
    minutes = float(input("Minutes: "))
    seconds = float(input("Seconds: "))

    # Converts minutes to seconds and adds them to seconds variable
    seconds += minutes * 60

    # TODO: probably I'll have to return minutes too in the future so I can display them
    return seconds


if __name__ == "__main__":
    timer = Timer()
    timer.run()