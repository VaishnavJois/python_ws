c_word = 0
c_lines = 0
d = {}
try:
    with open('data.txt') as fin, open("U_data.txt",'w') as fout:
        lines = fin.readlines()
        lines = [l.upper() for l in lines]
        fout.writelines(lines)
        #no_of_lines = len(lines)
        '''
        for line in lines:
            c_lines += 1
            for w in line.split():
                c_word += 1
                if w not in d:
                    d[w] = 1
                else:
                    d[w] += 1
        print(c_word)
        for k,v in d.items():
            print(k,v)
        '''
except Exception as e:
    print(e)
