b = ['редиска']
a = 'Плохой человек - редиска'
a = a.lower()
print(a.split())
for i in a.split():
    if i in b:
        print("".join(f'{i[0]}***'))

if isinstance(a, str):
    print(a)