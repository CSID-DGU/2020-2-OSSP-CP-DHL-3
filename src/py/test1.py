import tkinter as tk

x = 1024
y = 720
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

b1_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166, bg='red')
b1_frame.pack(side = tk.LEFT)
image1 = tk.PhotoImage(file="가렌.png").zoom(zoom_size).subsample(subsample_size)
tk.Button(b1_frame, text=" ", image = image1).pack()

b2_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='orange')
b2_frame.pack(side = tk.LEFT)
image2 = tk.PhotoImage(file="갈리오.png").zoom(zoom_size).subsample(subsample_size)
tk.Button(b2_frame, text=" ", image = image2).pack()

b3_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='yellow')
b3_frame.pack(side = tk.LEFT)
image3 = tk.PhotoImage(file="갱플랭크.png").zoom(zoom_size).subsample(subsample_size)
tk.Button(b3_frame, text=" ", image = image3).pack()

b4_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='green')
b4_frame.pack(side = tk.LEFT)
image4 = tk.PhotoImage(file="그라가스.png").zoom(zoom_size).subsample(subsample_size)
tk.Button(b4_frame, text=" ", image = image4).pack()

b5_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='blue')
b5_frame.pack(side = tk.LEFT)
image5 = tk.PhotoImage(file="그레이브즈.png").zoom(zoom_size).subsample(subsample_size)
tk.Button(b5_frame, text=" ", image = image5).pack()

b6_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='navy')
b6_frame.pack(side = tk.LEFT)
image6 = tk.PhotoImage(file="나르.png").zoom(zoom_size).subsample(subsample_size)
tk.Button(b6_frame, text=" ", image = image6).pack()

b7_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='blue')
b7_frame.pack(side = tk.LEFT)
image7 = tk.PhotoImage(file="나미.png").zoom(zoom_size).subsample(subsample_size)
tk.Button(b7_frame, text=" ", image = image7).pack()

b8_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='green')
b8_frame.pack(side = tk.LEFT)
image8 = tk.PhotoImage(file="나서스.png").zoom(zoom_size).subsample(subsample_size)
tk.Button(b8_frame, text=" ", image = image8).pack()

b9_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='yellow')
b9_frame.pack(side = tk.LEFT)
image9 = tk.PhotoImage(file="노틸러스.png").zoom(zoom_size).subsample(subsample_size)
tk.Button(b9_frame, text=" ", image = image9).pack()

b10_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166,  bg='orange')
b10_frame.pack(side = tk.LEFT)
image10 = tk.PhotoImage(file="녹턴.png").zoom(zoom_size).subsample(subsample_size)
tk.Button(b10_frame, text=" ", image = image10).pack()

l1_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.166, bg='orange')
l1_frame.grid(row = 1, column = 0)

l2_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.166, bg='yellow')
l2_frame.grid(row = 2, column = 0)

l3_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.166, bg='green')
l3_frame.grid(row = 3, column = 0)

l4_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.168, bg='blue')
l4_frame.grid(row = 4, column = 0)

l5_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.166, bg='red')
l5_frame.grid(row = 5, column = 0)

m_frame = tk.Frame(frame, width = x * 0.6, height = y * 0.668, bg='purple')
m_frame.grid(row = 1, column = 1, rowspan = 4)

r1_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.166, bg='orange')
r1_frame.grid(row = 1, column = 4)

r2_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.166, bg='yellow')
r2_frame.grid(row = 2, column = 4)

r3_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.166, bg='green')
r3_frame.grid(row = 3, column = 4)

r4_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.168, bg='blue')
r4_frame.grid(row = 4, column = 4)

r5_frame = tk.Frame(frame, width = x * 0.2, height = y * 0.166, bg='red')
r5_frame.grid(row = 5, column = 4)

option_frame = tk.Frame(frame, width = x * 0.6, height = y * 0.166, bg='white')
option_frame.grid(row = 5, column = 1)

line_frame = tk.Frame(option_frame, width = x * 0.61, height = y * 0.066, bg = "orange")
line_frame.grid(row = 0, column = 0)

CheckVariety=tk.IntVar()
top_btn = tk.Radiobutton(line_frame, text="탑", value = 1, width = 10, height = 3, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)
jg_btn = tk.Radiobutton(line_frame, text="정글", value = 2, width = 10, height = 3, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)
mid_btn = tk.Radiobutton(line_frame, text="미드", value = 3, width = 10, height = 3, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)
ad_btn = tk.Radiobutton(line_frame, text="원딜", value = 4, width = 10, height = 3, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)
sp_btn = tk.Radiobutton(line_frame, text="서폿", value = 5, width = 10, height = 3, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)

