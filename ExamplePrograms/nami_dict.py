myDictPairs = {}
myFriendsNameAndBounty = {
    'luffy': 30,
    'zoro': 20
}

print(myDictPairs)
print(myFriendsNameAndBounty)
print(myFriendsNameAndBounty['luffy'])

myFriendsNameAndBounty['sanji'] = 15
print('After adding Sanji', myFriendsNameAndBounty)

del myFriendsNameAndBounty['zoro']
print('After Deleting Zoro', myFriendsNameAndBounty)

for key in myFriendsNameAndBounty:
    print(key, myFriendsNameAndBounty[key])

print('The length of myFriendsNameAndBounty', len(myFriendsNameAndBounty))

print('luffy in myFriendsNameAndBounty', 'luffy' in myFriendsNameAndBounty)
print('zoro not in myFriendsNameAndBounty', 'zoro' not in myFriendsNameAndBounty)

print(myFriendsNameAndBounty.keys())

print(myFriendsNameAndBounty.get('luffy'))
print(myFriendsNameAndBounty.get('zoro', 'not my friends'))

print('pop luffy', myFriendsNameAndBounty.pop('luffy'), myFriendsNameAndBounty)
