from random import choice

ans = input('Поиграем? y/n ')
kards = [11, 6, 7, 8, 9, 10, 2, 3, 4] *4

ans1 = 'y'
ans2 = 'y'

def add_beauty(input_func):
    def wrapper(*args, **kwargs):
        print('●•٠·˙˙·٠•●♥ Ƹ̵̡Ӝ̵̨̄Ʒ ♥●•٠·˙˙·٠•●')
        print()
        input_func(*args, **kwargs)
        print()
        print('●•٠·˙˙·٠•●♥ Ƹ̵̡Ӝ̵̨̄Ʒ ♥●•٠·˙˙·٠•●')
    return wrapper

summ_p1 = 0 #сумма очков певого игрока
summ_p2 = 0 #сумма очков второго игрока
count_tuz = 0

def choice_kard():  
    '''Выбор случайной карты из колоды. Карта удаляется из списка'''
    kard = choice(kards) 
    kards.remove(kard)
    return kard

@add_beauty
def summ_22(player): 
    '''у игрока два туза подряд'''
    print(f'{player}, Вы выиграли - два туза подряд!!! Пора за лотерейным билетом')

@add_beauty
def get_result(*,total_1, total_2, a, b):
    if 21 > total_1 > total_2:
        '''победа, но у игрока нет 21'''
        print(f'{a}, у Вас {total_1} очков!Победа!!!')
        print(f'{b}, у Вас {total_2} очков!Вы проиграли(')
    elif total_1 == 21:
        '''сумма очков у игрокa a = 21'''
        print(f'{a}, Победа! Очко!!!')
        print(f'{b}, у Вас {total_2} очков!Вы проиграли(')
    elif total_1 > 21:    
        '''Сумма очков у игрока a > 21'''
        print(f'{a} Вы проиграли - у Вас {total_1} очков - перебор(')  
        print('Повезет в следующий раз')
        print(f'{b}, Победа! У соперника перебор!!!')


def one_more_card(player, kard, total):  #Запрос дополнительной карты
    print(f'{player}, Ваша карта {kard}. Итого у Вас {total} очков!')
    return input('Еще карту? y/n ')

if ans == 'y':

    player1 = input('Как Вас зовут?  ') #имя первого игрока
    player2 = input('Как Вас зовут?  ') #имя второго игрока    

    while ans1 == 'y' and ans2 == 'y':
   
        pl_1 = choice_kard()
        pl_2 = choice_kard()
        
        count_tuz += 1 #переменная будет считаться всегда, надо считать ее только две первые итерации, в дальнейшем она просто является лишним действием
        summ_p1 += pl_1
        summ_p2 += pl_2

        if count_tuz == 2 and (summ_p1 == 22 or summ_p2 == 22):
            if summ_p1 == 22 and summ_p2 != 22:
                summ_22(player1)
                break
            elif summ_p2 == 22 and summ_p1 != 22:
                summ_22(player2)
                break
            else:
                print('●•٠·˙˙·٠•●♥ Ƹ̵̡Ӝ̵̨̄Ʒ ♥●•٠·˙˙·٠•●')
                print()
                print(f'{player1} и {player2}, вы победители!!! Четыре туза на двоих!!! Вау!!!')
                print()
                print('●•٠·˙˙·٠•●♥ Ƹ̵̡Ӝ̵̨̄Ʒ ♥●•٠·˙˙·٠•●')
                break

        if summ_p1 == summ_p2 == 21:
            print('●•٠·˙˙·٠•●♥ Ƹ̵̡Ӝ̵̨̄Ʒ ♥●•٠·˙˙·٠•●')
            print()
            print(f'Ничья! {player1} и {player2}, Вы выиграли - у каждого 21 очко!')
            print()
            print('●•٠·˙˙·٠•●♥ Ƹ̵̡Ӝ̵̨̄Ʒ ♥●•٠·˙˙·٠•●')
            break
        elif summ_p1 > 20:
            get_result(total_1=summ_p1,total_2=summ_p2, a=player1, b=player2)
            break
        elif summ_p2 > 20:
            get_result(total_1=summ_p2,total_2=summ_p1, a=player2, b=player1)
            break
        ans1 = one_more_card(player1, pl_1, summ_p1)
        ans2 = one_more_card(player2, pl_2, summ_p2)
    else:
        while ans1 == 'y' and ans2 == 'n':
            pl_1 = choice_kard() 
            summ_p1 += pl_1
            if summ_p1 >20:
                get_result(total_1=summ_p1,total_2=summ_p2, a=player1, b=player2)
                break
            ans1 = one_more_card(player1, pl_1, summ_p1)
        else:
            while ans1 == 'n' and ans2 == 'y':
                pl_2 = choice_kard() 
                summ_p2 += pl_2 
                if summ_p2 > 20:
                    get_result(total_1=summ_p2,total_2=summ_p1, a=player2, b=player1)
                    break
                ans2 = one_more_card(player2, pl_2, summ_p2)

        if ans1 == 'n' and ans2 == 'n':
            if summ_p1 > summ_p2:
                get_result(total_1=summ_p1, total_2=summ_p2, a=player1, b=player2)
            elif summ_p1 < summ_p2: 
                get_result(total_1=summ_p2, total_2=summ_p1, a=player2, b=player1)
            else:
                print('●•٠·˙˙·٠•●♥ Ƹ̵̡Ӝ̵̨̄Ʒ ♥●•٠·˙˙·٠•●')
                print()
                print(f'Ничья! {player1} и {player2}, Вы выиграли - у каждого {summ_p1} очко(в)!')
                print()
                print('●•٠·˙˙·٠•●♥ Ƹ̵̡Ӝ̵̨̄Ʒ ♥●•٠·˙˙·٠•●')
            
    if (ans1 not in ('y', 'n')) or (ans2 not in ('y', 'n')):
        print('Что-то пошло не так.')  

elif ans == 'n':
    print('До свидания') 
else:
    print('Что-то пошло не так.')        