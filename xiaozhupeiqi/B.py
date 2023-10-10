fname = input()

try:
    with open(fname) as f:
        min_m = 0
        min_f = ''
        max_m = 0
        max_f = '' 
        for line in f.readlines():
            data = line.rstrip('\n').split(';')
            metric = int(data[1]) + int(data[2]) + int(data[3]) + int(data[4])
            min_m = metric if metric < min_m else min_m
            min_f = data[0] if metric < min_m else min_f
            max_m = metric if metric > max_m else max_m
            max_f = data[0] if metric > max_f else max_f
        
        print(max_f, max_m)
        print(min_f, min_m)
except:
    print('no data')