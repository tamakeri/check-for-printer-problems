
# Initialize a variable to store the value
value = 0

# Function to add a number to the value
def add(num):
    global value
    value += num

# Function to get the current value
def get_value():
    global value
    return value

# Add some numbers
add(5)
add(10)

# Get the current value
result = get_value()
print(f"Current Value: {result}")
