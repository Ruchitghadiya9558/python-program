# i=pnr/100 p=principal of amount n=number of year r=rate
person = int(input('enter the amount:'))
year   = int (input ('how many year:'))
per    = int (input ('enter the percentage:'))

si=(person+year+per)/100
print('simple interest=',si)

if si>=10:
    print('yes')
else:
    print('no')