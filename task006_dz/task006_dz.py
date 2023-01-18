# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

s = 'пра прабв огнр длорпабвовгв зщзыфшвщ вфыыабвгыоы абвывовдлыф"'.split()
print(s)
result = filter(lambda x: "а" not in x or "б" not in x or "в" not in x, s)
print(*result)
