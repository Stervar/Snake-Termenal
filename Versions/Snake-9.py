import curses
import time
import random
import sys
from curses import textpad

def animation_loading(stdscr):
    loading_text = [
        "   _____             _         _____                      ",
        "  / ____|           | |       / ____|                     ",
        " | (___   __ _ _ __ | |_ ___ | |  __  __ _ _ __ ___   ___ ",
        "  \\___ \\ / _` | '_ \\| __/ _ \\| | |_ |/ _` | '_ ` _ \\ / _ \\",
        "  ____) | (_| | | | | ||  __/| |__| | (_| | | | | | |  __/ ",
        " |_____/ \\__,_|_| |_|\\__\\___| \\_____|\\__,_|_| |_| |_|\\___| "
    ]
    game_title = "Игра про змейку высшего уровня"
    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(1)

    start_time = time.time()
    animation_duration = 5

    while True:
        stdscr.clear()
        elapsed_time = time.time() - start_time
        progress = elapsed_time / animation_duration
        
        if progress <= 1:
            for i, line in enumerate(loading_text):
                visible_chars = int(len(line) * progress)
                stdscr.addstr(stdscr.getmaxyx()[0] // 2 - len(loading_text) // 2 + i,
                            stdscr.getmaxyx()[1] // 2 - len(line) // 2,
                            line[:visible_chars])
            
            bar_length = 30
            filled_length = int(bar_length * progress)
            bar = '█' * filled_length + '-' * (bar_length - filled_length)
            y = stdscr.getmaxyx()[0] // 2 + len(loading_text) // 2 + 2
            x = stdscr.getmaxyx()[1] // 2 - bar_length // 2
            if y >= 0 and y < stdscr.getmaxyx()[0] and x >= 0 and x < stdscr.getmaxyx()[1]:
                stdscr.addstr(y, x, f"[{bar}] {int(progress * 100)}%")
        else:
            for i, line in enumerate(loading_text):
                stdscr.addstr(stdscr.getmaxyx()[0] // 2 - len(loading_text) // 2 + i,
                            stdscr.getmaxyx()[1] // 2 - len(line) // 2,
                            line)

        if progress > 0.5:
            title_progress = (progress - 0.5) * 2
            visible_title_chars = int(len(game_title) * title_progress)
            y = stdscr.getmaxyx()[0] - 2
            x = stdscr.getmaxyx()[1] // 2 - len(game_title) // 2
            if y >= 0 and y < stdscr.getmaxyx()[0] and x >= 0 and x < stdscr.getmaxyx()[1]:
                stdscr.addstr(y, x, game_title[:visible_title_chars])
        
        if progress > 1:
            stdscr.refresh()
            time.sleep(1)
            break
        
        time.sleep(0.05)
        stdscr.refresh()
        
