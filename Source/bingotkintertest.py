import io
import time
import os
import tkinter as tk
import base64
import pygame # type: ignore
import random
import win32gui # type: ignore
from threading import Thread
global closed
closed = False
def open_popup2():
    global root, img, im
    top2 = tk.Toplevel(root)
    top2.title("Settings")
    top2.geometry("250x150")
    top2.iconphoto(False, img)
    tk.Button(top2, text="Save", image=im, compound='c', height=30, width=30).place(x=0, y=112)
    top2.mainloop()
def open_popup1():
    global root, im, img
    top1 = tk.Toplevel(root)
    top1.configure(background='white')
    top1.iconphoto(False, img)
    top1.resizable(False, False)
    top1.geometry("640x80")
    top1.title("About")
    tk.Label(top1, text= "Tehty Juho Jokisalo käyttämällä python 3.12.7", font=('Segoe UI', 10), bg="white", fg="black").place(x=0,y=0)
    tk.Label(top1, text= "Hello from the pygame community.", font=('Segoe UI', 10), bg="white", fg="black").place(x=0,y=20)
    link1 = tk.Label(top1, text= "https://www.pygame.org/contribute.html", font=('Segoe UI', 10), bg="white", fg="black")
    link1.place(x=207,y=20)
    link1.bind("<Enter>", lambda _:link1.config(font=('Segoe UI', 10, "underline")))
    link1.bind("<Leave>", lambda _:link1.config(font=('Segoe UI', 10)))
    link1.bind("<Button-1>", lambda _:os.system("start \"\" https://www.pygame.org/contribute.html"))
    tk.Label(top1, text= "Minä aloitin luomaan tätä projektia Kuivasjärven Koululle 5/10/2024.", font=('Segoe UI', 10), bg="white", fg="black").place(x=0,y=40)
    tk.Label(top1, text= "Tämä ohjelma on avoimen lähdekoodin.", font=('Segoe UI', 10), bg="white", fg="black").place(x=0,y=60)
    link2 = tk.Label(top1, text= "https://github.com/TheDoubleMix/PygameBingo", font=('Segoe UI', 10), bg="white", fg="black")
    link2.place(x=235,y=60)
    link2.bind("<Enter>", lambda _:link2.config(font=('Segoe UI', 10, "underline")))
    link2.bind("<Leave>", lambda _:link2.config(font=('Segoe UI', 10)))
    link2.bind("<Button-1>", lambda _:os.system("start \"\" https://github.com/TheDoubleMix/PygameBingo"))
def threaded_function(arg):
    global closed, root, im, img, i
    root = tk.Tk()
    menu = tk.Menu(root)
    root.config(menu=menu)
    helpmenu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label='Options', menu=helpmenu)
    helpmenu.add_command(label='Settings', command=open_popup2)
    helpmenu.add_command(label='About', command=open_popup1)
    helpmenu.add_command(label='Quit', command=root.quit)
    root.resizable(False, False)
    root.geometry('250x187')
    root.title("Console")
    im = tk.PhotoImage(width=1, height=1)
    img = tk.PhotoImage(data=pngfile)
    root.iconphoto(False, img)
    def reset():
        start.config(text="Restart")
        global i, text_width, text_line, reset_history, not_started
        text_line, text_width, i, reset_history, not_started = 0, 0, 0, 1, False
    def pause():
        global paused
        if paused == False:
            pausebutton.config(text="Unpause")
            paused = True
        else:
            pausebutton.config(text="Pause")
            paused = False
    start =tk.Button(root, text="Start", image=im, compound='c', height=85, width=250, font=('Segoe UI', 48), command=reset)
    start.pack()
    pausebutton = tk.Button(root, text="Pause", image=im, compound='c', height=85, width=250, font=('Segoe UI', 48), command=pause)
    pausebutton.pack()
    root.mainloop()
