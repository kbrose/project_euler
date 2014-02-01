def embed(space):
    len_x = len(space)
    len_y = len(space[0])
    zeros = [0]*(len_x+2)
    print zeros
    new_space = [[[[0]+space[x][y]+[0]] for y in range(len_y)] for x in range(len_x)]
    new_space = 
    return new_space

def show_space(space):
    for thing in space:
        print thing

space = [[[1,1] for i in range(2)] for j in range(2)]
show_space(space)
print 'BREAK'
show_space(embed(space))
