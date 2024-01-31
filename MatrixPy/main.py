from random import randint  #Импорт функции для псевдорандома
import time #Импорт модуля для замеров времени

N =  #Число элементов
k = int(0)  #Дополнительная переменная-счётчик
sum = int(0)    #Переменна для перемножения матриц
matrix1 = [0] * N   #Первая матрица
matrix2 = [0] * N   #Вторая матрица
ResultMatrix = [0] * N  #Результирующая матрица
for i in range(N):
    matrix1[i] = [0] * N
    matrix2[i] = [0] * N
    ResultMatrix[i] = [0] * N
string = str()  #Строка для считывания данных из файла
file = open('data.txt', 'w')    #Открытие файла для записи данных

#Заполнение файла псевдорадномными числами
for i in range(N * N):
    file.write(str(randint(0, 9)))

file.close()    #Закрытие файла

start_time = time.time()    #Начало замеров времени с учётом чтения данных из файла

file = open('data.txt', 'r')    #Открытие файла для чтения данных
string = file.read()    #Считывание данных из файла в специальную строку
file.close()    #Закрытие файла

#Заполнение матриц считанными данными
for i in range(N):
    for j in range(N):
        matrix1[i][j] = int(string[k])
        matrix2[j][i] = matrix1[i][j]
        k+=1

#Перемеожение матриц
for i in range(N):
    for j in range(N):
        sum = 0
        for k in range(N):
            sum = sum + matrix1[i][k] * matrix2[k][j]
        ResultMatrix[i][j] = sum

end_time = time.time()  #Конец замеров времени с учётом чтения данных из файла
execution_time = end_time - start_time  #Время работы алгоритма

print('Время выполнения программы: ', execution_time)
