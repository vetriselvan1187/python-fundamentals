
# python generators

# odd index generator
def odd_index_generator(data):
    for i in range(1, len(data), 2):
        yield data[i]



# even index generator
def even_index_generator(data):
    for i in range(0, len(data), 2):
        yield data[i]



