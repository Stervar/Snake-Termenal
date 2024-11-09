# curses: для создания текстового интерфейса в терминале

import curses

# time: для работы со временем

import time

# random: для генерации случайных чисел

import random

# sys: для системных функций

import sys

# textpad: модуль из curses для рисования прямоугольников

from curses import textpad






def animation_loading(animation):

# loading_text: ASCII-арт логотип игры, представленный списком строк.

    loading_text = [
        "   _____             _         _____                      ",
        "  / ____|           | |       / ____|                     ",
        " | (___   __ _ _ __ | |_ ___ | |  __  __ _ _ __ ___   ___ ",
        "  \\___ \\ / _` | '_ \\| __/ _ \\| | |_ |/ _` | '_ ` _ \\ / _ \\",
        "  ____) | (_| | | | | ||  __/| |__| | (_| | | | | | |  __/ ",
        " |_____/ \\__,_|_| |_|\\__\\___| \\_____|\\__,_|_| |_| |_|\\___| "
    ]

# game_title: Название игры на русском языке.

    game_title = "Игра про змейку высшего уровня"

# stdscr.clear(): Очищает экран.

    animation.clear()

# curses.curs_set(0): Скрывает курсор.

    curses.curs_set(0)

# stdscr.nodelay(1): Устанавливает неблокирующий режим ввода.

    animation.nodelay(1)

# start_time = time.time(): Запоминает время начала анимации.

    start_time = time.time()

# animation_duration = 5: Устанавливает длительность анимации в секундах.

    animation_duration = 5

    while True:

        animation.clear()

        elapsed_time = time.time() - start_time

# Вычисляет прогресс анимации: progress = elapsed_time / animation_duration.

        progress = elapsed_time / animation_duration
        
        if progress <= 1:

            for i, line in enumerate(loading_text):

                visible_chars = int(len(line) * progress)

# Использует stdscr.addstr() для вывода текста на экран.

                animation.addstr(animation.getmaxyx()[0] // 2 - len(loading_text) // 2 + i,
                            animation.getmaxyx()[1] // 2 - len(line) // 2,
                            line[:visible_chars])
            
            bar_length = 30
            filled_length = int(bar_length * progress)

# Рисует прогресс-бар, заполняя его символами '█'.

            bar = '█' * filled_length + '-' * (bar_length - filled_length)
            y = animation.getmaxyx()[0] // 2 + len(loading_text) // 2 + 2
            x = animation.getmaxyx()[1] // 2 - bar_length // 2

            if y >= 0 and y < animation.getmaxyx()[0] and x >= 0 and x < animation.getmaxyx()[1]:
                animation.addstr(y, x, f"[{bar}] {int(progress * 100)}%")

        else:
            for i, line in enumerate(loading_text):

                animation.addstr(animation.getmaxyx()[0] // 2 - len(loading_text) // 2 + i,
                            animation.getmaxyx()[1] // 2 - len(line) // 2,
                            line)
                
# После 50% прогресса начинает отображать название игры.

        if progress > 0.5:

            title_progress = (progress - 0.5) * 2
            visible_title_chars = int(len(game_title) * title_progress)

            y = animation.getmaxyx()[0] - 2
            x = animation.getmaxyx()[1] // 2 - len(game_title) // 2

            if y >= 0 and y < animation.getmaxyx()[0] and x >= 0 and x < animation.getmaxyx()[1]:

# Использует stdscr.addstr() для вывода текста на экран.
               
                animation.addstr(y, x, game_title[:visible_title_chars])
        
# Проверяет границы экрана перед выводом, чтобы избежать ошибок.

        if progress > 1:

            animation.refresh()

            time.sleep(1)

            break

# time.sleep(0.05): Контролирует скорость анимации.   
     
        time.sleep(0.05)

        animation.refresh()

# Основное меню
def show_menu(stdscr): 

    stdscr.clear()

    h, w = stdscr.getmaxyx()

# Проверяет размер окна терминала: if h < 20 or w < 60.

    if h < 20 or w < 60:

        stdscr.addstr(0, 0, "Пожалуйста, измените размер окна терминала.")

        stdscr.refresh()

        stdscr.getch()

        sys.exit()

