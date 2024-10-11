import curses
import time
import math
import random
import sys
from curses import textpad

def animation_loading(stdscr):
    # Текстовые данные
    loading_text = [
        "   _____             _         _____                      ",
        "  / ____|           | |       / ____|                     ",
        " | (___   __ _ _ __ | |_ ___ | |  __  __ _ _ __ ___   ___ ",
        "  \\___ \\ / _` | '_ \\| __/ _ \\| | |_ |/ _` | '_ ` _ \\ / _ \\",
        "  ____) | (_| | | | | ||  __/| |__| | (_| | | | | | |  __/",
        " |_____/ \\__,_|_| |_|\\__\\___| \\_____|\\__,_|_| |_| |_|\\___|"
    ]
    game_title = "Игра про змейку высшего уровня"

    # Инициализация curses
    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(1)

    # --- Анимация ---
    start_time = time.time()
    animation_duration = 5  # Продолжительность анимации в секундах

    while True:
        stdscr.clear()
        elapsed_time = time.time() - start_time
        
        # --- Анимация текста ---
        progress = elapsed_time / animation_duration
        if progress <= 1:
            for i, line in enumerate(loading_text):
                visible_chars = int(len(line) * progress)
                stdscr.addstr(stdscr.getmaxyx()[0] // 2 - len(loading_text) // 2 + i,
                            stdscr.getmaxyx()[1] // 2 - len(line) // 2,
                            line[:visible_chars])
        else:
            for i, line in enumerate(loading_text):
                stdscr.addstr(stdscr.getmaxyx()[0] // 2 - len(loading_text) // 2 + i,
                            stdscr.getmaxyx()[1] // 2 - len(line) // 2,
                            line)

        # --- Анимация заголовка игры ---
        if progress > 0.5:  # Заголовок появляется после половины анимации
            title_progress = (progress - 0.5) * 4  # Изменяем скорость анимации заголовка
            visible_title_chars = int(len(game_title) * title_progress)
            stdscr.addstr(stdscr.getmaxyx()[0] - 2,
                        stdscr.getmaxyx()[1] // 2 - len(game_title) // 2,
                        game_title[:visible_title_chars])
        
        # --- Запуск игры ---
        if progress > 1:
            break
        
        time.sleep(0.05)
        stdscr.refresh()

def show_menu(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(50)

    # Инициализация цветовых пар
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Для головы змейки

    # Начальные параметры
    direction = curses.KEY_RIGHT
    score = 0
    start_time = time.time()
    difficulty = 1
    map_size = 'medium'
    paused = False
    apple_count = 2  # Начальное количество яблок
    apple_types = ['normal', 'big']  # Начальные типы яблок

    def create_apple(snake, box):
        while True:
            apple = [random.randint(box[0][0] + 1, box[1][0] - 1), random.randint(box[0][1] + 1, box[1][1] - 1)]
            if apple not in snake:
                return apple

    def create_apples(snake, box, apple_count, apple_types):
        apples = []
        for _ in range(apple_count):
            while True:
                apple = [random.randint(box[0][0] + 1, box[1][0] -  1), random.randint(box[0][1] + 1, box[1][1] - 1)]
                if apple not in snake and apple not in [a[0] for a in apples]:
                    if random.random() < 0.5:  # 50% шанс обычное яблоко
                        apple_type = 'normal'
                    elif random.random() < 0.8:  # 30% шанс большое яблоко
                        apple_type = 'big'
                    else:  # 20% шанс специальное яблоко
                        apple_type = 'special'
                    apples.append((apple, apple_type))
                    break
        return apples

    def draw_box(stdscr, box):
        for i in range(box[0][0], box[1][0]):
            stdscr.addstr(i, box[0][1], '#')
            stdscr.addstr(i, box[1][1], '#')
        for i in range(box[0][1], box[1][1]):
            stdscr.addstr(box[0][0], i, '#')
            stdscr.addstr(box[1][0], i, '#')

    def draw_snake(stdscr, snake, direction):
        for i, point in enumerate(snake):
            if i == 0:
                stdscr.addstr(point[0], point[1], '#', curses.color_pair(4))
            else:
                stdscr.addstr(point[0], point[1], '#')

    def draw_apples(stdscr, apples):
        for apple in apples:
            if apple[1] == 'normal':
                stdscr.addstr(apple[0][0], apple[0][1], '*', curses.color_pair(1))
            elif apple[1] == 'big':
                stdscr.addstr(apple[0][0], apple[0][1], '*', curses.color_pair(2))
            else:
                stdscr.addstr(apple[0][0], apple[0][1], '*', curses.color_pair(3))

    def game_over(stdscr, score):
        stdscr.clear()
        stdscr.addstr(stdscr.getmaxyx()[0] // 2, stdscr.getmaxyx()[1] // 2 - 10, "Game Over!")
        stdscr.addstr(stdscr.getmaxyx()[0] // 2 + 1, stdscr.getmaxyx()[1] // 2 - 10, f"Score: {score}")
        stdscr.refresh()
        time.sleep(2)

    # Инициализация змейки
    snake = [[20, 20], [20, 21], [20, 22], [20, 23], [20, 24]]
    box = [[10, 10], [30, 30]]

    # Создаем яблоки
    apples = create_apples(snake, box, apple_count, apple_types)

    while True:
        stdscr.clear()
        draw_box(stdscr, box)
        draw_snake(stdscr, snake, direction)
        draw_apples(stdscr, apples)

        # Обработка событий
        c = stdscr.getch()
        if c == curses.KEY_UP and direction != curses.KEY_DOWN:
            direction = curses.KEY_UP
        elif c == curses.KEY_DOWN and direction != curses.KEY_UP:
            direction = curses.KEY_DOWN
        elif c == curses.KEY_LEFT and direction != curses.KEY_RIGHT:
            direction = curses.KEY_LEFT
        elif c == curses.KEY_RIGHT and direction != curses.KEY_LEFT:
            direction = curses.KEY_RIGHT
        elif c == ord('p'):
            paused = not paused

        # Движение змейки
        if not paused:
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

            # Проверка столкновения со стеной
            if (new_head[0] < box[0][0] or new_head[0] > box[1][0] or
                new_head[1] < box[0][1] or new_head[1] > box[1][1]):
                game_over(stdscr, score)
                break

            # Проверка столкновения с яблоком
            for apple in apples:
                if new_head == apple[0]:
                    score += 1
                    apples.remove(apple)
                    apples.append(create_apple(snake, box))
                    break
            else:
                snake.pop()

        stdscr.refresh()
        time.sleep(0.1)

def main(stdscr):
    animation_loading(stdscr)
    show_menu(stdscr)

curses.wrapper(main)