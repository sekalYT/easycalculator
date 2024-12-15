import numpy as np

def multiply_matrices():
    print("\nУмножение матриц")
    # Ввод размеров первой матрицы
    rows1 = int(input("Введите количество строк первой матрицы: "))
    cols1 = int(input("Введите количество столбцов первой матрицы: "))
    
    # Ввод первой матрицы
    print("Введите элементы первой матрицы:")
    matrix1 = []
    for i in range(rows1):
        row = list(map(float, input().split()))
        matrix1.append(row)
    
    # Ввод размеров второй матрицы
    rows2 = int(input("Введите количество строк второй матрицы: "))
    cols2 = int(input("Введите количество столбцов второй матрицы: "))
    
    if cols1 != rows2:
        print("Умножение невозможно! Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")
        return
    
    # Ввод второй матрицы
    print("Введите элементы второй матрицы:")
    matrix2 = []
    for i in range(rows2):
        row = list(map(float, input().split()))
        matrix2.append(row)
    
    # Умножение матриц
    result = np.dot(matrix1, matrix2)
    print("\nРезультат умножения матриц:")
    print(result)

def diagonal_method(matrix):
    if len(matrix) != 2:
        return "Диагональный метод применим только для матриц 2x2"
    
    # Для матрицы 2x2:
    # | a b |
    # | c d |
    # Определитель = ad - bc
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]



