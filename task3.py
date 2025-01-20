# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
f=open('task3.txt', 'r', encoding='utf-8')
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
        if b[j]==' ' or b[j]=='.':
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
f3=sorted(f2)
f4=[]
for i in range(len(f3)-1):
    for j in range(i+1,len(f3)-1):
        if f3[i]!=f3[j]:
            f4.append(str(f3[i]))
            f4.append(str(j-i))
            break
with open('12345.txt', 'w', encoding='utf-8') as g:
    for s in [f4]:
        g.write(str(s))
