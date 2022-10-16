#Ввод отношений критериев в матрицу
def inMatrix(mat, n):
    #Ввод отношений для верхней половины матрицы, считая от главной диагонали
    for i in range(n):
        for j in range(n):
            if (i == j):
                mat[i][j] = 1 
            if (i < j):
                while mat[i][j] == 0: 
                    temp = input(f"Введите отношение критерия {i+1} к критерию {j+1} ")
                    temp = errorCheck(temp)
                    if  (temp > 9) or (temp < 1): 
                        print('Отношение должно быть целым числом от 1 до 9')
                    else:
                        mat[i][j] = temp
    #Подстановка обратных значений для нижней части матрицы
    for i in range(n):
        for j in range(n):
            if (i > j):
                mat[i][j] = 1/mat[j][i]
    return mat

#Вывод матрицы отношений
def outMatrix(mat, n):
    for i in range(n):
        for j in range(n):
            print("{0:.2f}".format(mat[i][j]), end=" ")
        print()

#Cуммирование всех элементов матрицы
def matrixSum(mat, n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += mat[i][j]
    return sum

#Расчёт весовых коэффициентов
def koef(mat,n,sum):
    st  = []
    #расчёт суммы отношений для каждого отдельного критерия
    for i in range(n):
        sum1=0
        for j in range(n):
            sum1 += mat[j][i]
        st.append(sum1/sum)
    return st

#Проверка на ошибочный ввод
def errorCheck(n):
    try:
        n = int(n)
    except Exception:
        return -1
    return n

n = 0
#Ввод количества критериев
while n == 0: 
    n = input("Введите количество критериев: ")
    n = errorCheck(n)
    if (n < 1):
        print("Ошибка ввода - количество критериев должно быть положительным целым числом")
        n = 0
mass = [[0] * n for i in range(n)] # Создание двумерного массива 
mass = inMatrix(mass, n)
print("\nМатрица попарного сравнения: ")
outMatrix(mass, n)
mass_sum = matrixSum(mass, n)
print("\nСумма элементов матрицы: {0:.2f}".format(mass_sum))
koef1 = koef(mass, n, mass_sum) #Создание массива, хранящего весовые коэффициенты
koef1.reverse()
print("Весовые коэффициенты:", end=" ")
for elem in koef1:
    print("{0:.2f}".format(elem), end=" ") 
