


from lex_tabel import tabel


def preaperer():
    f = open("source.txt", "r")

    in_pipe = f.read()  # strips of white spaces

    in_pipe = in_pipe.replace('\n', ' ')
    in_pipe.split()
    f.close()

    return in_pipe


def finite_machina(tab, input):
    check = ''
    lo_match = []
    final = []
    def l_of_k(tab):
        list_of_keys = []
        tab = list(tab.values())

        for i in tab:
            i = i.values()

            for j in i:
                #print(j)
                list_of_keys.append(j)

        return list_of_keys

    for i in input:
        print(i)
        if i == ' ':
           
            lo_match.clear()
            if check in l_of_k(tab):
                final.append(check)
                check = ''
                

        
        
        else:
            check += i
            if check in l_of_k(tab):
                lo_match.append(check)
                 
        if '.' in check:
            final.append(check)
            check = ''            

        
       

   
    return final
print(finite_machina(tabel, preaperer()))