import numpy as np

a = np.array([['0', '', '12.12', '140.65', '', ''],
              ['3', '', '10.45', '154.45', '', ''],
              ['5', '', '15.65', '184.74', '', '']])

#data = np.char.replace(a, '', '0')
'''
elm = []
data = []

for item in a:
    for x in item:
        if(x == ''):
            elm.append('0')
        else:
            elm.append(x)
    data.append(elm)
    elm = []
'''
#a[np.where(a == '')] = '0'
a[a == ''] = '0'

a = a.astype(np.float64)

print(a)
