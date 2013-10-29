grid_size = 50 # assumes a square grid

counter = 3 * (grid_size * grid_size) # all cases that won't be covered

def gcd(a,b):
    while (b != 0) and (a != b) and (a != 0):
        if b < a:
            a = a - b
        else:
            b = b - a
    if a > 0:
        return a
    return b
end = grid_size+1

def my_append(arr, item):
    if item in arr:
        return 0
    arr.append(item)
    return 1

triangles = []

for x in xrange(1,end):
    for y in xrange(1,end):
        GCD = gcd(x,y)
        if GCD > 0:
            slope = [x / GCD, y / GCD]
            inv_slope = [y / GCD, -(x / GCD)]
        else:
            slope = [x,y]
            inv_slope = [y,-x]
        out_of_bounds_left = 0
        out_of_bounds_right = 0
        for mult in xrange(1,51):
            x_inc = mult*inv_slope[0]
            y_inc = mult*inv_slope[1]
            if ((x - x_inc < 0) or (y - y_inc > grid_size)):
                out_of_bounds_left = 1
            else:
                counter += my_append(triangles, [[0,0],[x,y],[x-x_inc,y-y_inc]])
            if ((x + x_inc > grid_size) or (y + y_inc < 0)):
                out_of_bounds_right = 1
            else:
                counter += my_append(triangles, [[0,0],[x,y],[x+x_inc,y+y_inc]])
            if (out_of_bounds_left and out_of_bounds_right):
                break

print counter
            
