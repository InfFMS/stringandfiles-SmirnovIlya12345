# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
f = open('task1.txt', 'r', encoding='utf-8')
lines=[line for line in f]
print(len(lines))
a=0
b=''
for i in range(len(lines)):
    a+=len(lines[i])
    b+=lines[i]
print(b)
c=0
for i in range(a):
    if b[i]==' ':
        c+=1
print(c-len(lines))
print(a)
f.close()