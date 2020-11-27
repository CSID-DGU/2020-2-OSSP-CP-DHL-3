import tkinter as tk

x = 960
y = 690
zoom_size = 24
subsample_size = 30

size = str(x) + "x" + str(y)
root = tk.Tk()
root.title('DHL')
root.geometry(size)
root.resizable(False, False)
frame = tk.Frame(root, bd = 5, bg='white', relief = 'groove')
frame.pack()

b_frame = tk.Frame(frame, width = x * 1, height = y * 0.166)
b_frame.grid(row = 0, column = 0, columnspan = 5)

line = [" 탑", "정글", "미드", "원딜", "서폿"]
global select_champion_num, select_line_num, select
select_champion_num, select_line_num,  = None, None

jon = 10
si = 6

select = tk.IntVar()

b1_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b1_frame.pack(side = tk.LEFT)
tk.Radiobutton(b1_frame, value = 11, variable=select, width = jon, activebackground="blue").pack(side=tk.BOTTOM)

b2_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b2_frame.pack(side = tk.LEFT)
tk.Radiobutton(b2_frame, value = 12, variable=select, width = jon, activebackground="blue").pack(side=tk.BOTTOM)

b3_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b3_frame.pack(side = tk.LEFT)
tk.Radiobutton(b3_frame, value = 13, variable=select, width = jon, activebackground="blue").pack(side=tk.BOTTOM)

b4_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b4_frame.pack(side = tk.LEFT)
tk.Radiobutton(b4_frame, value = 14, variable=select, width = jon, activebackground="blue").pack(side=tk.BOTTOM)

b5_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b5_frame.pack(side = tk.LEFT)
tk.Radiobutton(b5_frame, value = 15, variable=select, width = jon, activebackground="blue").pack(side=tk.BOTTOM)

b6_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b6_frame.pack(side = tk.LEFT)
tk.Radiobutton(b6_frame, value = 16, variable=select, width = jon, activebackground="blue").pack(side=tk.BOTTOM)

b7_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b7_frame.pack(side = tk.LEFT)
tk.Radiobutton(b7_frame, value = 17, variable=select, width = jon, activebackground="blue").pack(side=tk.BOTTOM)

b8_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b8_frame.pack(side = tk.LEFT)
tk.Radiobutton(b8_frame, value = 18, variable=select, width = jon, activebackground="blue").pack(side=tk.BOTTOM)

b9_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b9_frame.pack(side = tk.LEFT)
tk.Radiobutton(b9_frame, value = 19, variable=select, width = jon, activebackground="blue").pack(side=tk.BOTTOM)

b10_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b10_frame.pack(side = tk.LEFT)
tk.Radiobutton(b10_frame, value = 20, variable=select, width = jon, activebackground="blue").pack(side=tk.BOTTOM)

l1_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
l1_frame.grid(row = 1, column = 0)
tk.Radiobutton(l1_frame, value = 1, variable=select, activebackground="blue").pack(side=tk.LEFT)
l1_line = tk.Label(l1_frame)
l1_line.pack(side=tk.RIGHT)

l2_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
l2_frame.grid(row = 2, column = 0)
tk.Radiobutton(l2_frame, value = 2, variable=select, activebackground="blue").pack(side=tk.LEFT)
l2_line = tk.Label(l2_frame)
l2_line.pack(side=tk.RIGHT)

l3_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
l3_frame.grid(row = 3, column = 0)
tk.Radiobutton(l3_frame, value = 3, variable=select, activebackground="blue").pack(side=tk.LEFT)
l3_line = tk.Label(l3_frame)
l3_line.pack(side=tk.RIGHT)

l4_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
l4_frame.grid(row = 4, column = 0)
tk.Radiobutton(l4_frame, value = 4, variable=select, activebackground="blue").pack(side=tk.LEFT)
l4_line = tk.Label(l4_frame)
l4_line.pack(side=tk.RIGHT)

l5_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
l5_frame.grid(row = 5, column = 0)
tk.Radiobutton(l5_frame, value = 5, variable=select, activebackground="blue").pack(side=tk.LEFT)
l5_line = tk.Label(l5_frame)
l5_line.pack(side=tk.RIGHT)

m_frame = tk.Frame(frame, width = x * 0.6, height = y * 0.668)
m_frame.grid(row = 1, column = 1, rowspan = 4)