def calculate_determinant():
    print("\nВычисление определителя матрицы")
    n = int(input("Введите размер квадратной матрицы: "))
    print("Введите элементы матрицы:")
    matrix = []
    for i in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    # Метод 1: Диагональный метод
    det1 = diagonal_method(matrix)
    print(f"\n1. Диагональный метод: {det1}")

    # Метод 2: Метод Саррюса
    if n == 3:
        det2 = (matrix[0][0] * matrix[1][1] * matrix[2][2] + 
                matrix[0][1] * matrix[1][2] * matrix[2][0] + 
                matrix[0][2] * matrix[1][0] * matrix[2][1] - 
                matrix[0][2] * matrix[1][1] * matrix[2][0] - 
                matrix[0][0] * matrix[1][2] * matrix[2][1] - 
                matrix[0][1] * matrix[1][0] * matrix[2][2])
        print(f"2. Метод Саррюса: {det2}")
    else:
        print("2. Метод Саррюса применим только для матрицы 3x3")

    # Метод 3: Метод Лапласа (миноров)
    def get_minor(matrix, i, j):
        return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
    
    def laplace_method(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        det = 0
        for j in range(len(matrix)):
            det += ((-1) ** j) * matrix[0][j] * laplace_method(get_minor(matrix, 0, j))
        return det
    
    det3 = laplace_method(matrix)
    print(f"3. Метод Лапласа (миноров): {det3}")

    # Метод 4: Метод элементарных преобразований
    det4 = np.linalg.det(matrix)
    print(f"4. Метод элементарных преобразований: {det4}")


def calculate_rank():
    print("\nВычисление ранга матрицы")
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    
    print("Введите элементы матрицы:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    # Преобразуем в numpy массив
    matrix = np.array(matrix)
    
    # Вычисляем ранг
    rank = np.linalg.matrix_rank(matrix)
    
    print(f"\nРанг матрицы: {rank}")
    
    # Дополнительная информация о матрице
    print(f"Размерность матрицы: {rows}x{cols}")
    if rank == min(rows, cols):
        print("Матрица имеет полный ранг")
    else:
        print("Матрица имеет неполный ранг")
    
    # Показываем ступенчатый вид матрицы (метод Гаусса)
    matrix_rref = matrix.copy()
    
    # Приведение к ступенчатому виду
    for i in range(min(rows, cols)):
        # Находим максимальный элемент в текущем столбце
        pivot = abs(matrix_rref[i:, i]).argmax() + i
        
        # Меняем строки местами
        if pivot != i:
            matrix_rref[[i, pivot]] = matrix_rref[[pivot, i]]
        
        # Если ведущий элемент не нулевой
        if matrix_rref[i, i] != 0:
            # Нормализуем строку
            matrix_rref[i] = matrix_rref[i] / matrix_rref[i, i]
            
            # Вычитаем из всех остальных строк
            for j in range(rows):
                if j != i:
                    matrix_rref[j] -= matrix_rref[j, i] * matrix_rref[i]
    
    print("\nСтупенчатый вид матрицы:")
    print(matrix_rref)
    
    # Проверка линейной зависимости строк/столбцов
    if rank < rows:
        print(f"Имеется {rows - rank} линейно зависимых строк")
    if rank < cols:
        print(f"Имеется {cols - rank} линейно зависимых столбцов")

def check_system_compatibility():
    print("\nИсследование СЛАУ на совместность и определенность")
    n = int(input("Введите количество уравнений: "))
    m = int(input("Введите количество неизвестных: "))
    
    print("\nВведите уравнения в формате: коэффициенты = свободный_член")
    print("Пример: 1 2 1 = 4 для уравнения 1x₁ + 2x₂ + 1x₃ = 4")
    
    extended_matrix = []
    for i in range(n):
        while True:
            try:
                # Разбиваем ввод на части до и после =
                equation = input(f"Уравнение {i+1}: ").split('=')
                if len(equation) != 2:
                    print("Ошибка: используйте формат 'коэффициенты = свободный_член'")
                    continue
                
                # Получаем коэффициенты и свободный член
                coefficients = list(map(float, equation[0].strip().split()))
                free_term = float(equation[1].strip())
                
                # Дополняем нулями, если коэффициентов меньше, чем неизвестных
                while len(coefficients) < m:
                    coefficients.append(0.0)
                
                # Если коэффициентов больше, чем неизвестных
                if len(coefficients) > m:
                    print(f"Ошибка: введено слишком много коэффициентов. Нужно {m}")
                    continue
                
                # Добавляем свободный член
                coefficients.append(free_term)
                extended_matrix.append(coefficients)
                break
            except ValueError:
                print("Ошибка: введите числа, разделенные пробелами")
    
    # Преобразуем в numpy массивы
    extended_matrix = np.array(extended_matrix)
    matrix = extended_matrix[:, :-1]  # матрица коэффициентов (без свободных членов)
    
    # Вычисляем ранги
    rank_matrix = np.linalg.matrix_rank(matrix)
    rank_extended = np.linalg.matrix_rank(extended_matrix)
    
    print("\nМатрица коэффициентов:")
    print(matrix)
    print("\nРасширенная матрица:")
    print(extended_matrix)
    
    print(f"\nРанг основной матрицы: {rank_matrix}")
    print(f"Ранг расширенной матрицы: {rank_extended}")
    
    if rank_matrix != rank_extended:
        print("Система несовместна (нет решений)")
    elif rank_matrix == rank_extended == m:
        print("Система определена (единственное решение)")
    elif rank_matrix == rank_extended < m:
        print("Система неопределена (бесконечно много решений)")
    else:
        print("Система несовместна (противоречивая)")

def gauss_method():
    print("\nРешение СЛАУ методом Гаусса")
    n = int(input("Введите количество уравнений: "))
    m = int(input("Введите количество неизвестных: "))
    
    print("\nВведите уравнения в формате: коэффициенты = свободный_член")
    print("Пример: 1 2 1 = 4 для уравнения 1x₁ + 2x₂ + 1x₃ = 4")
    
    matrix = []
    for i in range(n):
        while True:
            try:
                equation = input(f"Уравнение {i+1}: ").split('=')
                if len(equation) != 2:
                    print("Ошибка: используйте формат 'коэффициенты = свободный_член'")
                    continue
                
                coefficients = list(map(float, equation[0].strip().split()))
                free_term = float(equation[1].strip())
                
                while len(coefficients) < m:
                    coefficients.append(0.0)
                
                if len(coefficients) > m:
                    print(f"Ошибка: введено слишком много коэффициентов. Нужно {m}")
                    continue
                
                coefficients.append(free_term)
                matrix.append(coefficients)
                break
            except ValueError:
                print("Ошибка: введите числа, разделенные пробелами")
    
    matrix = np.array(matrix, dtype=float)
    
    print("\nНачальная расширенная матрица:")
    print(matrix)
    
    # Прямой ход метода Гаусса
    for i in range(min(n, m)):
        # Поиск максимального элемента в столбце для частичного выбора главного элемента
        max_element = abs(matrix[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_element:
                max_element = abs(matrix[k][i])
                max_row = k
        
        # Перестановка строк
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row].copy(), matrix[i].copy()
        
        # Если ведущий элемент близок к нулю, пропускаем
        if abs(matrix[i][i]) < 1e-10:
            continue
        
        # Нормализация строки
        matrix[i] = matrix[i] / matrix[i][i]
        
        # Вычитание из остальных строк
        for j in range(n):
            if i != j:
                matrix[j] = matrix[j] - matrix[i] * matrix[j][i]
    
    print("\nМатрица после прямого хода:")
    print(matrix)
    
    # Проверка на совместность и определенность
    rank_matrix = np.linalg.matrix_rank(matrix[:, :-1])
    rank_extended = np.linalg.matrix_rank(matrix)
    
    if rank_matrix != rank_extended:
        print("\nСистема несовместна (нет решений)")
        return
    elif rank_matrix < m:
        print("\nСистема имеет бесконечно много решений")
        return
    
    # Получение решения
    solution = matrix[:, -1][:m]
    print("\nРешение системы:")
    for i, x in enumerate(solution):
        print(f"x{i+1} = {x:.4f}")

def cramer_method():
    print("\nРешение СЛАУ методом Крамера")
    n = int(input("Введите количество уравнений: "))
    m = int(input("Введите количество неизвестных: "))
    
    if n != m:
        print("Метод Крамера применим только для систем с равным количеством уравнений и неизвестных!")
        return
    
    print("\nВведите уравнения в формате: коэффициенты = свободный_член")
    print("Пример: 1 2 1 = 4 для уравнения 1x₁ + 2x₂ + 1x₃ = 4")
    
    # Матрица коэффициентов A и вектор свободных членов b
    A = []
    b = []
    
    for i in range(n):
        while True:
            try:
                equation = input(f"Уравнение {i+1}: ").split('=')
                if len(equation) != 2:
                    print("Ошибка: используйте формат 'коэффициенты = свободный_член'")
                    continue
                
                coefficients = list(map(float, equation[0].strip().split()))
                free_term = float(equation[1].strip())
                
                while len(coefficients) < m:
                    coefficients.append(0.0)
                
                if len(coefficients) > m:
                    print(f"Ошибка: введено слишком много коэффициентов. Нужно {m}")
                    continue
                
                A.append(coefficients)
                b.append(free_term)
                break
            except ValueError:
                print("Ошибка: введите числа, разделенные пробелами")
    
    A = np.array(A)
    b = np.array(b)
    
    print("\nМатрица коэффициентов A:")
    print(A)
    print("\nВектор свободных членов b:")
    print(b)
    
    # Вычисление определителя основной матрицы
    det_A = np.linalg.det(A)
    
    if abs(det_A) < 1e-10:  # Проверка на близость к нулю
        print("\nОпределитель основной матрицы равен нулю!")
        print("Система не имеет единственного решения")
        return
    
    # Вычисление решений по формулам Крамера
    solution = []
    for i in range(n):
        # Создаем копию матрицы A для замены i-го столбца
        A_i = A.copy()
        # Заменяем i-й столбец вектором свободных членов
        A_i[:, i] = b
        # Вычисляем определитель модифицированной матрицы
        det_i = np.linalg.det(A_i)
        # Находим i-ю неизвестную
        x_i = det_i / det_A
        solution.append(x_i)
    
    print("\nОпределитель основной матрицы:")
    print(f"det(A) = {det_A:.4f}")
    
    print("\nРешение системы:")
    for i, x in enumerate(solution):
        print(f"x{i+1} = {x:.4f}")
        print(f"det{i+1} = {np.linalg.det(A_i):.4f}")

def solve_matrix_laplace():  # для 7 задания
    print("\nРешение матрицы методом Лапласа")
    print("Введите размерность матрицы nxm в формате: n m")
    try:
        n, m = map(int, input("Размерность: ").split())
    except ValueError:
        print("Ошибка: введите два числа через пробел")
        return

    print("\nВведите элементы матрицы построчно")
    print("Пример для матрицы 2x2:")
    print("1 2")
    print("3 4")
    
    matrix = []
    for i in range(n):
        while True:
            try:
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != m:
                    print(f"Ошибка: строка должна содержать {m} чисел")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Ошибка: введите числа, разделенные пробелами")

    print("\nВведенная матрица:")
    for row in matrix:
        print(row)

    def get_minor(matrix, i, j):
        return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
    
    def determinant(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        det = 0
        for j in range(len(matrix)):
            det += ((-1) ** j) * matrix[0][j] * determinant(get_minor(matrix, 0, j))
        return det

    if n != m:
        print("\nДля вычисления определителя матрица должна быть квадратной!")
        return

    result = determinant(matrix)
    print(f"\nОпределитель матрицы: {result}")

    # Дополнительная информация о миноре каждого элемента
    print("\nМиноры элементов:")
    for i in range(n):
        for j in range(n):
            minor = get_minor(matrix, i, j)
            minor_det = determinant(minor) if n > 1 else "не существует"
            print(f"Минор элемента [{i+1},{j+1}] = {minor_det}")


def main():
    while True:
        print("\nВыберите операцию:")
        print("1 - Калькулятор умножения матриц")
        print("2 - Вычислить определитель матрицы")
        print("3 - Найти ранг матрицы")
        print("4 - Исследование СЛАУ на совместность и определенность")
        print("5 - Решение СЛАУ методом Гаусса")
        print("6 - Решение СЛАУ методом Крамера")
        print("7 - Решение матрицы методом Лапласа")
        print("0 - Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == '0':
            break
        elif choice == '1':
            multiply_matrices()
        elif choice == '2':
            calculate_determinant()
        elif choice == '3':
            calculate_rank()
        elif choice == '4':
            check_system_compatibility()
        elif choice == '5':
            gauss_method()
        elif choice == '6':
            cramer_method()
        elif choice == '7':
            solve_matrix_laplace()
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()