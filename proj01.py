# proj01.py
# CSE 231 Spring 2017
# Programming Project #1
# Author: [Rishi Dayal]
# Description: This program converts a distance in rods to meters, feet, miles, furlongs,
# and calculates the time to walk that distance at an average speed.
# Constants for conversions
ROD_TO_METERS = 5.0292
FURLONGS_IN_RODS = 40
MILES_IN_METERS = 1609.34
FEET_IN_METERS = 0.3048
AVERAGE_WALKING_SPEED_MPH = 3.1
def main():
    # Prompt the user for input
    rods_str = input("Please enter a distance in rods: ")
    rods = float(rods_str)  # Convert input to a floating-point number
    # Perform conversions
    meters = rods * ROD_TO_METERS
    feet = meters / FEET_IN_METERS
    miles = meters / MILES_IN_METERS
    furlongs = rods / FURLONGS_IN_RODS
    # Calculate time to walk the distance in minutes
    time_hours = miles / AVERAGE_WALKING_SPEED_MPH
    time_minutes = time_hours * 60
    # Display the results
    print(f"{rods} rods is equivalent to:")
    print(f"{meters:.2f} meters")
    print(f"{feet:.2f} feet")
    print(f"{miles:.2f} miles")
    print(f"{furlongs:.2f} furlongs")
    print(f"Time to walk: {time_minutes:.2f} minutes")
if __name__ == "__main__":
    main()