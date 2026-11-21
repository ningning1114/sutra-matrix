#!/usr/bin/env python3
"""Scattered Buddhist scripture rain for UTF-8 terminals. No dependencies."""
import argparse
import curses
import locale
import random
import sys
import time
from pathlib import Path


def han(text):
    return [c for c in text if '\u3400' <= c <= '\u9fff' or '\U00020000' <= c <= '\U0003134f']


class Stream:
    """Separated falling trails, with brightness and speed suggesting depth."""
    def __init__(self, x, height, chars, initial=False, depth=None):
        self.x = x
        self.height = max(1, height)
        self.depth = depth if depth is not None else random.choices((0, 1, 2), (3, 5, 2))[0]
        # Far streams are faint and slow; foreground streams are bright and fast.
        low, high, speed_low, speed_high, self.peak = (
            (.15, .35, 2, 4, 2),
            (.25, .55, 4, 8, 4),
            (.35, .7, 8, 13, 5),
        )[self.depth]
        self.length = random.randint(max(3, int(height * low)), max(4, int(height * high)))
        self.head = random.uniform(-self.length, height + self.length) if initial else -random.uniform(1, height * .35)
        self.speed = random.uniform(speed_low, speed_high)
        self.chars = [random.choice(chars) for _ in range(self.length)]
        self.gap = random.uniform(height * .04, height * .20)

    def step(self, dt, height):
        self.head += self.speed * dt
        return self.head - self.length > self.height + self.gap

    def cells(self):
        for offset, char in enumerate(self.chars):
            y = int(self.head) - offset
            if not 0 <= y < self.height:
                continue
            # Sparse breaks in the dim end soften the tail without frame flicker.
            if offset > self.length * .65 and (ord(char) + offset) % 7 == 0:
                continue
            strength = 1 - offset / self.length
            band = min(self.peak, int(strength * (self.peak + 1)))
            yield y, char, band


def run(screen, args, chars):
    try:
        curses.curs_set(0)
    except curses.error:
        pass
    screen.nodelay(True)
    screen.keypad(True)
    palette = [curses.A_DIM, curses.A_DIM, 0, 0, curses.A_BOLD, curses.A_BOLD]
    if curses.has_colors():
        curses.start_color()
        themes = {
            'teal': [234, 235, 23, 30, 73, 109],
            'ivory': [234, 236, 240, 245, 250, 230],
            'green': [234, 22, 28, 34, 40, 120],
        }
        colors = themes[args.theme] if curses.COLORS >= 256 else ([0, 0, 7, 7, 7, 7] if args.theme == 'ivory' else [0, 0, 2, 2, 6, 7])
        for i, color in enumerate(colors, 1):
            curses.init_pair(i, color, curses.COLOR_BLACK)
        palette = [curses.color_pair(i) for i in range(1, 7)]
        palette[5] |= curses.A_BOLD
        screen.bkgd(' ', curses.color_pair(1))
    size = None
    streams = []
    paused = False
    speed = args.speed
    last = start = time.monotonic()
    while True:
        now = time.monotonic()
        dt = min(now - last, 0.1)
        last = now
        if args.duration and now - start >= args.duration:
            break
        key = screen.getch()
        if key in (ord('q'), ord('Q'), 27):
            break
        if key == ord(' '):
            paused = not paused
        elif key in (ord('+'), ord('=')):
            speed = min(5, speed * 1.2)
        elif key == ord('-'):
            speed = max(0.1, speed / 1.2)
        height, width = screen.getmaxyx()
        if size != (height, width):
            size = (height, width)
            streams = [Stream(x, height, chars, True) for x in range(0, width - 1, 2)
                       if random.random() < args.density]
        screen.erase()
        for i, stream in enumerate(streams):
            if not paused and stream.step(dt * speed, height):
                streams[i] = stream = Stream(stream.x, height, chars, depth=stream.depth)
            for y, char, band in stream.cells():
                try:
                    screen.addstr(y, stream.x, char, palette[band])
                except curses.error:
                    pass  # A concurrent resize can invalidate a cell.
        screen.refresh()
        time.sleep(1 / 30)


def main():
    parser = argparse.ArgumentParser(description='佛經字雨 · Sutra Matrix', epilog='q / Esc 離開；空白鍵暫停；+ / - 調整速度。')
    parser.add_argument('--text', type=Path, default=Path(__file__).with_name('heart_sutra.txt'), help='UTF-8 經文文字檔')
    parser.add_argument('--speed', type=float, default=2.0, help='速度倍率（0.1–5，預設 2）')
    parser.add_argument('--density', type=float, default=1.0, help='啟用字雨欄位的比例（0.1–1，預設 1）')
    parser.add_argument('--theme', choices=['teal', 'ivory', 'green'], default='ivory', help='青綠、象牙白（預設）、經典綠')
    parser.add_argument('--duration', type=float, default=0, help='幾秒後自動退出；0 表示持續播放')
    args = parser.parse_args()
    if not .1 <= args.speed <= 5 or not .1 <= args.density <= 1 or not args.duration >= 0:
        parser.error('速度須為 0.1–5，密度須為 0.1–1，時間不可小於 0。')
    try:
        chars = han(args.text.read_text(encoding='utf-8'))
    except (OSError, UnicodeError) as error:
        parser.error(str(error))
    if not chars:
        parser.error('文字檔內沒有可顯示的漢字。')
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        parser.error('請在互動式終端機中執行。')
    locale.setlocale(locale.LC_ALL, '')
    try:
        curses.wrapper(run, args, chars)
    except KeyboardInterrupt:
        pass
    except curses.error as error:
        parser.exit(1, f'終端機初始化失敗：{error}\n請使用支援 UTF-8 與色彩的終端機。\n')


if __name__ == '__main__':
    main()
