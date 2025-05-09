with open ('public/dest-data/desc/kochi.txt') as f:
    k = f.readlines()
    m = ''
    for i in k:
        for u in i.split():
            if u != 'he':
                m+= u + ' '
            else: 
                m+= 'she '

    print(m)


    
