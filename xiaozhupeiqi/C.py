fname = input().rstrip('\n')
try:
    with open(fname, 'r') as f:
        min_m = 999 
        min_f = 'aaaa'
        max_m = 0
        max_f = 'bbbb' 
        for line in f:
            data = line.rstrip('\n').split(';')
            metric = int(data[1]) + int(data[2]) + int(data[3]) + int(data[4])



            if metric < min_m:
                min_m = metric
                min_f = data[0]
            if metric > max_m:
                max_m = metric
                max_f = data[0]



        print(max_f, max_m)
        print(min_f, min_m)
except:
     print('no data')


