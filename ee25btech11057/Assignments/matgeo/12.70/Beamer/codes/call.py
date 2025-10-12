import ctypes

# Load the shared object file (make sure plough.so is in the same directory)
plough = ctypes.CDLL('./plough.so')

# Define argument and return types for the C function
plough.days_for_bullocks_alone.argtypes = [ctypes.c_double, ctypes.c_double]
plough.days_for_bullocks_alone.restype = ctypes.c_double

def main():
    print(" Bullocks and Tractors Ploughing Problem ")
    # Get input values
    X = float(input("Enter number of bullocks (X): "))
    Y = float(input("Enter number of tractors (Y): "))

    # Call the C function
    T = plough.days_for_bullocks_alone(X, Y)

    # Display result
    print(f"\n➡ Days taken by {X:.0f} bullocks alone to plough the field = {T:.2f} days")

if __name__ == "__main__":
    main()