# Название игры
    title = [
        "   _____             _         _____                      ",
        "  / ____|           | |       / ____|                     ",
        " | (___   __ _ _ __ | |_ ___ | |  __  __ _ _ __ ___   ___ ",
        "  \\___ \\ / _` | '_ \\| __/ _ \\| | |_ |/ _` | '_ ` _ \\ / _ \\",
        "  ____) | (_| | | | | ||  __/| |__| | (_| | | | | | |  __/ ",
        " |_____/ \\__,_|_| |_|\\__\\___| \\_____|\\__,_|_| |_| |_|\\___| "
    ]
    for i, line in enumerate(title):

# Центрирует все элементы меню с помощью расчетов:

        y = h // 2 - len(title) - 8 + i
        x = max(0, w // 2 - len(line) // 2)

        if y >= 0 and y < h and x >= 0 and x < w:
            stdscr.addstr(y, x, line)

    subtitle = "Игра про змейку которая была улучшина 'Sterva'"

    y = h // 2 - len(title) - 1
    x = max(0, w // 2 - len(subtitle) // 2)

    if y >= 0 and y < h and x >= 0 and x < w:
        stdscr.addstr(y, x, subtitle)

    # Отображает главное меню с 6 пунктами.

    menu_items = [
        "╔═══════════════════════════════╗",
        "║       ● ГЛАВНОЕ МЕНЮ  ●       ║",
        "╠═══════════════════════════════╣",
        "║ • 1. Начать игру              ║",
        "║ • 2. Установить сложность     ║",
        "║ • 3. Установить размер карты  ║",
        "║ • 4. Количество яблок         ║",
        "║ • 5. Установить типы яблок    ║",
        "║ • 6. Выйти                    ║",
        "╚═══════════════════════════════╝"
    ]
    for i, line in enumerate(menu_items):

        y = h // 2 + i - 2  # Переместить пункты меню на 2 строки вверх
        x = max(0, w // 2 - len(line) // 2)

        if y >= 0 and y < h and x >= 0 and x < w:
            stdscr.addstr(y, x, line)

    # Показывает информационный блок с правилами игры.

    info_box = [
        "╔═══════════════════════════════════════╗",
        "║         Информация об игре            ║",
        "╠═══════════════════════════════════════╣",
        "║ Управление:                           ║",
        "║  • W/↑ - вверх,    • S/↓ - вниз       ║",
        "║  • A/← - влево,    • D/→ - вправо     ║",
        "║  • P - Пауза                          ║",
        "╠═══════════════════════════════════════╣",
        "║ Яблоки:                               ║",
        "║  • Обычное яблоко: +1 очко            ║",
        "║  • Большое яблоко: +2 очка            ║",
        "║  • Супер яблоко: +3 очка              ║",
        "║    (дает дополнительные очки)         ║",
        "╚═══════════════════════════════════════╝"
    ]
    for i, line in enumerate(info_box):

        y = h // 2 + len(menu_items) - 2 + i  # Переместите информационное окно на 2 строки вверх
        x = max(0, w // 2 - len(line) // 2)

        if y >= 0 and y < h and x >= 0 and x < w:

            stdscr.addstr(y, x, line)
            

    stdscr.refresh()
    

    while True:
        key = stdscr.getch ()

        if key == ord('1'):
            return 'play'
        
        elif key == ord('2'):
            return 'difficulty'
        
        elif key == ord('3'):
            return 'map_size'
        
        elif key == ord('4'):
            return 'apple_count'
        
        elif key == ord('5'):
            return 'apple_types'
        
        elif key == ord('6'):
            return 'exit'
        
# Отображает меню выбора сложности.

def set_difficulty(complexity):

    complexity.clear()

    h, w = complexity.getmaxyx()
    options = [
    "╔═══════════════════════════════╗",
    "║     Выберите сложность:       ║",
    "╠═══════════════════════════════╣",
    "║ • 1. Легко                    ║",
    "║ • 2. Средне                   ║",
    "║ • 3. Сложно                   ║",
    "╚═══════════════════════════════╝"
]

    for i, line in enumerate(options):

        complexity.addstr(h // 2 - len(options) // 2 + i, max(0, w // 2 - len(line) // 2), line)

    complexity.refresh()


    while True:

# Использует stdscr.getch() для получения выбора пользователя.
# Возвращает числовое значение сложности (1, 1.5 или 2).

        key = complexity.getch()

        if key == ord('1'):
            return 1
        
        elif key == ord('2'):
            return 1.5
        
        elif key == ord('3'):
            return 2

# Отображает меню выбора размера карты.

def set_map_size(map):

    map.clear()

    h, w = map.getmaxyx()
    options = [
    "╔═══════════════════════════════╗",
    "║   Выберите размер карты:      ║",
    "╠═══════════════════════════════╣",
    "║ • 1. Маленький                ║",
    "║ • 2. Средний                  ║",
    "║ • 3. Большой                  ║",
    "╚═══════════════════════════════╝"
]
    for i, line in enumerate(options):

        map.addstr(h // 2 - len(options) // 2 + i, max(0, w // 2 - len(line) // 2), line)

    map.refresh()

# Возвращает строку с выбранным размером ('small', 'medium', 'large').

    while True:

        key = map.getch()

        if key == ord('1'):
            return 'small'
        
        elif key == ord('2'):
            return 'medium'
        
        elif key == ord('3'):
            return 'large'

# Запрашивает у пользователя количество яблок.

def set_apple_count(apple_quantity):
    apple_quantity.clear()
    h, w = apple_quantity.getmaxyx()
    
    options = [
        "╔═══════════════════════════════╗",
        "║   Введите количество яблок:   ║",
        "╠═══════════════════════════════╣",
        "║    Используйте (1-10)         ║",
        "╚═══════════════════════════════╝"
    ]
    
    for i, line in enumerate(options):
        apple_quantity.addstr(h // 2 - len(options) // 2 + i, 
                            max(0, w // 2 - len(line) // 2), 
                            line)
    
    input_y = h // 2 - len(options) // 2 + len(options)
    input_x = w // 2
    
    apple_quantity.refresh()
    curses.curs_set(1)  # Показываем курсор
    
    count = ""
    while True:
        apple_quantity.addstr(input_y, input_x - 5, " " * 10)  # Очищаем строку ввода
        apple_quantity.addstr(input_y, input_x - 5, count)  # Показываем текущий ввод
        apple_quantity.move(input_y, input_x - 5 + len(count))  # Перемещаем курсор
        apple_quantity.refresh()
        
        key = apple_quantity.getch()
        
        if key == ord('\n'):  # Enter
            if count and 1 <= int(count) <= 10:
                curses.curs_set(0)  # Скрываем курсор
                return int(count)
            else:
                error_msg = "Ошибка! Введите число от 1 до 10"
                apple_quantity.addstr(input_y + 1, 
                                   max(0, w // 2 - len(error_msg) // 2), 
                                    error_msg)
                apple_quantity.refresh()
                apple_quantity.getch()  # Ждем нажатия любой клавиши
                apple_quantity.addstr(input_y + 1, 0, " " * w)  # Очищаем сообщение об ошибке
                count = ""  # Сбрасываем ввод
        elif key in [ord(str(i)) for i in range(10)]:  # Цифры
            if len(count) < 2:
                count += chr(key)
        elif key == 27:  # Escape
            curses.curs_set(0)  # Скрываем курсор
            return 2  # Возвращаем значение по умолчанию
        elif key in [8, 127]:  # Backspace
            count = count[:-1]

    
# Отображает меню выбора типов яблок.

def set_apple_types(apple_types):
    apple_types.clear()

    h, w = apple_types.getmaxyx()
    options = [
    "╔═══════════════════════════════╗",
    "║    Выберите типы яблок:       ║",
    "╠═══════════════════════════════╣",
    "║ • 1. Только обычные           ║",
    "║ • 2. Обычные и большие        ║",
    "║ • 3. Все типы (включая супер) ║",
    "╚═══════════════════════════════╝"
]

# Возвращает список выбранных типов яблок.

    for i, line in enumerate(options):

        apple_types.addstr(h // 2 - len(options) // 2 + i, max(0, w // 2 - len(line) // 2), line)

    apple_types.refresh()


    while True:

        key = apple_types.getch()

        if key == ord('1'):
            return [' normal']
        
        elif key == ord('2'):
            return ['normal', 'big']
        
        elif key == ord('3'):
            return ['normal', 'big', 'super']

# Генерирует список яблок заданного количества.

def create_apples(snake, box, apple_count, apple_types):

    apples = []

    for _ in range(apple_count):

# Использует вложенный цикл while для генерации уникальных позиций яблок.

        while True:

            apple = [random.randint(box[0][0] + 1, box[1][0] - 1), random.randint(box[0][1] + 1, box[1][1] - 1)]

# Проверяет, чтобы яблоки не появлялись на змейке или друг на друге. - Случайно выбирает тип каждого яблока из доступных типов.


            if apple not in snake and apple not in [a[0] for a in apples]:

                apple_type = random.choice(apple_types)

                apples.append((apple, apple_type))

                break

    return apples


def main(color):

    animation_loading(color)
    
# Инициализирует цветовые пары для curses.

    curses.curs_set(0)

    color.nodelay(1)

    color.timeout(50)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

# Инициализирует параметры игры (сложность, размер карты и т.д.).

    difficulty = 1

    map_size = 'medium'

    apple_count = 2

    apple_types = ['normal', 'big']

    while True:
        menu_choice = show_menu(color)
        if menu_choice == 'play':
            game_result = play_game(color, difficulty, map_size, apple_count, apple_types)
            if game_result == 'exit':
                return
        elif menu_choice == 'difficulty':
            difficulty = set_difficulty(color)
        elif menu_choice == 'map_size':
            map_size = set_map_size(color)
        elif menu_choice == 'apple_count':
            apple_count = set_apple_count(color)
        elif menu_choice == 'apple_types':
            apple_types = set_apple_types(color)
        elif menu_choice == 'exit':
            return
        
def play_game(color, difficulty, map_size, apple_count, apple_types):
    
# Создает игровое поле, змейку и яблоки.

    if map_size == 'small':
        box = [[2, 2], [20, 40]]

    elif map_size == 'medium':
        box = [[2, 2], [25, 50]]

    elif map_size == 'large':
        box = [[2, 2], [35, 80]]

    snake = [[box[0][0] + 2, box[0][1] + 2], [box[0][0] + 2, box[0][1] + 1]]

    apples = create_apples(snake, box, apple_count, apple_types)

    score = 0

    start_time = time.time()

    last_move_time = time.time()

    direction = curses.KEY_RIGHT

    paused = False

# Содержит основной игровой цикл:

    while True:
        current_time = time.time()

        color.clear()
        textpad.rectangle(color, box[0][0], box[0][1], box[1][0], box[1][1])
            # Создаем информационную строку
        score_info = f"Счет: {score}"
        time_info = f"Время: {int(current_time - start_time)} сек"
        control_info = "Выход: Q-Й | Пауза: P-З | Меню: M-Ь"

    # Вычисляем доступную ширину
        available_width = curses.COLS - 2  # -2 для учета боковых границ

    # Вычисляем ширину для каждой секции
        control_width = len(control_info)
        remaining_width = available_width - control_width
        score_width = remaining_width // 2
        time_width = remaining_width - score_width

    # Форматируем строки
        top_border = "╔" + "═" * available_width + "╗"
        info_line = f"║ {control_info:<{control_width}}{score_info:^{score_width}}{time_info:>{time_width}} ║"
        bottom_border = "╚" + "═" * available_width + "╝"

    # Отображаем информационную панель
        color.addstr(0, 0, top_border)
        color.addstr(1, 0, info_line)
        color.addstr(2, 0, bottom_border)

# Движение змейки.

        for i, (y, x) in enumerate(snake):
            if i == 0:
                color.addch(y, x, '۝', curses.color_pair(4))  # Голова змейки
            else:
                color.addch(y, x, 'o', curses.color_pair(1))  # Тело змейки


        for apple, apple_type in apples:

            if apple_type == 'normal':

                color.addch(apple[0], apple[1], '*', curses.color_pair(2))

            elif apple_type == 'big':
                color.addch(apple[0], apple[1], '*', curses.color_pair(3))

            elif apple_type == 'super':
                color.addch(apple[0], apple[1], '*', curses.color_pair(4))


        color.refresh()


        key = color.getch()
        if key != -1:
            if key in [ord('q'), ord('й'), ord('P'), ord('З')]:
                return 'exit'
            elif key in [ord('m'), ord('ь'), ord('M'), ord('Ь')]:
                return 'menu'
            elif key in [ord('p'), ord('з'), ord('Q'), ord('Й')]:
            
                paused = True
                
                while paused:
                    color.addstr(curses.LINES // 2, curses.COLS // 2 - 15, "╔═══════════════════════╗")
                    color.addstr(curses.LINES // 2 + 1, curses.COLS // 2 - 15, "║         ПАУЗА         ║")
                    color.addstr(curses.LINES // 2 + 2, curses.COLS // 2 - 15, "╠═══════════════════════╣",)
                    color.addstr(curses.LINES // 2 + 3, curses.COLS // 2 - 15,  "║  P/З - Продолжить     ║",)
                    color.addstr(curses.LINES // 2 + 4, curses.COLS // 2 - 15, "║  M/Ь - Главное меню   ║",)
                    color.addstr(curses.LINES // 2 + 5, curses.COLS // 2 - 15,"║  Q/Й - Выйти из игры  ║",)
                    color.addstr(curses.LINES // 2 + 6, curses.COLS // 2 - 15,"╚═══════════════════════╝")
                    color.refresh()

                    pause_key = color.getch()
                    if pause_key in [ord('p'), ord('з'), ord('P'), ord('З')]:
                        paused = False
                    elif pause_key in [ord('m'), ord('ь'), ord('M'), ord('Ь')]:
                        return 'menu'
                    elif pause_key in [ord('q'), ord('й'), ord('Q'), ord('Й')]:
                        return 'exit'




            elif key in [curses.KEY_UP, ord('w')] and direction != curses.KEY_DOWN:
                direction = curses.KEY_UP

            elif key in [curses.KEY_DOWN, ord('s')] and direction != curses.KEY_UP:
                direction = curses.KEY_DOWN

            elif key in [curses.KEY_LEFT, ord('a')] and direction != curses.KEY_RIGHT:
                direction = curses.KEY_LEFT

            elif key in [curses.KEY_RIGHT, ord('d')] and direction != curses.KEY_LEFT:
                direction = curses.KEY_RIGHT

            elif key in [curses.KEY_UP, ord('ц')] and direction != curses.KEY_DOWN:
                direction = curses.KEY_UP

            elif key in [curses.KEY_DOWN, ord('ы')] and direction != curses.KEY_UP:
                direction = curses.KEY_DOWN

            elif key in [curses.KEY_LEFT, ord('ф')] and direction != curses.KEY_RIGHT:
                direction = curses.KEY_LEFT

            elif key in [curses.KEY_RIGHT, ord('в')] and direction != curses.KEY_LEFT:
                direction = curses.KEY_RIGHT
            
            elif key in [curses.KEY_UP, ord('W')] and direction != curses.KEY_DOWN:
                direction = curses.KEY_UP

            elif key in [curses.KEY_DOWN, ord('S')] and direction != curses.KEY_UP:
                direction = curses.KEY_DOWN

            elif key in [curses.KEY_LEFT, ord('A')] and direction != curses.KEY_RIGHT:
                direction = curses.KEY_LEFT

            elif key in [curses.KEY_RIGHT, ord('D')] and direction != curses.KEY_LEFT:
                direction = curses.KEY_RIGHT
            
            elif key in [curses.KEY_UP, ord('Ц')] and direction != curses.KEY_DOWN:
                direction = curses.KEY_UP

            elif key in [curses.KEY_DOWN, ord('Ы')] and direction != curses.KEY_UP:
                direction = curses.KEY_DOWN

            elif key in [curses.KEY_LEFT, ord('Ф')] and direction != curses.KEY_RIGHT:
                direction = curses.KEY_LEFT

            elif key in [curses.KEY_RIGHT, ord('В')] and direction != curses.KEY_LEFT:
                direction = curses.KEY_RIGHT



        if current_time - last_move_time > 0.1 / difficulty and not paused:

            last_move_time = current_time

            head = snake[0]

            if direction == curses.KEY_UP:
                new_head = [head[0] - 1, head[1]]

            elif direction == curses.KEY_DOWN:
                new_head = [head[0] + 1, head[1]]

            elif direction == curses.KEY_LEFT:
                new_head = [head[0], head[1] - 1]

            elif direction == curses.KEY_RIGHT:
                new_head = [head[0], head[1] + 1]


            # Проверка столкновения с границей
            if new_head[0] < box[0][0] + 1:
                new_head[0] = box[1][0] - 1

            elif new_head[0] > box[1][0] - 1:
                new_head[0] = box[0][0] + 1
                
            if new_head[1] < box[0][1] + 1:
                new_head[1] = box[1][1] - 1

            elif new_head[1] > box[1][1] - 1:
                new_head[1] = box[0][1] + 1

            snake.insert(0, new_head)


            # Проверка столкновения с яблоком
            for apple, apple_type in apples:
                if snake[0] == apple:
                    if apple_type == 'super':
                        score += 3
                    elif apple_type == 'big':
                        score += 2
                    elif apple_type == 'normal':
                        score += 1  
                    apples.remove((apple, apple_type))
                    
                    # Респавн только съеденного яблока
                    while True:
                        new_apple = [
                            random.randint(box[0][0] + 1, box[1][0] - 1),
                            random.randint(box[0][1] + 1, box[1][1] - 1)
                            ]
                        if new_apple not in snake and new_apple not in [a[0] for a in apples]:
                            apples[i] = (new_apple, apple_type)
                            break
        

                    # Проверка типа яблока
                    if apple_type == 'super':
                        for _ in range(2):  # Добавляем три сегмента к змейке
                            new_head = snake[0]
                            snake.insert(0, new_head)
                            
                    if apple_type == 'big':
                        for _ in range(1):  # Добавляем два сегмента к змейке
                            new_head = snake[0]
                            snake.insert(0, new_head)
                            
                    if apple_type == 'normal':
                        for _ in range(0): #Добовляет один сегмент к змейки
                            new_head = snake[0]
                            snake.insert(0, new_head)
                            
                            
                            


                            # Проверка выхода за границы
                            if snake[0][0] < box[0][0] + 1:
                                snake[0][0] = box[1][0] - 1

                            elif snake[0][0] > box[1][0] - 1:
                                snake[0][0] = box[0][0] + 1

                            if snake[0][1] < box[0][1] + 1:
                                snake[0][1] = box[1][1] - 1

                            elif snake[0][1] > box[1][1] - 1:
                                snake[0][1] = box[0][1] + 1

                    apples = create_apples(snake, box, apple_count, apple_types)
                    break
            else:
                snake.pop()
                
                if snake[0] in snake[1:]:
                    game_over_result = show_game_over_screen(color, score)
                    if game_over_result == 'exit':
                        return 'exit'
                    elif game_over_result == 'restart':
                        return 'play'
                    elif game_over_result == 'menu':
                        return 'menu'
                else:
                    snake.pop()

        color.refresh()
def show_game_over_screen(color, score):
    h, w = color.getmaxyx()
    box_width = 33
    box_height = 9
    start_y = h // 2 - box_height // 2
    start_x = w // 2 - box_width // 2

    # Рамка
    color.addstr(start_y, start_x, "╔═══════════════════════════════╗")
    color.addstr(start_y + 1, start_x, "║          GAME OVER            ║")
    color.addstr(start_y + 2, start_x, "╠═══════════════════════════════╣")
    color.addstr(start_y + 3, start_x, f"║  Ваш счет: {score:17d}  ║")
    color.addstr(start_y + 4, start_x, "╠═══════════════════════════════╣")
    color.addstr(start_y + 5, start_x, "║  R/К - Начать заново          ║")
    color.addstr(start_y + 6, start_x, "║  M/Ь - Вернуться в меню       ║")
    color.addstr(start_y + 7, start_x, "║  Q/Й - Выйти из игры          ║")
    color.addstr(start_y + 8, start_x, "╚═══════════════════════════════╝")

    color.refresh()

    while True:
        key = color.getch()
        if key in [ord('q'), ord('й'), ord('Q'), ord('Й')]:
            return 'exit'
        elif key in [ord('r'), ord('к'), ord('R'), ord('К')]:
            return 'restart'
        elif key in [ord('m'), ord('ь'), ord('M'), ord('Ь')]:
            return 'menu'


if __name__ == '__main__':
    curses.wrapper(main)
    