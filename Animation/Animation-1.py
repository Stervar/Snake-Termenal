import curses
import time
import math

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
stdscr = curses.initscr()
curses.curs_set(0)
stdscr.nodelay(1)

# Настройки змеи
snake_length = 30
snake_radius = 4
smoothness = 8

# Начальные координаты змеи
snake_x = [stdscr.getmaxyx()[1] // 2] * snake_length
snake_y = [stdscr.getmaxyx()[0] // 2] * snake_length

# Направление движения
direction = 'right'

# --- Анимация ---
start_time = time.time()
animation_duration = 2  # Продолжительность анимации в секундах

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
        title_progress = (progress - 0.5) * 2  # Изменяем скорость анимации заголовка
        visible_title_chars = int(len(game_title) * title_progress)
        stdscr.addstr(stdscr.getmaxyx()[0] - 2,
                      stdscr.getmaxyx()[1] // 2 - len(game_title) // 2,
                    game_title[:visible_title_chars])
    
    # --- Запуск игры ---
    if progress > 1:
        # --- Код змеи ---
        # ... (код такой же, как в предыдущем примере)

     time.sleep(0.05)
    stdscr.refresh()

# Завершение curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()