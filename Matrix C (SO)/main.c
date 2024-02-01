#include <stdio.h>
#include <stdlib.h>
#define SIZE 800  //Размерность матрицы

int main()
{
    //matrix1 - первая матрица, matrix2 - вторая матрица, ResultMatrix - результирующая матрица
    int matrix1[SIZE][SIZE], matrix2[SIZE][SIZE], ResultMatrix[SIZE][SIZE];
    int i = 0, j = 0, sum = 0;  //i и j - переменные-счётчики, sum - для перемножения матриц
    FILE *file; //Указатель на файл с данными

    file = fopen("data.txt", "r");  //Открытие файла для чтения данных

    //Заполенение матриц числами
    for(i = 0; i < SIZE; i++)
        for(j = 0; j < SIZE; j++)
        {
            //Считывание символов из файла и преобразование их в цифры
            matrix1[i][j] = fgetc(file) - 48;
            matrix2[j][i] = matrix1[i][j];
        }

    fclose(file);   //Закрытие файла

    //==========  Перемножение матриц ==========
    for (i = 0; i < SIZE; i++)
       {
            for (j = 0; j < SIZE; j++)
            {
                sum = 0;
                for(int k = 0; k < SIZE; k++)
                {
                    sum = sum + matrix1[i][k] * matrix2[k][j];
                }
                ResultMatrix[i][j] = sum;
            }
       }
    //==========================================

    return 0;
}
