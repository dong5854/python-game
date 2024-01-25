import tkinter

def mouse_click(e: tkinter.Event):
    px = e.x
    py = e.y
    print("마우스 포인터 좌표: ({},{})".format(px, py))
    mx = int(px / 48)
    my = int(py / 48)
    if 0 <= mx and mx <= 6 and 0 <= my and my <= 4:
        n = map_data[my][mx]
        print("여기에 있는 맵 칩은 " + CHIP_NAME[n])

root : tkinter.Tk = tkinter.Tk()
root.title("맵 데이터")
canvas : tkinter.Canvas = tkinter.Canvas(width=336, height=240)
canvas.pack() # 캔버스 컴포넌트 생성
canvas.bind("<Button>", mouse_click)
CHIP_NAME = ["풀", "꽃", "숲", "바다"]
img : list = [ # 리스트에 이미지 로딩
    tkinter.PhotoImage(file="chip0.png"), # 풀 맵 칩
    tkinter.PhotoImage(file="chip1.png"), # 꽃 맵 칩
    tkinter.PhotoImage(file="chip2.png"), # 숲 맵 칩
    tkinter.PhotoImage(file="chip3.png")  # 바다 맵 칩
]
map_data : list = [ # 2차원 리스트로 맵 데이터 정의
    [0, 1, 0, 2, 2, 2, 2],
    [3, 0, 0, 0, 2, 2, 2],
    [3, 0, 0, 1, 0, 0, 0],
    [3, 3, 0, 0, 0, 0, 1],
    [3, 3, 3, 3, 0, 0, 0],
]
for y in range(5):
    for x in range(7):
        canvas.create_image(x * 48 + 24, y * 48 + 24, image=img[map_data[y][x]])

root.mainloop()