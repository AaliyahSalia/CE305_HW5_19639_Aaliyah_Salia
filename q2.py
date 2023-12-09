def store(storage, address, block_data):
    storage[address] = block_data
    return storage

# Initialize main memory
init_mem = {}

# Take memory address as the key and all values in the block as the key's value
a = {"00000110101000": [0, 1, 2, 3, 4, 5, 6, 7]}

# Store the block into memory
# We take the address '00000110101000', strip the word index, and use it as the key
mem = store(init_mem, "00000110101000"[:-3] + '000', a["00000110101000"])

print(mem)  # This will print the updated memory with the stored block
def store(storage, elm):
    # elm is a dictionary with one key-value pair: 
    # the key is the memory address and the value is the block data.
    # This function will add the block to the storage.
    storage.update(elm)
    return storage

# Initialize main memory
init_mem = {}

# Memory blocks to be stored
a = {"00000110101000": [0, 1, 2, 3, 4, 5, 6, 7]}  # Block 'a'
b = {"00001110101000": [10, 11, 12, 13, 14, 15, 16, 17]}  # Block 'b'

# Store the blocks in memory
mem = store(init_mem, a)
mem = store(mem, b)

# Print the memory to check if the blocks are stored correctly
print(mem)

# Store function to update the memory with the given block
def store(storage, elm):
    storage.update(elm)
    return storage

# Direct map cache function to map a block of memory to the cache
def dir_map_cache(cache, adr, storage):
    block_number = adr[7:11]  # Extract the block number (4 bits)
    tag = adr[:7]  # Extract the tag (7 bits)
    block_base_address = adr[:11] + '000'  # Base address of the block

    if block_base_address in storage:
        # Update the cache line with the new block data and tag
        cache[block_number] = [tag, storage[block_base_address], 1]
    else:
        # If the block is not found in storage, it cannot be mapped to the cache
        print(f"Address {adr} block not found in storage. Cannot map to cache.")

    return cache

# Initialize main memory and cache
init_mem = {}
cache = {f"{i:04b}": ["0000000", [0] * 8, 0] for i in range(16)}

# Define memory blocks to store in memory
a = {"00000110101000": [0, 1, 2, 3, 4, 5, 6, 7]}  # Block 'a'
b = {"00001110101000": [10, 11, 12, 13, 14, 15, 16, 17]}  # Block 'b'

# Store the blocks in memory
mem = store(init_mem, a)
mem = store(mem, b)

# Address to be mapped to the cache
adr1 = "00000110101010"  # Hex address: 1AA
adr2 = "00001110101010"  # Hex address: 3AA
adr3 = "00001110111111"  # Hex address: 3BF

# Map the addresses to the cache
cache = dir_map_cache(cache, adr1, mem)
cache = dir_map_cache(cache, adr2, mem)
cache = dir_map_cache(cache, adr3, mem)

# Print the cache after mapping
for k, v in cache.items():
    print(f"Cache line {k}: Tag: {v[0]}, Data: {v[1]}, Valid: {v[2]}")

def check_cache(cache, adr):
    # Extract the block number (4 bits) and tag (7 bits) from the address
    block_number = adr[7:11]
    tag = adr[:7]
    
    # Check if the cache line exists and if the tag matches and is valid
    if cache.get(block_number, [None, None, 0])[0] == tag and cache[block_number][2] == 1:
        return "Hit"
    else:
        return "Miss"

# Given code with the store and dir_map_cache functions and memory/cache initialization
# ...

# Addresses to be checked in the cache
adr1 = "00000110101010"  # Hex address: 1AA
adr2 = "00001110101010"  # Hex address: 3AA
adr3 = "00001110111111"  # Hex address: 3BF

# Check if each address is saved in cache or not
result_adr1 = check_cache(cache, adr1)
result_adr2 = check_cache(cache, adr2)
result_adr3 = check_cache(cache, adr3)

# Output the results of the cache check
print(f"Address {adr1}: {result_adr1}")  # Expected: Hit
print(f"Address {adr2}: {result_adr2}")  # Expected: Miss
print(f"Address {adr3}: {result_adr3}")  # Expected: Hit
