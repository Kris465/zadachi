'''
Смешарики собрали определенное количество морковок и решили поделить их между собой. Сколько морковок получит каждый друг, если они поделят их поровну? Введите общее количество морковок и количество друзей.
'''

morkovok = int(input("Сколько морковок? "))
druzey = int(input("Сколько друзей? "))
na_druga = morkovok // druzey
print(na_druga, "морковок на каждого друга")
