ma=0
me=0
for c in range (1,8):
    p=float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if p==1:
        ma=p
        me=p
    else:
        if p>ma:
            ma=p
        if p<me:
            me=p
print ('O maior peso informado foi {}Kg.'.format(ma))
print ('O menor peso foi {}Kg.'.format(me))
