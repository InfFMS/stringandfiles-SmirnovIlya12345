# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
f=open('task5.txt', 'r', encoding='utf-8')
lines=[line for line in f]
a=0
b=''
for j in range(len(lines)):
    a+=len(lines[j])
    b+=lines[j]
c=''
d=0
e=[]
for i in range(a):
    for j in range(i, a):
        if b[j]==' ' or b[j]=='.' or b[j]=='!':
            e.append(b[d:j])
            d=j
            break
f=[]
for i in range(len(e)):
    if e[i]!='' and e[i]!=' ' and e[i]!='.':
        f.append(e[i])
f2=[]
for i in range(len(f)):
    if f[i][0]==' ':
        f[i]=f[i][1::]
    if f[i][0]=='\n':
        f[i]=f[i][1::]
    f2.append(f[i].lower())
l=0
l2=''
for i in range(len(f2)):
    if len(f2[i])>l:
        l=len(f2[i])
        l2=f2[i]
with open('1234567.txt', 'w', encoding='utf-8') as g:
    for s in [l2, '\n', str(l)]:
        g.write(s)
print(l2,l)
