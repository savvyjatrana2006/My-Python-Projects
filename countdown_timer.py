import time

def countdown_timer(seconds):
    while seconds > 0:
        # Format time as minutes:seconds
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        
        # Print the countdown time
        print(timer, end="\r")  # '\r' overwrites the previous line
        
        # Sleep for 1 second and reduce the total time by 1 second
        time.sleep(1)
        seconds -= 1
    
    # When the countdown ends
    print("Time's up!")

# Example usage:
try:
    total_seconds = int(input("Enter the time in seconds for the countdown: "))
    countdown_timer(total_seconds)
except ValueError:
    print("Please enter a valid number!")
