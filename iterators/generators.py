
# python generators

# odd index generator
def odd_index_generator(data):
    for i in range(1, len(data), 2):
        yield data[i]



# even index generator
def even_index_generator(data):
    for i in range(0, len(data), 2):
        yield data[i]



# chained generators

def gen_num_10():
    for i in range(10):
        yield i

def squared(gennum):
    for j in gennum:
        yield j*j

gensquared = squared(gen_num_10)


# chained generator using generator expression

gen_num_10 = (i for i in range(10))
squared = (i*i for i in gen_num_10)
oddgen = (i for i in squared if i%2 == 0)

for _ in oddgen:
    print(_)


