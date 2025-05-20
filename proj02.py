# proj01.py

def calculate_energy(richter):
    # Energy in joules based on the Richter scale
    energy_joules = 10 ** (1.5 * richter + 4.8)
    # Convert joules to tons of TNT
    energy_tnt = energy_joules / (4.184 * 10**9)
    return energy_joules, energy_tnt


def main():
    # Predefined Richter scale measurements
    richter_values = [1.0, 5.0, 9.1, 9.2, 9.5]
    
    print("Earthquake Energy Calculator")
    print("=============================")
    
    # Calculate and display energy for predefined Richter values
    for richter in richter_values:
        energy_joules, energy_tnt = calculate_energy(richter)
        print(f"Richter Scale: {richter:.1f} -> Energy: {energy_joules:.2e} Joules, "
              f"Equivalent: {energy_tnt:.2f} tons of TNT")
    
    # Prompt user for a Richter scale measurement
    user_input = input("Please enter a Richter scale measurement: ")
    
    try:
        user_richter = float(user_input)
        if user_richter < 0:
            print("Please enter a positive number.")
        else:
            energy_joules, energy_tnt = calculate_energy(user_richter)
            print(f"Richter Scale: {user_richter:.1f} -> Energy: {energy_joules:.2e} Joules, "
                  f"Equivalent: {energy_tnt:.2f} tons of TNT")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
