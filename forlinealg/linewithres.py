import numpy as np

def multiply_matrices():
    print("\nУмножение матриц")
    rows1 = int(input("Введите количество строк первой матрицы: "))
    cols1 = int(input("Введите количество столбцов первой матрицы: "))
    
    print("Введите элементы первой матрицы:")
    matrix1 = []
    for i in range(rows1):
        row = list(map(float, input().split()))
        matrix1.append(row)
    
    print("\nПервая матрица:")
    for row in matrix1:
        print(row)
    
    rows2 = int(input("\nВведите количество строк второй матрицы: "))
    cols2 = int(input("Введите количество столбцов второй матрицы: "))
    
    if cols1 != rows2:
        print("Умножение невозможно! Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")
        return
    
    print("Введите элементы второй матрицы:")
    matrix2 = []
    for i in range(rows2):
        row = list(map(float, input().split()))
        matrix2.append(row)
    
    print("\nВторая матрица:")
    for row in matrix2:
        print(row)
    
    # Пошаговое умножение
    result = np.zeros((rows1, cols2))
    print("\nПошаговое вычисление:")
    for i in range(rows1):
        for j in range(cols2):
            sum_elem = 0
            print(f"\nВычисление элемента [{i+1},{j+1}]:")
            for k in range(cols1):
                product = matrix1[i][k] * matrix2[k][j]
                sum_elem += product
                print(f"({matrix1[i][k]} × {matrix2[k][j]}) + ", end="")
            print(f"\b\b= {sum_elem}")
            result[i][j] = sum_elem
    
    print("\nИтоговый результат умножения матриц:")
    print(result)

