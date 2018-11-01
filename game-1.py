import random
x50 = '*'*51
x3 = '*'*3
print(x50)
print(x3 + '\t Сыграем в камень-ножницы-бумагу\t' + x3)
print(x3+'\t\t\t\t\t\t'+x3)
print(x50)
print(x3 + '\t\t Играем 3 раза. \t\t' + x3)
print(x3 + '\t[k] камень, [n] ножницы, [b] бумага\t'+x3)
player_score = 0
comp_score = 0

for i in range(3):
    print(x50)
    print(x3 + f"\t\t\tРаунд {i+1}\t\t\t" + x3)
    comp_select = random.choice('knb')
    print(x3+'\t\t\t\t\t\t'+x3)
    while True:
        player_select = input(x3 +"\tВаш выбор [k], [n], [b]: ")
        if player_select == 'n' or player_select == 'k' or player_select == 'b':
            break
        else:
            print(x3+"\tНекорректный выбор. Попробуйте еще.\t"+x3)
    print(x3+'\t\t\t\t\t\t'+x3)
    print(x3 + '\t\tВыбор ПК:'+comp_select+'\t\t\t'+x3)
    print(x3+'\t\t\t\t\t\t'+x3)
    if comp_select == player_select:
        print(x3 + '\t\t\tНичья\t\t\t' +x3)
    elif comp_select == 'k' and player_select == 'b':
        print(x3 + '\t\tРаунд за вами\t\t\t' +x3)
        player_score += 1
    elif comp_select == 'k' and player_select == 'n':
        print(x3 + '\t\tРаунд за компьютером\t\t' +x3)
        comp_score += 1
    elif comp_select == 'n' and player_select == 'k':
        print(x3 + '\t\tРаунд за вами\t\t\t' +x3)
        player_score += 1
    elif comp_select == 'n' and player_select == 'b':
        print(x3 + '\t\tРаунд за компьютером\t\t' +x3)
        comp_score += 1
    elif comp_select == 'b' and player_select == 'k':
        print(x3 + '\t\tРаунд за компьютером\t\t' +x3)
        comp_score += 1
    elif comp_select == 'b' and player_select == 'n':
        print(x3 + '\t\tРаунд за вами\t\t\t' +x3)
        player_score += 1
print(x3+'\t\t\t\t\t\t'+x3)
print(x50)
print(x3+'\t\t\t\t\t\t'+x3)
print(x3+'\t\tРЕЗУЛЬТАТ ИГРЫ\t\t\t'+x3)
print(x3+'\t\t\t\t\t\t'+x3)
if player_score > comp_score:
    print(x3+'\t\tВы выиграли!\t\t\t'+x3)
elif player_score < comp_score:
    print(x3+'\t\tПобеда за ПК!\t\t\t'+x3)
else:
    print(x3 + '\t\t\tНичья\t\t\t' +x3)
print(x3+'\t\t\t\t\t\t'+x3)
print(x50)
