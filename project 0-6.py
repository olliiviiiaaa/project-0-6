import os

# Define the file to store authorized vehicles
vehicles_file = "AuthorizedVehicles.txt"

# Load the list of authorized vehicles from the file
def load_vehicles():
    if not os.path.exists(vehicles_file):
        with open(vehicles_file, "w") as file:  # Create the file if it doesn't exist
            file.write("Ford F-150\nChevrolet Silverado\nTesla CyberTruck\nToyota Tundra\nRivian R1T\nRam 1500\n")
    with open(vehicles_file, "r") as file:
        return [line.strip() for line in file.readlines()]

# Save the list of authorized vehicles back to the file
def save_vehicles(vehicles_list):
    with open(vehicles_file, "w") as file:
        file.write("\n".join(vehicles_list) + "\n")

# Function to PRINT all Authorized Vehicles
def print_vehicles(vehicles_list):
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in vehicles_list:
        print(vehicle)
    print()

# Function to SEARCH for an Authorized Vehicle
def search_vehicle(vehicles_list):
    vehicle_to_search = input("Please enter the full vehicle name: ").strip()
    if vehicle_to_search in vehicles_list:
        print(f"{vehicle_to_search} is an authorized vehicle.\n")
    else:
        print(f"{vehicle_to_search} is NOT an authorized vehicle. Please check the spelling and try again.\n")

# Function to ADD an Authorized Vehicle
def add_vehicle(vehicles_list):
    vehicle_to_add = input("Please enter the full vehicle name you would like to add: ").strip()
    if vehicle_to_add in vehicles_list:
        print(f'"{vehicle_to_add}" is already in the authorized vehicles list.\n')
    else:
        vehicles_list.append(vehicle_to_add)
        save_vehicles(vehicles_list)
        print(f'You have added "{vehicle_to_add}" as an authorized vehicle.\n')

# Function to DELETE an Authorized Vehicle
def delete_vehicle(vehicles_list):
    vehicle_to_delete = input("Please enter the full vehicle name you would like to REMOVE: ").strip()
    if vehicle_to_delete in vehicles_list:
        confirmation = input(f'Are you sure you want to remove "{vehicle_to_delete}" from the Authorized Vehicles List? (yes/no): ').strip().lower()
        if confirmation == "yes":
            vehicles_list.remove(vehicle_to_delete)
            save_vehicles(vehicles_list)
            print(f'You have REMOVED "{vehicle_to_delete}" as an authorized vehicle.\n')
        else:
            print("Vehicle removal canceled.\n")
    else:
        print(f'"{vehicle_to_delete}" is not in the Authorized Vehicles List.\n')

# Main menu to handle user choices
def menu():
    vehicles_list = load_vehicles()  # Load vehicles from the file
    while True:
        print("********************************")
        print("AutoCountry Vehicle Finder v0.5")
        print("********************************")
        print("Please enter a number from the following menu:")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for an Authorized Vehicle")
        print("3. ADD an Authorized Vehicle")
        print("4. DELETE an Authorized Vehicle")
        print("5. Exit")
        
        # Get user input
        choice = input("\nEnter your choice (1, 2, 3, 4, or 5): ").strip()
        
        if choice == "1":
            print_vehicles(vehicles_list)
        elif choice == "2":
            search_vehicle(vehicles_list)
        elif choice == "3":
            add_vehicle(vehicles_list)
        elif choice == "4":
            delete_vehicle(vehicles_list)
        elif choice == "5":
            print("Thank you for using the AutoCountry Vehicle Finder. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

# Start the program
if __name__ == "__main__":
    menu()