r1_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
r1_frame.grid(row = 1, column = 4)
tk.Radiobutton(r1_frame, value = 6, variable=select, activebackground="blue").pack(side=tk.RIGHT)
r1_line = tk.Label(r1_frame)
r1_line.pack(side=tk.LEFT)

r2_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
r2_frame.grid(row = 2, column = 4)
tk.Radiobutton(r2_frame, value = 7, variable=select, activebackground="blue").pack(side=tk.RIGHT)
r2_line = tk.Label(r2_frame)
r2_line.pack(side=tk.LEFT)

r3_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
r3_frame.grid(row = 3, column = 4)
tk.Radiobutton(r3_frame, value = 8, variable=select, activebackground="blue").pack(side=tk.RIGHT)
r3_line = tk.Label(r3_frame)
r3_line.pack(side=tk.LEFT)

r4_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
r4_frame.grid(row = 4, column = 4)
tk.Radiobutton(r4_frame, value = 9, variable=select, activebackground="blue").pack(side=tk.RIGHT)
r4_line = tk.Label(r4_frame)
r4_line.pack(side=tk.LEFT)

r5_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.17)
r5_frame.grid(row = 5, column = 4)
tk.Radiobutton(r5_frame, value = 10, variable=select, activebackground="blue").pack(side=tk.RIGHT)
r5_line = tk.Label(r5_frame)
r5_line.pack(side=tk.LEFT)

option_frame = tk.Frame(frame, width = x * 0.6, height = y * 0.166)
option_frame.grid(row = 5, column = 1)

line_frame = tk.Frame(option_frame, width = x * 0.61, height = y * 0.066)
line_frame.grid(row = 1, column = 0)

CheckVariety = tk.IntVar()
tk.Radiobutton(line_frame, text="탑", value = 0, width = 10, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)
tk.Radiobutton(line_frame, text="정글", value = 1, width = 10, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)
tk.Radiobutton(line_frame, text="미드", value = 2, width = 10, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)
tk.Radiobutton(line_frame, text="원딜", value = 3, width = 10, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)
tk.Radiobutton(line_frame, text="서폿", value = 4, width = 10, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)

choice_frame = tk.Frame(option_frame, width=x * 0.6, height=y * 0.1)
choice_frame.grid(row=2, column=0)

rec_frame = tk.Frame(choice_frame, width=x * 0.6 * 0.33, height=y * 0.1)
rec_frame.grid(row=0, column=0)
button_recommend = tk.Button(rec_frame, width=21, height=3, text="추천받기")
button_recommend.pack()

select_frame = tk.Frame(choice_frame, width=x * 0.6 * 0.34, height=y * 0.1)
select_frame.grid(row=0, column=1)
button_pick = tk.Button(select_frame, width=26, height=3, text="선택하기")
button_pick.pack()

rec_text_frame = tk.Frame(choice_frame, width=x * 0.6 * 0.328, height=y * 0.1)
rec_text_frame.grid(row=0, column=2)
button_request = tk.Button(rec_text_frame, width=21, height=3, text="추천챔피언")
button_request.pack()

champion_list = ['가렌', '갈리오', '갱플랭크', '그라가스', '그레이브즈', '나르', '나미', '나서스', '노틸러스', '녹턴', '누누', '니달리', '니코', '다리우스',
                 '다이애나', '드레이븐', '라이즈', '라칸', '람머스', '럭스', '럼블', '레넥톤', '레오나', '렉사이', '렝가', '루시안', '룰루', '르블랑', '리 신',
                 '리븐', '리산드라', '릴리아', '마스터 이', '마오카이', '말자하', '말파이트', '모데카이저', '모르가나', '문도 박사', '미스 포츈', '바드', '바루스',
                 '바이', '베이가', '베인', '벨코즈', '볼리베어', '브라움', '브랜드', '블라디미르', '블리츠크랭크', '빅토르', '뽀삐', '사미라', '사이온', '사일러스',
                 '샤코', '세나', '세라핀', '세주아니', '세트', '소나', '소라카', '쉔', '쉬바나', '스웨인', '스카너', '시비르', '신 짜오', '신드라', '신지드',
                 '쓰레쉬', '아리', '아무무', '아우렐리온 솔', '아이번', '아지르', '아칼리', '아트록스', '아펠리오스', '알리스타', '애니', '애니비아', '애쉬', '야스오',
                 '에코', '엘리스', '오공', '오른', '오리아나', '올라프', '요네', '요릭', '우디르', '우르곳', '워윅', '유미', '이렐리아', '이블린', '이즈리얼',
                 '일라오이', '자르반 4세', '자야', '자이라', '자크', '잔나', '잭스', '제드', '제라스', '제이스', '조이', '직스', '진', '질리언', '징크스',
                 '초가스', '카르마', '카밀', '카사딘', '카서스', '카시오페아', '카이사', '카직스', '카타리나', '칼리스타', '케넨', '케이틀린', '케인', '케일',
                 '코그모', '코르키', '퀸', '클레드', '키아나', '킨드레드', '타릭', '탈론', '탈리야', '탐 켄치', '트런들', '트리스타나', '트린다미어',
                 '트위스티드 페이트', '트위치', '티모', '파이크', '판테온', '피들스틱', '피오라', '피즈', '하이머딩거', '헤카림']

