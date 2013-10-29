def read_in():
    f = open('p107_text.txt')
    G = [[0 for i in range(40)] for j in range(40)]

    fr = f.readline()
    i = 0
    while fr:
        fs = fr.strip().split(',')
        for j in range(len(fs)):
            if fs[j] == '-':
                continue
            G[i][j] = int(fs[j])
        i += 1
        fr = f.readline()
    return G

# uses Prim's algorithm
def find_next_min(G, G_new_verts):
    curr_min = 10000000
    curr_vert = -1
    for i in range(40):
        for j in range(i+1,40):
            if G[i][j] < curr_min and ((i not in G_new_verts and j in G_new_verts) or (j not in G_new_verts and i in G_new_verts)) and G[i][j] > 0:
                curr_min = G[i][j]
                if i in G_new_verts:
                    curr_vert = j
                else:
                    curr_vert = i
    return curr_vert, curr_min

def main():
    G = read_in()
    
    init_weight = 0
    for i in range(40):
        for j in range(i, 40):
            init_weight += G[i][j]
    
    total_cost = 0
    G_new_verts = [0]
    while len(G_new_verts) < 40:
        vert, take_away = find_next_min(G, G_new_verts)
        G_new_verts.append(vert)
        total_cost += take_away
    print init_weight - total_cost


main()
