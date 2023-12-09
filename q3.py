# Define the store function to update the main memory with the given block
def store(storage, elm):
    storage.update(elm)
    return storage

# Define the map_to_cache function for a fully associative cache
def map_to_cache(cache, storage):
    for address, block in storage.items():
        # Convert the binary address to a tag and find a cache line
        tag = address[:-3]  # Last 3 bits are for the word within a block, so they're excluded from the tag

        # Find an empty cache line or one that can be replaced
        for cache_line in cache.values():
            if cache_line[2] == 0:  # Check if the valid bit is 0, indicating an empty line
                cache_line[0] = tag  # Set the tag
                cache_line[1] = block  # Set the block data
                cache_line[2] = 1  # Set the valid bit to 1 (occupied)
                break
        else:
            print(f"No empty cache lines available to map the address {address}.")
            break  # If no empty line was found, break out of the loop

    return cache

# Initialize main memory and cache
init_mem = {}
cache = {
    "blk0": ["00000000000", [0]*8, 0],
    "blk1": ["00000000000", [0]*8, 0],
    "blk2": ["00000000000", [0]*8, 0],
    "blk3": ["00000000000", [0]*8, 0]
}

# Define memory blocks to store in memory
a = {"00000110101000": [0, 1, 2, 3, 4, 5, 6, 7]}
b = {"00001110101000": [10, 11, 12, 13, 14, 15, 16, 17]}
c = {"00011110101000": [20, 21, 22, 23, 24, 25, 26, 27]}
d = {"00111110101000": [30, 31, 32, 33, 34, 35, 36, 37]}
e = {"01111110101000": [40, 41, 42, 43, 44, 45, 46, 47]}

# Store the blocks in memory
mem = store(init_mem, a)
mem = store(mem, b)
mem = store(mem, c)
mem = store(mem, d)
mem = store(mem, e)

# Map the blocks to the cache
cache = map_to_cache(cache, mem)

# Print the state of the cache
for k, v in cache.items():
    print(f"Cache line {k}: Tag: {v[0]}, Data: {v[1]}, Valid: {v[2]}")


def fully_ass_cache(cache, adr, storage):
    # Extract the tag (11 bits) from the address
    tag = adr[:-3]  # Last 3 bits are for the word within a block, remove to get the tag

    # Convert the address to a block's base address by setting the last 3 bits to '000'
    block_base_address = adr[:-3] + '000'

    # Check if the block is in storage
    if block_base_address not in storage:
        raise ValueError(f"Block with base address {block_base_address} not found in storage.")

    # Check for an available cache line (valid bit is 0)
    for line, data in cache.items():
        if data[2] == 0:  # The line is available
            cache[line] = [tag, storage[block_base_address], 1]
            return cache

    # If no lines are available, choose one to evict (for example, the first one)
    # For simplicity, we're evicting the first line, but this can be replaced with a better policy
    line_to_evict = 'blk0'
    print(f"No empty cache lines available, evicting {line_to_evict}.")
    cache[line_to_evict] = [tag, storage[block_base_address], 1]
    
    return cache


# Store blocks in memory with the base address as the key
mem = store(mem, {"01111110101000": [40, 41, 42, 43, 44, 45, 46, 47]})

# Try to map adr5 to the cache, which should trigger an eviction
adr5 = '01111110101110'  # hex address: 1FAE
cache = fully_ass_cache(cache, adr5, mem)

# Print the cache after attempting to map adr5
for k, v in cache.items():
    print(f"Cache line {k}: Tag: {v[0]}, Data: {v[1]}, Valid: {v[2]}")
