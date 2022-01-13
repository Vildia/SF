"""Игра угадай число
компьютер сам загадывает и сам угадывает число
"""

import numpy as np
from numpy.random.mtrand import random

def random_predict(number: int=1) -> int:
    """Угадываем число ограничивая рамки подбора
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 
    
    min, max = 1, 100
    predict_number = max / 2
    
    while number != predict_number:
        count+=1
        # меняем минимум и максимум
        if number > predict_number: 
            min = predict_number + 1
        
        elif number < predict_number: 
            max = predict_number - 1
        
        predict_number = round((max + min ) / 2) # разбиваем по полам новые рамки поиска
        
            
    return(count)


def score_game(random_predict) ->int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм 

    Args:
        random_predict ([type]): функция угадывания
    
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадываем список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return(score)


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
 