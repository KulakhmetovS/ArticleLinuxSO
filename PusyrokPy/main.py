from random import randint  #Импорт функции для псевдорандома
import time #Импорт модуля для замеров времени

N = 250 #Число элементов
tmp = 0 #Переменная для хранения промежуточного значения
array = [0] * N #Сортируемый массив
string = str()  #Строка для считывания данных из файла
file = open('data.txt', 'w')    #Открытие файла для записи данных

#Заполнение файла псевдорадномными числами
for i in range(N):
    file.write(str(randint(0, 9)))

file.close()    #Закрытие файла

start_time = time.time()    #Начало замеров времени с учётом чтения данных из файла

file = open('data.txt', 'r')    #Открытие файла для чтения данных
string = file.read()    #Считывание данных из файла в специальную строку
file.close()    #Закрытие файла

#Преобразование строки данных в массив чисел
for i in range(N):
        array[i] = int(string[i])

#Сортировка пузырьком
for i in range(N-1):
    for j in range(N-i-1):
        if array[j] > array[j+1]:
            tmp = array[j]
            array[j] = array[j+1]
            array[j+1] = tmp

end_time = time.time()  #Конец замеров времени с учётом чтения данных из файла
execution_time = end_time - start_time  #Время работы алгоритма

print('Время выполнения программы: ', execution_time)