import pandas as pd

friend_name = ["Fakeoo", "Anonymoose", "Jesus"]
friend_birthday = ["01/01/1899", "02/01/2022", "00/00/00"]
print("P1.14")
df = pd.DataFrame({'friend_name':friend_name, 'friend_birthday':friend_birthday})
print(df)

'''
friend_name_series = pd.Series(friend_name)
friend_name_birthday = pd.Series(friend_birthday)

for birthday in zip(friend_birthday):
    print(birthday)
for name in zip(friend_name):
    print(name)
'''   
print("-----------")
print("-----------")
print("-----------")



