from ctypes import *    #Импорт модуля для работы с динамической библиотекой
from random import randint  #Импорт функции для псевдорандома
import time #Импорт модуля для замеров времени
Matrix_Multiplication = CDLL('./main.so')

N = 800 #Размерность матрицы

file = open('data.txt', 'w')    #Открытие файла для записи данных

#Заполнение файла псевдорадномными числами
for i in range(N * N):
    file.write(str(randint(0, 9)))

file.close()    #Закрытие файла

start_time = time.time()    #Начало замеров времени с учётом чтения данных из файла
Matrix_Multiplication.main()
end_time = time.time()  #Конец замеров времени с учётом чтения данных из файла

execution_time = end_time - start_time  #Время работы алгоритма

print('Время выполнения программы: ', execution_time)