def show_menu(stdscr):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    if h < 20 or w < 60:
        stdscr.addstr(0, 0, "Пожалуйста, измените размер окна терминала.")
        stdscr.refresh()
        stdscr.getch()
        sys.exit()

    title = [
        "   _____             _         _____                      ",
        "  / ____|           | |       / ____|                     ",
        " | (___   __ _ _ __ | |_ ___ | |  __  __ _ _ __ ___   ___ ",
        "  \\___ \\ / _` | '_ \\| __/ _ \\| | |_ |/ _` | '_ ` _ \\ / _ \\",
        "  ____) | (_| | | | | ||  __/| |__| | (_| | | | | | |  __/ ",
        " |_____/ \\__,_|_| |_|\\__\\___| \\_____|\\__,_|_| |_| |_|\\___| "
    ]
    for i, line in enumerate(title):
        y = h // 2 - len(title) - 8 + i
        x = max(0, w // 2 - len(line) // 2)
        if y >= 0 and y < h and x >= 0 and x < w:
            stdscr.addstr(y, x, line)

    subtitle = "Игра про змейку которая была улучшина 'Sterva'"
    y = h // 2 - len(title) - 1
    x = max(0, w // 2 - len(subtitle) // 2)
    if y >= 0 and y < h and x >= 0 and x < w:
        stdscr.addstr(y, x, subtitle)

    # Adjust the y position for menu_items
    menu_items = [
        "+---------------------------+",
        "|      ГЛАВНОЕ МЕНЮ         |",
        "+---------------------------+",
        "| 1. Начать игру            |",
        "| 2. Установить сложность   |",
        "| 3. Установить размер карты|",
        "| 4. Количество яблок       |",
        "| 5. Установить типы яблок  |",
        "| 6. Выйти                  |",
        "+---------------------------+"
    ]
    for i, line in enumerate(menu_items):
        y = h // 2 + i - 2  # Move menu items up by 2 lines
        x = max(0, w // 2 - len(line) // 2)
        if y >= 0 and y < h and x >= 0 and x < w:
            stdscr.addstr(y, x, line)

    # Adjust the y position for info_box
    info_box = [
        "+---------------------------------------+",
        "|          Информация об игре           |",
        "+---------------------------------------+",
        "| Управление: W/↑ - вверх, S/↓ - вниз,  |",
        "| A/← - влево, D/→ - вправо             |",
        "| Пауза: P                              |",
        "| Яблоки:                               |",
        "|  - Обычное яблоко: +1 очко            |",
        "|  - Большое яблоко: +2 очка            |",
        "|  - Супер яблоко: +3 очка              |",
        "|    (дает дополнительные очки)         |",
        "+---------------------------------------+"
    ]
    for i, line in enumerate(info_box):
        y = h // 2 + len(menu_items) - 2 + i  # Move info box up by 2 lines
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
        
def set_difficulty(stdscr):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    options = [
        "+---------------------------+",
        "|     Выберите сложность:   |",
        "| 1. Легко                  |",
        "| 2. Средне                 |",
        "| 3. Сложно                 |",
        "+---------------------------+"
    ]
    for i, line in enumerate(options):
        stdscr.addstr(h // 2 - len(options) // 2 + i, max(0, w // 2 - len(line) // 2), line)
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('1'):
            return 1
        elif key == ord('2'):
            return 1.5
        elif key == ord('3'):
            return 2

def set_map_size(stdscr):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    options = [
        "+---------------------------+",
        "|   Выберите размер карты:  |",
        "| 1. Маленький              |",
        "| 2. Средний                |",
        "| 3. Большой                |",
        "+---------------------------+"
    ]
    for i, line in enumerate(options):
        stdscr.addstr(h // 2 - len(options) // 2 + i, max(0, w // 2 - len(line) // 2), line)
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('1'):
            return 'small'
        elif key == ord('2'):
            return 'medium'
        elif key == ord('3'):
            return 'large'

def set_apple_count(stdscr):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    stdscr.addstr(h // 2, max(0, w // 2 - 20), "Введите количество яблок (1-10): ")
    stdscr.refresh()

    curses.echo()
    while True:
        count_str = stdscr.getstr().decode('utf-8')
        if count_str.isdigit() and 1 <= int(count_str) <= 10:
            return int(count_str)
    curses.noecho()

def set_apple_types(stdscr):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    options = [
        "+---------------------------+",
        "|   Выберите типы яблок:    |",
        "| 1. Только обычные         |",
        "| 2. Обычные и большие      |",
        "| 3. Все типы (супер)       |",
        "+---------------------------+"
    ]
    for i, line in enumerate(options):
        stdscr.addstr(h // 2 - len(options) // 2 + i, max(0, w // 2 - len(line) // 2), line)
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('1'):
            return [' normal']
        elif key == ord('2'):
            return ['normal', 'big']
        elif key == ord('3'):
            return ['normal', 'big', 'super']

def create_apples(snake, box, apple_count, apple_types):
    apples = []
    for _ in range(apple_count):
        while True:
            apple = [random.randint(box[0][0] + 1, box[1][0] - 1), random.randint(box[0][1] + 1, box[1][1] - 1)]
            if apple not in snake and apple not in [a[0] for a in apples]:
                apple_type = random.choice(apple_types)
                apples.append((apple, apple_type))
                break
    return apples

def main(stdscr):
    animation_loading(stdscr)
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(50)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    difficulty = 1
    map_size = 'medium'
    apple_count = 2
    apple_types = ['normal', 'big']

    while True:
        menu_choice = show_menu(stdscr)
        if menu_choice == 'play':
            break
        elif menu_choice == 'difficulty':
            difficulty = set_difficulty(stdscr)
        elif menu_choice == 'map_size':
            map_size = set_map_size(stdscr)
        elif menu_choice == 'apple_count':
            apple_count = set_apple_count(stdscr)
        elif menu_choice == 'apple_types':
            apple_types = set_apple_types(stdscr)
        elif menu_choice == 'exit':
            return

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

    while True:
        current_time = time.time()
        stdscr.clear()
        textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
        stdscr.addstr(0, 0, f"Счет: {score} | Время: {int(current_time - start_time)} сек.")
        stdscr.addstr(0, curses.COLS - 5, "Выход: Q | Пауза: P")

        for i, (y, x) in enumerate(snake):
            if i == 0:
                stdscr.addch(y, x, '۝', curses.color_pair(4))  # Голова змейки
            else:
                stdscr.addch(y, x, 'o', curses.color_pair(1))  # Тело змейки

        for apple, apple_type in apples:
            if apple_type == 'normal':
                stdscr.addch(apple[0], apple[1], '*', curses.color_pair(2))
            elif apple_type == 'big':
                stdscr.addch(apple[0], apple[1], '*', curses.color_pair(3))
            elif apple_type == 'super':
                stdscr.addch(apple[0], apple[1], '*', curses.color_pair(4))

        stdscr.refresh()

        key = stdscr.getch()
        if key != -1:
            if key == ord('q'):
                break
            elif key == ord('p'):
                paused = not paused
                while paused:
                    stdscr.addstr(curses.LINES // 2, curses.COLS // 2 - 5, "Пауза. Нажмите P, чтобы продолжить.")
                    stdscr.refresh()
                    key = stdscr.getch()
                    if key == ord('p'):
                        paused = False
                        break
            elif key in [curses.KEY_UP, ord('w')] and direction != curses.KEY_DOWN:
                direction = curses.KEY_UP
            elif key in [curses.KEY_DOWN, ord('s')] and direction != curses.KEY_UP:
                direction = curses.KEY_DOWN
            elif key in [curses.KEY_LEFT, ord('a')] and direction != curses.KEY_RIGHT:
                direction = curses.KEY_LEFT
            elif key in [curses.KEY_RIGHT, ord('d')] and direction != curses.KEY_LEFT:
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
                    score += 1
                    apples.remove((apple, apple_type))

                    # Проверка типа яблока
                    if apple_type == 'super':
                        for _ in range(3):  # Добавляем три сегмента к змейке
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
                if snake[0] in snake[1:]:
                    stdscr.addstr(curses.LINES // 2, curses.COLS // 2 - 10, "Игра окончена! Нажмите Q, чтобы выйти.")
                    stdscr.refresh()
                    while True:
                        key = stdscr.getch()
                        if key == ord('q'):
                            return
                snake.pop()

if __name__ == '__main__':
    curses.wrapper(main)
    
