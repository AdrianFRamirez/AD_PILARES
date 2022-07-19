list4 = [ 
        ('juan', 45),
        ('maruti', 33),
        ('honda', 22)
        ]
print(len(list4))
DictNom={}
cont2=0
while cont2<(len(list4)):
    #my_dict['address'] = 'Downtown' for add
    #DictNom={cont2:list4[cont2]} solo agrega 1 vez y ya
    DictNom[cont2+1]=list4[cont2]
    cont2 += 1
print(DictNom)