import tkinter

def hit_check_rect():
    dx = abs((x1 + w1 / 2) - (x2 + w2 / 2)) # dx에 두 사각형의 중심 X 방향 거리 대입
    dy = abs((y1 + h1 / 2) - (y2 + h2 / 2)) # dy에 두 사각형의 중심 Y 방향 거리 대입
    if dx <= w1 / 2 + w2 / 2 and dy <= h1 / 2 + h2 / 2: # 사각현이 겹치는 조건 판정
        return True # 겹치면 True 반환
    return False # 겹치지 않으면 False 반환

def mouse_move(e : tkinter.Event):
    global x1, y1
    x1 = e.x - w1 / 2   # 파란색 사각형 X 좌표를 포인터 좌표로 함
    y1 = e.y - h1 / 2   # 파란색 사각형 Y 좌표를 포인터 좌표로 함
    col = "blue"
    if hit_check_rect() is True:
        col = "cyan"
    canvas.delete("RECT1")
    canvas.create_rectangle(x1, y1, x1 + w1, y1 + h1, fill=col, tag="RECT1")

root : tkinter.Tk = tkinter.Tk()
root.title("사각형을 이용한 히트 체크")
canvas : tkinter.Canvas = tkinter.Canvas(width=600, height=400, bg="white")
canvas.pack()
canvas.bind("<Motion>", mouse_move)

x1 : int = 50
y1 : int = 50
w1 : int = 120
h1 : int = 60
canvas.create_rectangle(x1, y1, x1 + w1, y1 + h1, fill="blue", tags="RECT1")

x2 : int = 300
y2 : int = 100
w2 : int = 120
h2 : int = 160
canvas.create_rectangle(x2, y2, x2 + w2, y2 + h2, fill="red")

root.mainloop()