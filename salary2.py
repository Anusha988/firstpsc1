x = ['$876,001', '$543,903', '$253,896']
list=[]
for i in x:
    list.append(int("".join(i[1:].split(','))))
print(list)