numberhistoryrect = pygame.Rect(480, 0, 480, 480)
currentletter = ""
pngfile = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAOlSURBVGhD5ZgNjSpBEISxgAYs4AEJaMACDnCAAxSgAAMYwAEe9uUjDKmt7ZmeveNIyKukk3c3f109VT17bzF8OUICq9VqWCwWaSyXy2Gz2QzH43G43+/P1THW6/Vo7eVyeY78DhMCJKIH9QZkrtfrc5cpfP67MNmJyvhhvQGJ6CYgpvO44XdhQgA56GFzg/WfxITAbrfrTuh8Pk/8cjgcnqOfwYTAXLORsM6PCGB0neN7Ij0dLzidTqN8+DdFU0wI6EZEBr8xDnXoOKE+8aYBWTzjhdRQEqMM3cBsEoFDmevJRya+3W6TOYroTL8RD20CIwJUL1rQExwatVGqpfOosKLWNCgO5IHLlChjIwL7/X4ysSdYF7VPkHnEb5HokWHx0YiAm603qH50KPA93YQ+vt1unyNj6ByiFGxEwCfNDU8OeJstV1+gY0Qkw5aPXgQysylgT8XdbG565uk4ofAXunZmy0evHTOzRYgMqPAO43v6mTX5tHz0OjEzWwRPgFD4nphd0Xtmy0evE1uTavA1LgEqquNudF9fOovDpao+ehFoTVKgaw7y5AhaosJfU08wMzjIvPkgEJntJ+EJ+LgiM3hB5s3HKjfbT8Ll4Xt6h/JxT6wg88mDgE+aE1xp9Ih5h3J5ZeMFmTcfBCI9twLtsoYkkEIE/yxhriIbL8i8GQvvi/B/EUDrqkmMqfrX6/Z2p8DAaF7bLPPZO/JTC10E0Ln3dA2S8bYYdRXm9PiNs6KPuggpgSz5Et4tvN317lOCRsGaDCkBqqsba9ukI9Qq6lKI/liCZEkSWfnL7EWI0CTgzzjBQQ4/2Of5ZzMRab3381rRJOBVi3QNoodQ4bdY2we4zDIvNAn4ZrUvVP8s4EYUfkOtL133UnTjiiYB3Yiomco/uPCFQseIljnfRsD16FVVuITUfNntOHQu4Z8OjioBP3iOblUic/bxm/yVif3g2mZRp1LjIRcdayXl8ql9oSpmeSDSY/Q4OdzEUQvldzqHyOQDmgQ8OX4uJKhylDy/c7hH9DHkhvxvA8L/A6CGJoGoKllE106SEdlatHziaBIA/ghpIA3Xbe0Pk14SvZUvSAkAbkIPJ+kiAU8qezlZxzuBjMoa9qBQ2doIXQRqmNNh/gohAYxKMlSaqH0Vuvl62t67USWgiRFok4qD0jlUBkTUZv8aVQl5clnM6RzvRJVAkVGUrAfJl9v5NJom5iVEKiToZErnaH0afwJNAt+ALycwDP8Ay11I2pHEEhQAAAAASUVORK5CYII='
output = io.BytesIO(base64.b64decode(pngfile))
icon = pygame.image.load(output)
color1 = (128, 0, 255)
color2 = (255, 0, 0)
color3 = (0, 0, 255)
color4 = (255, 255, 0)
color5 = (0, 255, 0)
pygame.font.init()
pygame.display.set_icon(icon)
pygame.display.set_caption('Bingo') 
GAME_WIDTH, GAME_HEIGHT = 960, 480
bingonumbers = random.sample(range(1, 76), 75)
font1 = pygame.font.Font(pygame.font.get_default_font(), 180)
font2 = pygame.font.Font(pygame.font.get_default_font(), 36)
text_surface = font1.render(str(bingonumbers[0]), True, (255, 255, 255))
class Rect:
    def __init__(self, size, position):
        self.size = size
        self.position = position
        self.rect = pygame.Rect(position, (size, size))
        self.speed = 5
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 5 or self.rect.x > GAME_WIDTH - self.size - 5:
            self.speed *= -1
    def draw(self, screen):
        pygame.draw.rect(screen, 'red', self.rect)