choice_frame = tk.Frame(option_frame, width = x * 0.6, height = y * 0.1, bg = "yellow")
choice_frame.grid(row = 1, column = 0)

rec_frame = tk.Frame(choice_frame, width = x * 0.6 * 0.33, height = y * 0.1, bg = "green")
rec_frame.grid(row = 0, column = 0)
tk.Button(rec_frame, width = 21, height = 3, text="추천받기").pack()

select_frame = tk.Frame(choice_frame, width = x * 0.6 * 0.34, height = y * 0.1, bg = "yellow")
select_frame.grid(row = 0, column = 1)
tk.Button(select_frame, width = 26, height = 3, text="선택하기").pack()

rec_text_frame = tk.Frame(choice_frame, width = x * 0.6 * 0.328, height = y * 0.1, bg = "navy")
rec_text_frame.grid(row = 0, column = 2)
tk.Button(rec_text_frame, width = 21, height = 3, text="추천챔피언").pack()

champion_list = ['가렌', '갈리오', '갱플랭크', '그라가스', '그레이브즈', '나르', '나미', '나서스', '노틸러스', '녹턴', '누누', '니달리', '니코', '다리우스',
                 '다이애나', '드레이븐', '라이즈', '라칸', '람머스', '럭스', '럼블', '레넥톤', '레오나', '렉사이', '렝가', '루시안', '룰루', '르블랑', '리 신',
                 '리븐', '리산드라', '릴리아', '마스터이', '마오카이', '말자하', '말파이트', '모데카이저', '모르가나', '문도 박사', '미스 포츈', '바드', '바루스',
                 '바이', '베이가', '베인', '벨코즈', '볼리베어', '브라움', '브랜드', '블라디미르', '블리츠크랭크', '빅토르', '뽀삐', '사미라', '사이온', '사일러스',
                 '샤코', '세나', '세라핀', '세주아니', '세트', '소나', '소라카', '쉔', '쉬바나', '스웨인', '스카너', '시비르', '신 짜오', '신드라', '신지드',
                 '쓰레쉬', '아리', '아무무', '아우렐리온 솔', '아이번', '아지르', '아칼리', '아트록스', '아펠리오스', '알리스타', '애니', '애니비아', '애쉬', '야스오',
                 '에코', '엘리스', '오공', '오른', '오리아나', '올라프', '요네', '요릭', '우디르', '우르곳', '워윅', '유미', '이렐리아', '이블린', '이즈리얼',
                 '일라오이', '자르반 4세', '자야', '자이라', '자크', '잔나', '잭스', '제드', '제라스', '제이스', '조이', '직스', '진', '질리언', '징크스',
                 '초가스', '카르마', '카밀', '카사딘', '카서스', '카시오페아', '카이사', '카직스', '카타리나', '칼리스타', '케넨', '케이틀린', '케인', '케일',
                 '코그모', '코르키', '퀸', '클레드', '키아나', '킨드레드', '타릭', '탈론', '탈리야', '탐 켄치', '트런들', '트리스타나', '트린다미어',
                 '트위스티드 페이트', '트위치', '티모', '파이크', '판테온', '피들스틱', '피오라', '피즈', '하이머딩거', '헤카림']

image_m = []
button_m = []

for i in range(len(champion_list)):
    image_m.append(tk.PhotoImage(file=champion_list[i] + '.png').zoom(zoom_size - 2).subsample(subsample_size))

canvas = tk.Canvas(m_frame)
canvas.grid(row=0, column=0, sticky="news")

scroll = tk.Scrollbar(m_frame, orient="vertical", command=canvas.yview)
scroll.grid(sticky='news', row=0, column=7)

canvas.configure(yscrollcommand=scroll.set)

frame_buttons = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')
selected = 0

def test(champ_idx):
    print(champ_idx, 'clicked');
for i in range(len(champion_list)):
    button_m.append(tk.Button(frame_buttons, image=image_m[i], command = lambda: test(i)))
    button_m[i].grid(row=int(i / 6), column=int(i % 6))

frame_buttons.update_idletasks()

firstcolumns_width = sum([button_m[i].winfo_width() for i in range(0, 6)])
firstrows_height = sum([button_m[i].winfo_height() for i in range(0, 5)])
m_frame.config(width=firstcolumns_width + scroll.winfo_width(), height=firstrows_height)
canvas.configure(width=firstcolumns_width + scroll.winfo_width(), height=firstrows_height)

canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
