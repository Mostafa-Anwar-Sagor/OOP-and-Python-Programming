a=1
boss= False

if a>5:
    print('5 er besi')
    print('lagbe koto')
elif a>3:
    print('olpo bor0')
elif a==2:
    print('akdom 2er soman')
else:
    print('choto rat')


if boss is True:
    print('lunch er pore ashen')
else:
    print('tel er baksho niye ashtesi boss re tel dibo')

coin='head'
#nested conditon
if boss==True:
    print('boss youre joss')
    if coin== 'tail':
        print('batting')
    else:
        print('bolling')
else:
    print('youre not boss')