image_m, button_m = [], []

for i in range(len(champion_list)):
    image_m.append(tk.PhotoImage(file='../../data/image/champion/' + champion_list[i] + '.png').zoom(zoom_size - 2).subsample(subsample_size))
canvas = tk.Canvas(m_frame)
canvas.grid(row=0, column=0, sticky="news")
scroll = tk.Scrollbar(m_frame, orient="vertical", command=canvas.yview)
scroll.grid(sticky='news', row=0, column=7)
canvas.configure(yscrollcommand=scroll.set)
frame_buttons = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

for i in range(len(champion_list)):
    button_m.append(tk.Button(frame_buttons, image=image_m[i]))
    button_m[i].grid(row=int(i / 6), column=int(i % 6))

frame_buttons.update_idletasks()
firstcolumns_width = sum([button_m[i].winfo_width() for i in range(0, 6)])
firstrows_height = sum([button_m[i].winfo_height() for i in range(0, 5)])
m_frame.config(width=firstcolumns_width + scroll.winfo_width(), height=firstrows_height)
canvas.configure(width=firstcolumns_width + scroll.winfo_width(), height=firstrows_height)
canvas.config(scrollregion=canvas.bbox("all"))

def click_champion(num):
    global select_champion_num
    select_champion_num = num

for i, v in enumerate(champion_list):
    button_m[i].config(command=lambda idx=i: click_champion(idx))

global l1_flag, l2_flag, l3_flag, l4_flag, l5_flag, r1_flag, r2_flag, r3_flag, r4_flag, r5_flag, b1_flag, b2_flag, b3_flag, b4_flag, b5_flag, b6_flag, b7_flag, b8_flag, b9_flag, b10_flag
l1_flag, l2_flag, l3_flag, l4_flag, l5_flag = 0, 0, 0, 0, 0
r1_flag, r2_flag, r3_flag, r4_flag, r5_flag = 0, 0, 0, 0, 0
b1_flag, b2_flag, b3_flag, b4_flag, b5_flag = 0, 0, 0, 0, 0
b6_flag, b7_flag, b8_flag, b9_flag, b10_flag = 0, 0, 0, 0, 0

