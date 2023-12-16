str1 = 'Hello'; print(str1,type(str1))
print(bool(True), bool(False))

str2 = '''
Hello my name is <xyz>. I'm python developer.
My hobbies are <coding, reading, gaming>.
I'm currentlyn learning data analysis using python.
'''
print(str2)

l1 = [1,1,3,2,5,1,3,5,1,89,4,12,45]
l1.append(49); print(l1)
l2 = []
[l2.append(i) for i in l1 if i not in l2]
print(l2)
l2.sort()
print(l2)
print(l2[::-1])