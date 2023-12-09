# Initialize an empty dictionary to represent memory
init_mem = {}

# Define the 'store' function to add or update an element in memory
def store(storage, elm):
    for address, value in elm.items():
        storage[address] = value
    return storage

# Define the 'imm_load_ac' function for immediate addressing
def imm_load_ac(val):
    return val

# Define the 'dir_load_ac' function for direct addressing
def dir_load_ac(storage, val):
    return storage[val]

# Define the 'indir_load_ac' function for indirect addressing
def indir_load_ac(storage, val):
    # Get the address stored at the given 'val' location
    # and then load the value stored at that address
    return storage[storage[val]]

# Define the 'idx_load_ac' function for indexed addressing
def idx_load_ac(storage, idx, val):
    # Add the index to the base address and then load the value stored at that calculated address
    return storage[val + idx]

# Simulate memory storage operations
a = {800: 123}
b = {900: 1000}
c = {800: 900}
d = {1500: 700}

# Store the values in memory
mem = store(init_mem, a)  # mem = {800: 123}
mem = store(mem, b)       # mem = {800: 123, 900: 1000}
mem = store(mem, c)       # mem = {800: 900, 900: 1000}
mem = store(mem, d)       # mem = {800: 900, 900: 1000, 1500: 700}

# Load values into the accumulator using different addressing modes
ac = imm_load_ac(800)  # Immediate addressing: ac = 800
ac = dir_load_ac(mem, 800)  # Direct addressing: ac = 900
ac = indir_load_ac(mem, 800)  # Indirect addressing: ac = 1000
idxreg = 700
ac = idx_load_ac(mem, idxreg, 800)  # Indexed addressing: ac = 700

# Print the accumulator after each operation to verify the results
print(f"Immediate Addressing: ac = {imm_load_ac(800)}")  # Should print ac = 800
print(f"Direct Addressing: ac = {dir_load_ac(mem, 800)}")  # Should print ac = 900
print(f"Indirect Addressing: ac = {indir_load_ac(mem, 800)}")  # Should print ac = 1000
print(f"Indexed Addressing: ac = {idx_load_ac(mem, idxreg, 800)}")  # Should print ac = 700
