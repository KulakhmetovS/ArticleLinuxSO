#include <stdio.h>
#include <stdlib.h>
#define SIZE 100 //Число элементов сортируемого массива

int main()
{
    FILE *file = NULL;  //Указатель на файл с исходными данными
    //array - сортируемый массив данных; i - переменная-счётчик; tmp - переменная для обмена значениями
    int array[SIZE], i = 0, tmp = 0;

    file = fopen("data.txt", "r");  //Открытие файла с данными

    for(i = 0; i < SIZE; i++)
    {
        array[i] = fgetc(file); //Чтение данных из файла
        array[i] = array[i] - 48;   //Преобразование UTF-8 в int
    }

    fclose(file);   //Закрытие файла с данными

    //========== Сортировка пузырьком ==========
    for(i = 0; i < SIZE - 1; i++)
        for(int j = 0; j < SIZE - i - 1; j++)
            if(array[j] > array[j + 1])
            {
                tmp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = tmp;
            }
    //==========================================

    return 0;
}