def window_continue(hwnd):
    message = win32gui.GetMessage(hwnd, 0, 0)
    if message[0] != 0:
        win32gui.TranslateMessage(message[1])
        win32gui.DispatchMessage(message[1])
def handle_events():
    if not closed == True:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT] or event.type in [pygame.KEYDOWN] and event.key in [pygame.K_ESCAPE]:
                pygame.quit()
                raise SystemExit
    else:
        pygame.quit()
        raise SystemExit
def init(screen):
    global closed
    rect = Rect(20, (150, 150))
    pygamethread = Thread(target=lambda: draw(screen, [rect]), daemon=True)
    tkinterthread = Thread(target = threaded_function, args = (10, ))
    tkinterthread.daemon = True
    tkinterthread.start()
    pygamethread.start()
    while tkinterthread.is_alive():
        for event in pygame.event.get():
            if event.type in [pygame.QUIT] or event.type in [pygame.KEYDOWN] and event.key in [pygame.K_ESCAPE]:
                pygame.quit()
                raise SystemExit
        if pygamethread.is_alive() == False:
            break
    closed = True
    pygame.quit()

def draw(screen, game_objects):
    global closed, i, text_line, text_width, reset_history, not_started, paused
    paused = False
    reset_history = 0
    i = 0
    text_width = 0
    text_line = 0
    not_started = True
    scroll_up = numberhistoryrect.move(0, -100)
    print(bingonumbers)
    while not_started:
        screen.fill("black")
    while True:
        if closed == True:
            return
        if not i > 74:
            screen.fill("black", rect=(0,0,GAME_WIDTH/2,GAME_HEIGHT))
            if  bingonumbers[i] < 15:
                currentletter = "B"
                pygame.draw.circle(screen,color1,(240,240),240)
            elif  bingonumbers[i] < 30:
                currentletter = "I"
                pygame.draw.circle(screen,color2,(240,240),240)
            elif  bingonumbers[i] < 45:
                currentletter = "N"
                pygame.draw.circle(screen,color3,(240,240),240)
            elif  bingonumbers[i] < 60:
                currentletter = "G"
                pygame.draw.circle(screen,color4,(240,240),240)
            else:
                currentletter = "O"
                pygame.draw.circle(screen,color5,(240,240),240)
            text_surface = font1.render(currentletter + str(bingonumbers[i]), True, (255, 255, 255))
            text_surface2 = font2.render((currentletter + str(bingonumbers[i])) + ", ", True, (255, 255, 255))
            if reset_history == 1:
                screen.fill("black", rect=(480,0,GAME_WIDTH/2,GAME_HEIGHT))
                reset_history = 0
            if 480 + text_width + text_surface2.get_width() > 960:
                if not text_line + (text_surface2.get_height() * 2) > 480:
                    text_line += text_surface2.get_height()
                else:
                    scroll_up = numberhistoryrect.move(0, text_surface2.get_height() * -1)
                    currentscreen = screen.subsurface(numberhistoryrect).copy()
                    screen.fill("black", rect=(480,0,GAME_WIDTH/2,GAME_HEIGHT))
                    screen.blit(currentscreen, scroll_up.topleft)
                text_width = 0
            screen.blit(text_surface2, (480+text_width, text_line))
            text_width += text_surface2.get_width()
            i += 1
            screen.blit(text_surface, text_surface.get_rect(center=(240, 240)))
            pygame.display.flip()
            while True:
                for n in range(10):
                    time.sleep(0.1)
                    if reset_history == 1:
                        break
                break
            while True:
                if paused == False:
                    break
def run():
    if closed == False:
        hwnd = pygame.display.get_wm_info()['window']
    while True:
        if closed == False:
            window_continue(hwnd)
        handle_events()
def main():
    pygame.init()
    init(pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT)))
    run()
if __name__ == '__main__':  
    main()