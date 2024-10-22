import sys
import time
import random
import curses
from curses import textpad

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(50)

    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

    # Initial parameters
    direction = curses.KEY_RIGHT
    score = 0
    start_time = time.time()
    difficulty = 1
    map_size = 'medium'

    def create_apple(snake, box):
        while True:
            apple = [random.randint(box[0][0] + 1, box[1][0] - 1), random.randint(box[0][1] + 1, box[1][1] - 1)]
            if apple not in snake:
                return apple

    def show_menu():
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        stdscr.addstr(h//2-3, w//2-4, "ЗМЕЙКА")
        stdscr.addstr(h//2, w//2-4, "1. Играть")
        stdscr.addstr(h//2+1, w//2-4, "2. Информация")
        stdscr.addstr(h//2+2, w//2-4, "3. Сложность")
        stdscr.addstr(h//2+3, w//2-4, "4. Размер карты")
        stdscr.addstr(h//2+4, w//2-4, "5. Выход")
        stdscr.refresh()

        while True:
            key = stdscr.getch()
            if key == ord('1'):
                return 'play'
            elif key == ord('2'):
                return 'info'
            elif key == ord('3'):
                return 'difficulty'
            elif key == ord('4'):
                return 'map_size'
            elif key == ord('5'):
                return 'exit'

    def show_info():
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        info = [
            "Игра 'Змейка'",
            "Разработчик: Stervar",
            "Описание: Классическая игра 'Змейка'.",
            "Управление: W/↑ - вверх, S/↓ - вниз,",
            "A/← - влево, D/→ - вправо",
            "",
            "Нажмите любую клавишу для возврата в меню"
        ]
        for i, line in enumerate(info):
            stdscr.addstr(h//2 - len(info)//2 + i, w//2 - len(line)//2, line)
        stdscr.refresh()
        stdscr.getch()

    def set_difficulty():
        nonlocal difficulty
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        stdscr.addstr(h//2-2, w//2-8, "Выберите сложность:")
        stdscr.addstr(h//2, w//2-8, "1. Легко")
        stdscr.addstr(h//2+1, w//2-8, "2. Средне")
        stdscr.addstr(h//2+2, w//2-8, "3. Сложно")
        stdscr.refresh()

        while True:
            key = stdscr.getch()
            if key == ord('1'):
                difficulty = 1
                return
            elif key == ord('2'):
                difficulty = 1.5
                return
            elif key == ord('3'):
                difficulty = 2
                return

    def set_map_size():
        nonlocal map_size
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        stdscr.addstr(h//2-2, w//2-10, "Выберите размер карты:")
        stdscr.addstr(h//2, w//2-10, "1. Маленькая")
        stdscr.addstr(h//2+1, w//2-10, "2. Средняя")
        stdscr.addstr(h//2+2, w//2-10, "3. Большая")
        stdscr.refresh()

        while True:
            key = stdscr.getch()
            if key == ord('1'):
                map_size = 'small'
                return
            elif key == ord('2'):
                map_size = 'medium'
                return
            elif key == ord('3'):
                map_size = 'large'
                return

    while True:
        action = show_menu()
        if action == 'play':
            break
        elif action == 'info':
            show_info()
        elif action == 'difficulty':
            set_difficulty()
        elif action == 'map_size':
            set_map_size()
        elif action == 'exit':
            sys.exit()

    if map_size == 'small':
        sh, sw = 20, 40
    elif map_size == 'medium':
        sh, sw = 30, 60
    else:
        sh, sw = 40, 80

    w = sw - 2
    h = sh - 2

    box = [[1, 1], [h, w]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    snake = [[sh//2, sw//2]]
    apple = create_apple(snake, box)
    big_apple = create_apple(snake, box)
    last_move_time = time.time()

    while True:
        current_time = time.time()
        stdscr.clear()
        textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
        stdscr.addstr(0, 0, f"Счёт: {score} | Время: {int(current_time - start_time)} сек.")
        stdscr.addstr(0, w-5, "Выход: Q")

        for y, x in snake:
            stdscr.addch(y, x, '#', curses.color_pair(1))

        stdscr.addch(apple[0], apple[1], '*', curses.color_pair(2))
        stdscr.addch(big_apple[0], big_apple[1], '*', curses.color_pair(3))

        stdscr.refresh()

        key = stdscr.getch()
        if key != -1:
            if key == ord('q'):
                break
            elif key in [curses.KEY_UP, ord('w')] and direction != curses.KEY_DOWN:
                direction = curses.KEY_UP
            elif key in [curses.KEY_DOWN, ord('s')] and direction != curses.KEY_UP:
                direction = curses.KEY_DOWN
            elif key in [curses.KEY_LEFT, ord('a')] and direction != curses.KEY_RIGHT:
                direction = curses.KEY_LEFT
            elif key in [curses.KEY_RIGHT, ord('d')] and direction != curses.KEY_LEFT:
                direction = curses.KEY_RIGHT

        if current_time - last_move_time > 0.1 / difficulty:
            last_move_time = current_time
            head = snake[0]
            if direction == curses.KEY_UP:
                new_head = [head[0] - 1, head[1]]
                time.sleep(0.01)  # Add a small delay for vertical movement
            elif direction == curses.KEY_DOWN:
                new_head = [head[0] + 1, head[1]]
                time.sleep(0.01)  # Add a small delay for vertical movement
            elif direction == curses.KEY_LEFT:
                new_head = [head[0], head[1] - 1]
            elif direction == curses.KEY_RIGHT:
                new_head = [head[0], head[1] + 1]

            if new_head[0] < box[0][0] + 1:
                new_head[0] = box[1][0] - 1
            elif new_head[0] > box[1][0] - 1:
                new_head[0] = box[0][0] + 1
            if new_head[1] < box[0][1] + 1:
                new_head[1] = box[1][1] - 1
            elif new_head[1] > box[1][1] - 1:
                new_head[1] = box[0][1] + 1

            snake.insert(0, new_head)

            if snake[0] in snake[1:]:
                stdscr.addstr(sh//2, sw//2 - 5, "Ты проиграл!")
                stdscr.refresh()
                time.sleep(2)
                break
            elif snake[0] == apple:
                score += 1
                apple = create_apple(snake, box)
            elif snake[0] == big_apple:
                score += 2
                big_apple = create_apple(snake, box)
            else:
                snake.pop()

        if len(snake) == w * h:
            stdscr.addstr(sh//2, sw//2 - 5, "Вы победили!")
            stdscr.refresh()
            time.sleep(2)
            break

curses.wrapper(main)

# Описание


# # Импорт библиотек:
# import sys
# import time
# import random
# import curses
# from curses import textpad
# "sys: используется для выхода из программы (sys.exit())."
# "time: для измерения времени игры и создания задержек."
# "random: для генерации случайных позиций яблока."
# "curses: основная библиотека для создания текстового интерфейса."
# "textpad: модуль curses для создания текстовых полей и рамок."

# # Определение главной функции:
# def main(stdscr):
#     "stdscr - это стандартный экран, предоставляемый curses."
#     "Вся логика игры находится внутри этой функции."

#     # Настройка curses:
#     curses.curs_set(0)
#     stdscr.nodelay(1)
#     stdscr.timeout(50)
#     "curs_set(0): скрывает курсор."
#     "nodelay(1): устанавливает неблокирующий режим ввода."
#     "timeout(50): устанавливает таймаут для getch() в 50 миллисекунд."

#     # Инициализация цветов:
#     curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
#     curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
#     curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
#     "Создаются три цветовые пары: зеленый на черном (для змейки), красный на черном (для обычного яблока), синий на черном (для большого яблока)."

#     # Инициализация начальных параметров:
#     direction = curses.KEY_RIGHT
#     score = 0
#     start_time = time.time()
#     difficulty = 1
#     map_size = 'medium'
#     "direction: начальное направление движения (вправо)."
#     "score: начальный счет."
#     "start_time: время начала игры."
#     "difficulty: начальный уровень сложности."
#     "map_size: начальный размер карты."

#     # Вспомогательные функции:
#     def create_apple(snake, box):
#         # ...
#     def show_menu():
#         # ...
#     def show_info():
#         # ...
#     def set_difficulty():
#         # ...
#     def set_map_size():
#         # ...
#     "create_apple(): генерирует новую позицию для яблока."
#     "show_menu(): отображает главное меню и обрабатывает выбор пользователя."
#     "show_info(): показывает информацию об игре."
#     "set_difficulty(): позволяет пользователю выбрать уровень сложности."
#     "set_map_size(): позволяет пользователю выбрать размер карты."

#     # Главный цикл меню:
#     while True:
#         action = show_menu()
#         if action == 'play':
#             break
#         elif action == 'info':
#             show_info()
#         elif action == 'difficulty':
#             set_difficulty()
#         elif action == 'map_size':
#             set_map_size()
#         elif action == 'exit':
#             sys.exit()
#     "Отображает меню и обрабатывает выбор пользователя до начала игры."

#     # Настройка размера карты:
#     if map_size == 'small':
#         sh, sw = 20, 40
#     elif map_size == 'medium':
#         sh, sw = 30, 60
#     else:
#         sh, sw = 40, 80
#     "Устанавливает размеры карты в зависимости от выбора пользователя."

#     w = sw - 2
#     h = sh - 2
#     "Устанавливает внутренние размеры карты."

#     box = [[1, 1], [h, w]]
#     textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
#     "Создает рамку для карты."

#     snake = [[sh//2, sw//2]]
#     apple = create_apple(snake, box)
#     big_apple = create_apple(snake, box)
#     last_move_time = time.time()
#     "Инициализирует змейку, яблоко и большое яблоко."

#     # Основной игровой цикл:
#     while True:
#         # Очищает экран и перерисовывает все элементы на каждой итерации.
#         # Обрабатывает ввод пользователя и изменяет направление движения змейки.
#         # Проверяет столкновения змейки с границами, яблоком и самой собой.
#         # Обновляет счет и время игры.

#         current_time = time.time()
#         stdscr.clear()
#         textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
#         stdscr.addstr(0, 0, f"Счёт: {score} | Время: {int(current_time - start_time)} сек.")
#         stdscr.addstr(0, w-5, "Выход: Q")

#         for y, x in snake:
#             stdscr.addch(y, x, '#', curses.color_pair(1))

#         stdscr.addch(apple[0], apple[1], '*', curses.color_pair(2))
#         stdscr.addch(big_apple[0], big_apple[1], '*', curses.color_pair(3))

#         stdscr.refresh()

#         key = stdscr.getch()
#         if key != -1:
#             if key == ord('q'):
#                 break
#             elif key in [curses.KEY_UP, ord('w')] and direction != curses.KEY_DOWN:
#                 direction = curses.KEY_UP
#             elif key in [curses.KEY_DOWN, ord('s')] and direction != curses.KEY_UP:
#                 direction = curses.KEY_DOWN
#             elif key in [curses.KEY_LEFT, ord('a')] and direction != curses.KEY_RIGHT:
#                 direction = curses.KEY_LEFT
#             elif key in [curses.KEY_RIGHT, ord('d')] and direction != curses.KEY_LEFT:
#                 direction = curses.KEY_RIGHT

#         if current_time - last_move_time > 0.1 / difficulty:
#             last_move_time = current_time
#             head = snake[0]
#             if direction == curses.KEY_UP:
#                 new_head = [head[0] - 1, head[1]]
#                 time.sleep(0.01)  # Add a small delay for vertical movement
#             elif direction == curses.KEY_DOWN:
#                 new_head = [head[0] + 1, head[1]]
#                 time.sleep(0.01)  # Add a small delay for vertical movement
#             elif direction == curses.KEY_LEFT:
#                 new_head = [head[0], head[1] - 1]
#             elif direction == curses.KEY_RIGHT:
#                 new_head = [head[0], head[1] + 1]

#             if new_head[0] < box[0][0] + 1:
#                 new_head[0] = box[1][0] - 1
#             elif new_head[0] > box[1][0] - 1:
#                 new_head[0] = box[0][0] + 1
#             if new_head[1] < box[0][1] + 1:
#                 new_head[1] = box[1][1] - 1
#             elif new_head[1] > box[1][1] - 1:
#                 new_head[1] = box[0][1] + 1

#             snake.insert(0, new_head)

#             if snake[0] in snake[1:]:
#                 stdscr.addstr(sh//2, sw//2 - 5, "Ты проиграл!")
#                 stdscr.refresh()
#                 time.sleep(2)
#                 break
#             elif snake[0] == apple:
#                 score += 1
#                 apple = create_apple(snake, box)
#             elif snake[0] == big_apple:
#                 score += 2
#                 big_apple = create_apple(snake, box)
#             else:
#                 snake.pop()

#         if len(snake) == w * h:
#             stdscr.addstr(sh//2, sw//2 - 5, "Вы победили!")
#             stdscr.refresh()
#             time.sleep (2)
#             break

# # Запуск игры:
# curses.wrapper(main)
# "Запускает игру в безопасном режиме, чтобы предотвратить повреждение терминала."