def calculate_determinant():
    print("\nВычисление определителя матрицы")
    n = int(input("Введите размер квадратной матрицы: "))
    print("Введите элементы матрицы:")
    matrix = []
    for i in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    print("\nИсходная матрица:")
    for row in matrix:
        print(row)
    
    if n == 2:
        print("\nРешение для матрицы 2×2:")
        a, b = matrix[0][0], matrix[0][1]
        c, d = matrix[1][0], matrix[1][1]
        print(f"det = {a} × {d} - {b} × {c}")
        det = a*d - b*c
        print(f"det = {a*d} - {b*c} = {det}")
        
    elif n == 3:
        print("\nМетод Саррюса для матрицы 3×3:")
        # Положительные члены
        print("Положительные члены:")
        term1 = matrix[0][0] * matrix[1][1] * matrix[2][2]
        print(f"{matrix[0][0]} × {matrix[1][1]} × {matrix[2][2]} = {term1}")
        term2 = matrix[0][1] * matrix[1][2] * matrix[2][0]
        print(f"{matrix[0][1]} × {matrix[1][2]} × {matrix[2][0]} = {term2}")
        term3 = matrix[0][2] * matrix[1][0] * matrix[2][1]
        print(f"{matrix[0][2]} × {matrix[1][0]} × {matrix[2][1]} = {term3}")
        
        print("\nОтрицательные члены:")
        term4 = matrix[0][2] * matrix[1][1] * matrix[2][0]
        print(f"{matrix[0][2]} × {matrix[1][1]} × {matrix[2][0]} = {term4}")
        term5 = matrix[0][0] * matrix[1][2] * matrix[2][1]
        print(f"{matrix[0][0]} × {matrix[1][2]} × {matrix[2][1]} = {term5}")
        term6 = matrix[0][1] * matrix[1][0] * matrix[2][2]
        print(f"{matrix[0][1]} × {matrix[1][0]} × {matrix[2][2]} = {term6}")
        
        det = term1 + term2 + term3 - term4 - term5 - term6
        print(f"\nОпределитель = ({term1} + {term2} + {term3}) - ({term4} + {term5} + {term6}) = {det}")

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
                coefficients = list(map(float, equation[0].strip().split()))
                free_term = float(equation[1].strip())
                coefficients.append(free_term)
                matrix.append(coefficients)
                break
            except ValueError:
                print("Ошибка: введите числа, разделенные пробелами")
    
    matrix = np.array(matrix, dtype=float)
    print("\nНачальная расширенная матрица:")
    print(matrix)
    
    # Прямой ход
    print("\nПрямой ход метода Гаусса:")
    for i in range(min(n, m)):
        print(f"\nШаг {i+1}:")
        
        # Выбор главного элемента
        max_element = abs(matrix[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_element:
                max_element = abs(matrix[k][i])
                max_row = k
        
        if max_row != i:
            print(f"Меняем местами строки {i+1} и {max_row+1}")
            matrix[i], matrix[max_row] = matrix[max_row].copy(), matrix[i].copy()
            print("Текущая матрица:")
            print(matrix)
        
        if abs(matrix[i][i]) < 1e-10:
            continue
        
        # Нормализация строки
        div = matrix[i][i]
        print(f"Делим строку {i+1} на {div}")
        matrix[i] = matrix[i] / div
        print(matrix)
        
        # Вычитание из остальных строк
        for j in range(n):
            if i != j:
                factor = matrix[j][i]
                print(f"Вычитаем из строки {j+1} строку {i+1}, умноженную на {factor}")
                matrix[j] = matrix[j] - matrix[i] * factor
                print("Текущая матрица:")
                print(matrix)
    
    print("\nМатрица после прямого хода:")
    print(matrix)
    
    # Проверка на совместность и определенность
    rank_matrix = np.linalg.matrix_rank(matrix[:, :-1])
    rank_extended = np.linalg.matrix_rank(matrix)
    
    print(f"\nРанг основной матрицы: {rank_matrix}")
    print(f"Ранг расширенной матрицы: {rank_extended}")
    
    if rank_matrix != rank_extended:
        print("Система несовместна (нет решений)")
        return
    elif rank_matrix < m:
        print("Система имеет бесконечно много решений")
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
    A = []
    b = []
    
    for i in range(n):
        equation = input(f"Уравнение {i+1}: ").split('=')
        coefficients = list(map(float, equation[0].strip().split()))
        free_term = float(equation[1].strip())
        A.append(coefficients)
        b.append(free_term)
    
    A = np.array(A)
    b = np.array(b)
    
    print("\nМатрица коэффициентов A:")
    print(A)
    print("\nВектор свободных членов b:")
    print(b)
    
    # Вычисление главного определителя
    det_A = np.linalg.det(A)
    print(f"\nГлавный определитель системы = {det_A:.4f}")
    
    if abs(det_A) < 1e-10:
        print("Система не имеет единственного решения (определитель равен 0)")
        return
    
    # Вычисление определителей для каждой переменной
    solution = []
    for i in range(n):
        # Создаем копию матрицы A
        A_i = A.copy()
        # Заменяем i-й столбец вектором b
        A_i[:, i] = b
        
        print(f"\nМатрица для x{i+1}:")
        print(A_i)
        det_i = np.linalg.det(A_i)
        print(f"Определитель для x{i+1} = {det_i:.4f}")
        
        # Вычисляем значение переменной
        x_i = det_i / det_A
        print(f"x{i+1} = {det_i:.4f} / {det_A:.4f} = {x_i:.4f}")
        solution.append(x_i)

        print("\nИтоговое решение системы:")
    for i, x in enumerate(solution):
        print(f"x{i+1} = {x:.4f}")
    
    # Проверка решения
    print("\nПроверка решения:")
    for i in range(n):
        result = sum(A[i][j] * solution[j] for j in range(n))
        print(f"Уравнение {i+1}: ", end="")
        for j in range(n):
            if j > 0:
                print(" + ", end="")
            print(f"({A[i][j]:.2f} × {solution[j]:.4f})", end="")
        print(f" = {result:.4f} ≈ {b[i]:.4f}")

def calculate_rank():
    print("\nВычисление ранга матрицы")
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    
    print("Введите элементы матрицы:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    matrix = np.array(matrix)
    print("\nИсходная матрица:")
    print(matrix)
    
    # Метод Гаусса для нахождения ранга
    matrix_copy = matrix.copy()
    rank = 0
    rows, cols = matrix_copy.shape
    
    print("\nПреобразование матрицы к ступенчатому виду:")
    for i in range(min(rows, cols)):
        # Поиск ненулевого элемента в текущем столбце
        pivot_row = -1
        for j in range(i, rows):
            if abs(matrix_copy[j, i]) > 1e-10:
                pivot_row = j
                break
                
        if pivot_row == -1:
            print(f"Столбец {i+1} полностью нулевой")
            continue
            
        # Перестановка строк
        if pivot_row != i:
            print(f"Меняем местами строки {i+1} и {pivot_row+1}")
            matrix_copy[[i, pivot_row]] = matrix_copy[[pivot_row, i]]
            print("Текущая матрица:")
            print(matrix_copy)
        
        # Обнуление элементов под главным элементом
        for j in range(i + 1, rows):
            if abs(matrix_copy[j, i]) > 1e-10:
                factor = matrix_copy[j, i] / matrix_copy[i, i]
                print(f"Вычитаем из строки {j+1} строку {i+1}, умноженную на {factor:.4f}")
                matrix_copy[j] -= factor * matrix_copy[i]
                print("Текущая матрица:")
                print(matrix_copy)
        
        rank += 1
    
    print(f"\nРанг матрицы: {rank}")
    
    # Дополнительная информация
    print("\nАнализ матрицы:")
    if rank == min(rows, cols):
        print("Матрица имеет полный ранг")
    else:
        print("Матрица имеет неполный ранг")
    
    if rank < rows:
        print(f"Количество линейно зависимых строк: {rows - rank}")
    if rank < cols:
        print(f"Количество линейно зависимых столбцов: {cols - rank}")

def check_system_compatibility():
    print("\nИсследование СЛАУ на совместность и определенность")
    n = int(input("Введите количество уравнений: "))
    m = int(input("Введите количество неизвестных: "))
    
    print("\nВведите уравнения в формате: коэффициенты = свободный_член")
    print("Пример: 1 2 1 = 4 для уравнения 1x₁ + 2x₂ + 1x₃ = 4")
    
    extended_matrix = []
    print("\nВвод системы уравнений:")
    for i in range(n):
        while True:
            try:
                equation = input(f"Уравнение {i+1}: ").split('=')
                coefficients = list(map(float, equation[0].strip().split()))
                free_term = float(equation[1].strip())
                
                # Вывод уравнения в красивом формате
                print(f"Уравнение {i+1} в математической форме:")
                eq_str = ""
                for j, coef in enumerate(coefficients):
                    if j > 0:
                        eq_str += " + " if coef >= 0 else " - "
                        eq_str += f"{abs(coef)}x{j+1}"
                    else:
                        eq_str += f"{coef}x{j+1}"
                print(f"{eq_str} = {free_term}")
                
                coefficients.append(free_term)
                extended_matrix.append(coefficients)
                break
            except ValueError:
                print("Ошибка: введите числа, разделенные пробелами")
    
    extended_matrix = np.array(extended_matrix)
    matrix = extended_matrix[:, :-1]
    
    print("\nМатрица коэффициентов:")
    print(matrix)
    print("\nРасширенная матрица:")
    print(extended_matrix)
    
    # Вычисление рангов
    rank_matrix = np.linalg.matrix_rank(matrix)
    rank_extended = np.linalg.matrix_rank(extended_matrix)
    
    print(f"\nРанг матрицы коэффициентов: {rank_matrix}")
    print(f"Ранг расширенной матрицы: {rank_extended}")
    
    # Анализ совместности и определенности
    print("\nАнализ системы:")
    if rank_matrix != rank_extended:
        print("Система несовместна (нет решений)")
        print("Причина: ранг матрицы коэффициентов не равен рангу расширенной матрицы")
    else:
        print("Система совместна")
        if rank_matrix == m:
            print("Система определена (имеет единственное решение)")
            print(f"Причина: ранг матрицы ({rank_matrix}) равен числу неизвестных ({m})")
        else:
            print("Система неопределена (имеет бесконечно много решений)")
            print(f"Причина: ранг матрицы ({rank_matrix}) меньше числа неизвестных ({m})")
            print(f"Степень неопределенности: {m - rank_matrix}")
    
    # Дополнительный анализ
    if n > m:
        print("\nСистема переопределена (уравнений больше, чем неизвестных)")
    elif n < m:
        print("\nСистема недоопределена (уравнений меньше, чем неизвестных)")
    else:
        print("\nКоличество уравнений равно количеству неизвестных")

def main_menu():
    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print("1. Умножение матриц")
        print("2. Вычисление определителя матрицы")
        print("3. Вычисление ранга матрицы")
        print("4. Исследование СЛАУ на совместность")
        print("5. Решение СЛАУ методом Гаусса")
        print("6. Решение СЛАУ методом Крамера")
        print("0. Выход")
        
        choice = input("\nВыберите операцию (0-6): ")
        
        try:
            if choice == '0':
                print("\nПрограмма завершена.")
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
            else:
                print("\nОшибка: выберите число от 0 до 6")
                
            input("\nНажмите Enter для продолжения...")
            
        except Exception as e:
            print(f"\nПроизошла ошибка: {str(e)}")
            input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    print("Программа для работы с матрицами и решения СЛАУ")
    main_menu()