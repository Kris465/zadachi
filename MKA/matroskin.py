'''
Кот Матроскин поймал несколько мышей, но решил отпустить часть из них. Сколько мышей у него осталось после этого? Введите количество пойманных мышей и количество отпущенных.
'''

poymal = int(input("Матроскин поймал: "))
otpustil = int(input("Сколько мышей отпустил Матроскин? "))
ostalos = poymal - otpustil
print("Осталось мышей: ", ostalos)