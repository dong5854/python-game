import tkinter

root : tkinter.Tk = tkinter.Tk()    # 윈도우 객체 생성
root.title("맵 데이터") # 원도우 타이틀 지정
canvas : tkinter.Canvas = tkinter.Canvas(width=336, height=240) # 캔버스 컴포넌트 생성
canvas.pack()   # 캔버스 배치
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
        n = map_data[y][x]
        canvas.create_image(x * 48 + 24, y * 48 + 24, image=img[n])
root.mainloop()