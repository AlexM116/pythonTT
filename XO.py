def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Проверка строк
    for row in board:
        if all([spot == player for spot in row]):
            return True
    # Проверка столбцов
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Проверка диагоналей
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def is_full(board):
    return all([spot != " " for row in board for spot in row])


def tic_tac_toe():
    # Пустое поле 3x3
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Начинаем с игрока X

    while True:
        print_board(board)
        try:
            # Ввод строки и столбца от текущего игрока
            row = int(input(f"Игрок {current_player}, введите номер строки (0, 1 или 2): "))
            col = int(input(f"Игрок {current_player}, введите номер столбца (0, 1 или 2): "))

            # Корректность ввода
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Неверный ввод. Введите значения от 0 до 2.")
                continue

            # Свободна ли ячейка
            if board[row][col] == " ":
                board[row][col] = current_player
                # Победитель после каждого хода
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Игрок {current_player} победил!")
                    break
                # Проверка на ничью
                elif is_full(board):
                    print_board(board)
                    print("Ничья!")
                    break
                # Меняем текущего игрока
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Эта ячейка уже занята. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число от 0 до 2.")


# Запуск игры
tic_tac_toe()