def click_pick():
    global select_champion_num, select_line_num, select
    global l1_flag, l2_flag, l3_flag, l4_flag, l5_flag, r1_flag, r2_flag, r3_flag, r4_flag, r5_flag, b1_flag, b2_flag, b3_flag, b4_flag, b5_flag, b6_flag, b7_flag, b8_flag, b9_flag, b10_flag
    select_line_num = CheckVariety.get()
    select_user = select.get()
    if (select_user == -1):
        print('유저를 선택해주세요.')
    if (select_champion_num == -1):
        print('챔피언을 선택해주세요.')
    if (select_line_num == -1):
        print('라인을 정해주세요.')
    else:
        if (select_user == 1):
            if (not l1_flag):
                l1_line.config(text = line[select_line_num])
                l1_btn = tk.Button(l1_frame, image=image_m[select_champion_num])
                l1_btn.pack(side=tk.LEFT)
                l1_flag = 1
        elif (select_user == 2):
            if (not l2_flag):
                l2_line.config(text=line[select_line_num])
                l2_btn = tk.Button(l2_frame, image=image_m[select_champion_num])
                l2_btn.pack(side=tk.LEFT)
                l2_flag = 1
        elif (select_user == 3):
            if (not l3_flag):
                l3_line.config(text=line[select_line_num])
                l3_btn = tk.Button(l3_frame, image=image_m[select_champion_num])
                l3_btn.pack(side=tk.LEFT)
                l3_flag = 1
        elif (select_user == 4):
            if (not l4_flag):
                l4_line.config(text=line[select_line_num])
                l4_btn = tk.Button(l4_frame, image=image_m[select_champion_num])
                l4_btn.pack(side=tk.LEFT)
                l4_flag = 1
        elif (select_user == 5):
            if (not l5_flag):
                l5_line.config(text=line[select_line_num])
                l5_btn = tk.Button(l5_frame, image=image_m[select_champion_num])
                l5_btn.pack(side=tk.LEFT)
                l5_flag = 1
        elif (select_user == 6):
            if (not r1_flag):
                r1_line.config(text=line[select_line_num])
                r1_btn = tk.Button(r1_frame, image=image_m[select_champion_num])
                r1_btn.pack(side=tk.LEFT)
                r1_flag = 1
        elif (select_user == 7):
            if (not r2_flag):
                r2_line.config(text=line[select_line_num])
                r2_btn = tk.Button(r2_frame, image=image_m[select_champion_num])
                r2_btn.pack(side=tk.LEFT)
                r2_flag = 1
        elif (select_user == 8):
            if (not r3_flag):
                r3_line.config(text=line[select_line_num])
                r3_btn = tk.Button(r3_frame, image=image_m[select_champion_num])
                r3_btn.pack(side=tk.LEFT)
                r3_flag = 1
        elif (select_user == 9):
            if (not r4_flag):
                r4_line.config(text=line[select_line_num])
                r4_btn = tk.Button(r4_frame, image=image_m[select_champion_num])
                r4_btn.pack(side=tk.LEFT)
                r4_flag = 1
        elif (select_user == 10):
            if (not r5_flag):
                r5_line.config(text=line[select_line_num])
                r5_btn = tk.Button(r5_frame, image=image_m[select_champion_num])
                r5_btn.pack(side=tk.LEFT)
                r5_flag = 1
        elif (select_user == 11):
            b1_btn = tk.Button(b1_frame, image=image_m[select_champion_num])
            if (not b1_flag):
                b1_btn.pack(side=tk.LEFT)
                b1_flag = 1
        elif (select_user == 12):
            b2_btn = tk.Button(b2_frame, image=image_m[select_champion_num])
            if (not b2_flag):
                b2_btn.pack(side=tk.LEFT)
                b2_flag = 1
        elif (select_user == 13):
            b3_btn = tk.Button(b3_frame, image=image_m[select_champion_num])
            if (not b3_flag):
                b3_btn.pack(side=tk.LEFT)
                b3_flag = 1
        elif (select_user == 14):
            b4_btn = tk.Button(b4_frame, image=image_m[select_champion_num])
            if (not b4_flag):
                b4_btn.pack(side=tk.LEFT)
                b4_flag = 1
        elif (select_user == 15):
            b5_btn = tk.Button(b5_frame, image=image_m[select_champion_num])
            if (not b5_flag):
                b5_btn.pack(side=tk.LEFT)
                b5_flag = 1
        elif (select_user == 16):
            b6_btn = tk.Button(b6_frame, image=image_m[select_champion_num])
            if (not b6_flag):
                b6_btn.pack(side=tk.LEFT)
                b6_flag = 1
        elif (select_user == 17):
            b7_btn = tk.Button(b7_frame, image=image_m[select_champion_num])
            if (not b7_flag):
                b7_btn.pack(side=tk.LEFT)
                b7_flag = 1
        elif (select_user == 18):
            b8_btn = tk.Button(b8_frame, image=image_m[select_champion_num])
            if (not b8_flag):
                b8_btn.pack(side=tk.LEFT)
                b8_flag = 1
        elif (select_user == 19):
            b9_btn = tk.Button(b9_frame, image=image_m[select_champion_num])
            if (not b9_flag):
                b9_btn.pack(side=tk.LEFT)
                b9_flag = 1
        elif (select_user == 20):
            b10_btn = tk.Button(b10_frame, image=image_m[select_champion_num])
            if (not b10_flag):
                b10_btn.pack(side=tk.LEFT)
                b10_flag = 1
        button_m[select_champion_num].config(state=tk.DISABLED)
        select_champion_num = None

button_pick.config(command=lambda: click_pick())

root.mainloop()