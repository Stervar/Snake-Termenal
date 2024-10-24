
import sys
import time
import random
import curses
from curses import textpad

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Цвета
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

    # Размеры игрового поля
    sh, sw = stdscr.getmaxyx()
    w = sw - 2
    h = sh - 2

    # Создание границ
    box = [[1,1], [h, w]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    # Начальные параметры
    snake = [[sh//2, sw//2]]
    direction = curses.KEY_RIGHT
    apple = None
    score = 0
    start_time = time.time()
    difficulty = 1

    def create_apple():
        while True:
            apple = [random.randint(2, h-1), random.randint(2, w-1)]
            if apple not in snake:
                return apple

    def show_menu():
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        stdscr.addstr(h//2-2, w//2-4, "ЗМЕЙКА")
        stdscr.addstr(h//2, w//2-4, "1. Играть")
        stdscr.addstr(h//2+1, w//2-4, "2. Информация")
        stdscr.addstr(h//2+2, w//2-4, "3. Сложность")
        stdscr.addstr(h//2+3, w//2-4, "4. Выход")
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

    while True:
        action = show_menu()
        if action == 'play':
            break
        elif action == 'info':
            show_info()
        elif action == 'difficulty':
            set_difficulty()
        elif action == 'exit':
            sys.exit()

    while True:
        stdscr.clear()
        textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
        stdscr.addstr(0, 0, f"Счёт: {score} | Время: {int(time.time() - start_time)} сек.")
        stdscr.addstr(0, w-5, "Выход: Q")

        for y, x in snake:
            stdscr.addch(y, x, '#', curses.color_pair(1))

        if apple:
            stdscr.addch(apple[0], apple[1], '*', curses.color_pair(2))
        else:
            apple = create_apple()
            stdscr.addch(apple[0], apple[1], '*', curses.color_pair(2))

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_UP and direction != curses.KEY_DOWN:
            direction = curses.KEY_UP
        elif key == curses.KEY_DOWN and direction != curses.KEY_UP:
            direction = curses.KEY_DOWN
        elif key == curses.KEY_LEFT and direction != curses.KEY_RIGHT:
            direction = curses.KEY_LEFT
        elif key == curses.KEY_RIGHT and direction != curses.KEY_LEFT:
            direction = curses.KEY_RIGHT
        elif key == ord('w') and direction != curses.KEY_DOWN:
            direction = curses.KEY_UP
        elif key == ord('s') and direction != curses.KEY_UP:
            direction = curses.KEY_DOWN
        elif key == ord('a') and direction != curses.KEY_RIGHT:
            direction = curses.KEY_LEFT
        elif key == ord('d') and direction != curses.KEY_LEFT:
            direction = curses.KEY_RIGHT

        head = snake[0]
        if direction == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]

        snake.insert(0, new_head)

        if snake[0] in snake[1:]:
            stdscr.addstr(sh//2, sw//2 - 5, "Ты проиграл!")
            stdscr.refresh()
            time.sleep(2)
            break
        elif snake[0] == apple:
            score += 1
            apple = None
        else:
            snake.pop()

        if len(snake) == w * h:
            stdscr.addstr(sh//2, sw//2 - 5, "Вы победили!")
            stdscr.refresh()
            time.sleep(2)
            break

        time.sleep(0.1 / difficulty)

curses.wrapper(main)

# Описание:

# Импорт библиотек:
    
    
# Импорт библиотек:
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
#     stdscr.timeout(100)
#     "curs_set(0): скрывает курсор."
#     "nodelay(1): устанавливает неблокирующий режим ввода."
#     "timeout(100): устанавливает таймаут для getch() в 100 миллисекунд."

#     # Инициализация цветов:
#     curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
#     curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
#     curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
#     "Создаются три цветовые пары: зеленый на черном (для змейки), красный на черном (для яблока) и синий на черном."

#     # Определение размеров игрового поля:
#     sh, sw = stdscr.getmaxyx()
#     w = sw - 2
#     h = sh - 2
#     "getmaxyx() возвращает максимальные размеры экрана."
#     "w и h уменьшены на 2 для создания границ."

#     # Создание границ:
#     box = [[1,1], [h, w]]
#     textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
#     "Создается прямоугольник, определяющий границы игрового поля."

#     # Инициализация начальных параметров:
#     snake = [[sh//2, sw//2]]
#     direction = curses.KEY_RIGHT
#     apple = None
#     score = 0
#     start_time = time.time()
#     difficulty = 1
#     "snake: начальная позиция змейки (центр экрана)."
#     "direction: начальное направление движения (вправо)."
#     "apple: позиция яблока (изначально None)."
#     "score: начальный счет."
#     "start_time: время начала игры."
#     "difficulty: начальный уровень сложности."

#     # Вспомогательные функции:
#     def create_apple():
#         # ...
#     def show_menu():
#         # ...
#     def show_info():
#         # ...
#     def set_difficulty():
#         # ...
#     "create_apple(): генерирует новую позицию для яблока."
#     "show_menu(): отображает главное меню и обрабатывает выбор пользователя."
#     "show_info(): показывает информацию об игре."
#     "set_difficulty(): позволяет пользователю выбрать уровень сложности."

#     # Главный цикл меню:
#     while True:
#         action = show_menu()
#         if action == 'play':
#             break
#         elif action == 'info':
#             show_info ()
#         elif action == 'difficulty':
#             set_difficulty()

#     # Основной игровой цикл:
#     while True:
#         # Очищает экран и перерисовывает все элементы на каждой итерации.
#         # Обрабатывает ввод пользователя и изменяет направление движения змейки.
#         # Проверяет столкновения змейки с границами, яблоком и самой собой.
#         # Обновляет счет и время игры.

# # Запуск игры:
# curses.wrapper(main)
# "Запускает игру в безопасном режиме, чтобы предотвратить повреждение терминала."