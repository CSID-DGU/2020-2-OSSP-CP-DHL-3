import tkinter as tk
import tkinter.messagebox
import pickle

x, y = 960, 690
zoom_size = 24
subsample_size = 30
size = str(x) + "x" + str(y)

root = tk.Tk()
root.title('리그오브레전드 챔피언 추천시스템 - DHL')
root.geometry(size)
root.resizable(False, False)
frame = tk.Frame(root, bd = 5, bg='white', relief = 'groove')
frame.pack()
b_frame = tk.Frame(frame, width = x * 1, height = y * 0.166)
b_frame.grid(row = 0, column = 0, columnspan = 5)

image_m, button_m, team1, team2, ban = [], [], [], [], []
line = [" 탑", "정글", "미드", "원딜", "서폿"]
global select_champion_num, select_line_num, select
select_champion_num, select_line_num = None, None
select = tk.IntVar()
CheckVariety = tk.IntVar()
global l1_flag, l2_flag, l3_flag, l4_flag, l5_flag, r1_flag, r2_flag, r3_flag, r4_flag, r5_flag, b1_flag, b2_flag, b3_flag, b4_flag, b5_flag, b6_flag, b7_flag, b8_flag, b9_flag, b10_flag
l1_flag, l2_flag, l3_flag, l4_flag, l5_flag, r1_flag, r2_flag, r3_flag, r4_flag, r5_flag = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
b1_flag, b2_flag, b3_flag, b4_flag, b5_flag, b6_flag, b7_flag, b8_flag, b9_flag, b10_flag = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

with open('../../data/pickle/top_dict', 'rb') as fr:
    top_dict = pickle.load(fr)
with open('../../data/pickle/jungle_dict', 'rb') as fr:
    jungle_dict = pickle.load(fr)
with open('../../data/pickle/mid_dict', 'rb') as fr:
    mid_dict = pickle.load(fr)
with open('../../data/pickle/carry_dict', 'rb') as fr:
    carry_dict = pickle.load(fr)
with open('../../data/pickle/sup_dict', 'rb') as fr:
    sup_dict = pickle.load(fr)
with open('../../data/pickle/comb_win_rate', 'rb') as fr:
    comb_win_rate = pickle.load(fr)
with open('../../data/pickle/total_win_rate', 'rb') as fr:
    total_win_rate = pickle.load(fr)
with open('../../data/pickle/champ_dict', 'rb') as fr:
    champ_dict = pickle.load(fr)
positions = [top_dict, jungle_dict, mid_dict, carry_dict, sup_dict]

b1_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b1_frame.pack(side = tk.LEFT)
tk.Radiobutton(b1_frame, value = 11, variable=select, width = 10, activebackground="blue").pack(side=tk.BOTTOM)

b2_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b2_frame.pack(side = tk.LEFT)
tk.Radiobutton(b2_frame, value = 12, variable=select, width = 10, activebackground="blue").pack(side=tk.BOTTOM)

b3_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b3_frame.pack(side = tk.LEFT)
tk.Radiobutton(b3_frame, value = 13, variable=select, width = 10, activebackground="blue").pack(side=tk.BOTTOM)

b4_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b4_frame.pack(side = tk.LEFT)
tk.Radiobutton(b4_frame, value = 14, variable=select, width = 10, activebackground="blue").pack(side=tk.BOTTOM)

b5_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b5_frame.pack(side = tk.LEFT)
tk.Radiobutton(b5_frame, value = 15, variable=select, width = 10, activebackground="blue").pack(side=tk.BOTTOM)

b6_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b6_frame.pack(side = tk.LEFT)
tk.Radiobutton(b6_frame, value = 16, variable=select, width = 10, activebackground="blue").pack(side=tk.BOTTOM)

b7_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b7_frame.pack(side = tk.LEFT)
tk.Radiobutton(b7_frame, value = 17, variable=select, width = 10, activebackground="blue").pack(side=tk.BOTTOM)

b8_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b8_frame.pack(side = tk.LEFT)
tk.Radiobutton(b8_frame, value = 18, variable=select, width = 10, activebackground="blue").pack(side=tk.BOTTOM)

b9_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b9_frame.pack(side = tk.LEFT)
tk.Radiobutton(b9_frame, value = 19, variable=select, width = 10, activebackground="blue").pack(side=tk.BOTTOM)

b10_frame = tk.Frame(b_frame, width = x * 0.1, height = y * 0.166)
b10_frame.pack(side = tk.LEFT)
tk.Radiobutton(b10_frame, value = 20, variable=select, width = 10, activebackground="blue").pack(side=tk.BOTTOM)

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

for i, _ in enumerate(line):
    tk.Radiobutton(line_frame, text=_, value=i, width=10, variable=CheckVariety, activebackground="blue").pack(side=tk.LEFT)

choice_frame = tk.Frame(option_frame, width=x * 0.6, height=y * 0.1)
choice_frame.grid(row=2, column=0)

rec_frame = tk.Frame(choice_frame, width=x * 0.6 * 0.5, height=y * 0.1)
rec_frame.grid(row=0, column=0)
button_recommend = tk.Button(rec_frame, width=25, height=3, text="추천받기", command=lambda : discriminant())
button_recommend.pack()

select_frame = tk.Frame(choice_frame, width=x * 0.6 * 0.5, height=y * 0.1)
select_frame.grid(row=0, column=1)
button_pick = tk.Button(select_frame, width=25, height=3, text="선택하기", command=lambda: click_pick())
button_pick.pack()


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

for i, v in enumerate(champion_list):
    button_m[i].config(command=lambda idx=i: click_champion(idx))


def click_champion(num):
    global select_champion_num
    select_champion_num = num

def click_pick():
    global select_champion_num, select_line_num, select
    global l1_flag, l2_flag, l3_flag, l4_flag, l5_flag, r1_flag, r2_flag, r3_flag, r4_flag, r5_flag, b1_flag, b2_flag, b3_flag, b4_flag, b5_flag, b6_flag, b7_flag, b8_flag, b9_flag, b10_flag
    select_line_num = CheckVariety.get()
    select_user = select.get()
    if (select_user == -1):
        tk.messagebox.showwarning("메시지 상자", "유저를 선택해주세요.")
    if (select_champion_num == -1):
        tk.messagebox.showwarning("메시지 상자", "챔피언을 선택해주세요.")
    if (select_line_num == -1):
        tk.messagebox.showwarning("메시지 상자", "라인을 선택해주세요.")
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
        if (1 <= select_user and select_user <= 5):
            team1.append([champion_list[select_champion_num], select_line_num])
        elif (6 <= select_user and select_user <= 10):
            team2.append([champion_list[select_champion_num], select_line_num])
            ban.append(champion_list[select_champion_num])
        elif (11 <= select_user and select_user <= 20):
            ban.append(champion_list[select_champion_num])
        button_m[select_champion_num].config(state=tk.DISABLED)
        select_champion_num = None

def discriminant():
    my_position = CheckVariety.get()
    추천갯수 = 10
    enemy_position = my_position  # 적 포지션 = 내 포지션
    position_dict = {}
    if my_position == 0:
        comb_position = 1  # 탑 -> 정글
        position_dict = positions[0]

    elif my_position == 1:
        comb_position = 0  # 정글 + 미드
        comb_position2 = 2 # 정글 + 탑
        position_dict = positions[1]

    elif my_position == 2:
        comb_position = 1  # 미드 + 정글
        position_dict = positions[2]

    elif my_position == 3:
        comb_position = 4  # 원딜 + 서폿
        position_dict = positions[3]

    elif my_position == 4:
        comb_position = 3  # 서폿 + 원딜
        position_dict = positions[4]

    if not my_position == 1:
        # 정글이 아닌경우
        아군존재, 상대존재 = False, False
        아군, 아군2, 상대 = [], [], []
        출력 = "추천하는 챔피언은 다음과 같습니다. \n\n"

        for pick in team1:  # 아군 존재
            if pick[1] == comb_position:
                아군존재 = True
                아군 = pick.copy()

        for pick in team2:  # 적군 존재
            if pick[1] == enemy_position:
                상대존재 = True
                상대 = pick.copy()
        if 아군:
            아군[0] = champ_dict[아군[0]]
        if 상대:
            상대[0] = champ_dict[상대[0]]
        if 아군존재 and 상대존재:  # 아군o 상대o다  ----------------- 밴안본
            아군승률 = dict(comb_win_rate.loc[아군[0]][:])
            상대승률 = dict(total_win_rate.loc[상대[0]][:])

            추천픽리스트1, 추천픽리스트2, 최종추천, 리얼최종추천 = [], [], [], []
            for k, v in 아군승률.items():
                추천픽리스트1.append([k, v])

            for k, v in 상대승률.items():
                추천픽리스트2.append([k, round(1 - v, 4)])

            for 픽 in zip(추천픽리스트1, 추천픽리스트2):
                최종추천.append([픽[0][0], 픽[0][1] * 픽[1][1]])

            최종추천.sort(key=lambda x: x[1], reverse=True)

            for 추천픽, 승률 in 최종추천:
                if 추천픽 in list(position_dict.keys()):
                    if 추천픽 != 상대[0]:
                        리얼최종추천.append([추천픽, 승률])
            for i in range(len(리얼최종추천)):
                if 리얼최종추천[i][0] in ban:
                    del 리얼최종추천[리얼최종추천.index(i)]
            for _ in range(5):
                for key, value in champ_dict.items():
                    if value == 리얼최종추천[_][0]:
                        출력 += key + "   "
                        break ;
            tk.messagebox.showinfo("챔피언 추천 알림 / 아군o 상대o", 출력)
            print(리얼최종추천)
            print(ban)

        elif not 아군존재 and 상대존재:  # 아군x 상대o다 ------------------ 밴 안본
            상대승률 = dict(total_win_rate.loc[상대[0]][:])
            상대승률 = sorted(상대승률.items(), key=lambda x: x[1])
            추천픽리스트 = []
            n = 0
            for 추천픽, 승률 in 상대승률:
                if n == 추천갯수:  # 10개 까지 추천해줌
                    break
                if 추천픽 in list(position_dict.keys()):
                    추천픽리스트.append([추천픽, 1 - 승률])
                    n += 1
            for i in range(len(추천픽리스트)):
                if 추천픽리스트[i][0] in ban:
                    del 추천픽리스트[추천픽리스트.index(i)]
            for _ in range(5):
                for key, value in champ_dict.items():
                    if value == 추천픽리스트[_][0]:
                        출력 += key + "   "
                        break ;
            tk.messagebox.showinfo("챔피언 추천 알림 / 아군x 상대o", 출력)

        elif 아군존재 and not 상대존재:  # 아군o 상대x
            아군승률 = dict(comb_win_rate.loc[아군[0]][:])
            아군승률 = sorted(아군승률.items(), key=lambda x: x[1], reverse=True)
            추천픽리스트 = []
            n = 0
            for 추천픽, 승률 in 아군승률:
                if n == 추천갯수:
                    break ;
                if 추천픽 in list(position_dict.keys()):
                    추천픽리스트.append([추천픽, 승률])
                    n += 1
            for i in range(len(추천픽리스트)):
                if 추천픽리스트[i][0] in ban:
                    del 추천픽리스트[추천픽리스트.index(i)]
            for _ in range(5):
                for key, value in champ_dict.items():
                    if value == 추천픽리스트[_][0]:
                        출력 += key + "   "
                        break ;
            tk.messagebox.showinfo("챔피언 추천 알림 / 아군o 상대x", 출력)

        elif not (아군존재 and 상대존재):  # 아군x 상대x
            tk.messagebox.showinfo("안녕", '원하는 챔피언을 직접 선택하세요 ')
 #------------------------------------------------------------------------jungle--------------------------------------
    else: # 정글인 경우
        아군존재 = 0; 상대존재 = False
        아군, 상대 = [], []
        출력 = "추천하는 챔피언은 다음과 같습니다. \n\n"
        for pick in team1:  # 아군 존재          탑존재 1 미드존재 2 둘다존재 3
            if pick[1] == comb_position or pick[1] == comb_position2:
                if pick[1] == 0:
                    아군존재 += 1
                    아군.append(pick)
                elif pick[1] == 2:
                    아군존재 += 2
                    아군.append(pick)

        for pick in team2:  # 적군 존재
            if pick[1] == enemy_position:
                상대존재 = True
                상대 = pick.copy()

        if 아군존재 == 3 and 상대존재: # 탑O 미드O 상대O (아군2명 상대 1명 존재)봄 --------------- 밴안
            아군1승률 = dict(comb_win_rate.loc[아군[0][0]][:])
            아군2승률 = dict(comb_win_rate.loc[아군[1][0]][:])
            상대승률 = dict(total_win_rate.loc[상대[0]][:])

            추천픽리스트1, 추천픽리스트2, 추천픽리스트3, 최종추천, 리얼최종추천 = [], [], [], [], []
            for k, v in 아군1승률.items():
                추천픽리스트1.append([k, v])
            for k, v in 아군2승률.items():
                추천픽리스트2.append([k, v])
            for k, v in 상대승률.items():
                추천픽리스트3.append([k, round(1 - v, 4)])

            for 픽 in zip(추천픽리스트1, 추천픽리스트2, 추천픽리스트3):
                최종추천.append([픽[0][0], 픽[0][1] * 픽[1][1] * 픽[2][1]])

            최종추천.sort(key=lambda x: x[1], reverse=True)

            for 추천픽, 승률 in 최종추천:
                if 추천픽 in list(position_dict.keys()):
                    if 추천픽 != 상대[0]:
                        리얼최종추천.append([추천픽, 승률])
            for i in range(len(리얼최종추천)):
                if 리얼최종추천[i][0] in ban:
                    del 리얼최종추천[리얼최종추천.index(i)]
            for _ in range(5):
                for key, value in champ_dict.items():
                    if value == 리얼최종추천[_][0]:
                        출력 += key + "   "
                        break;
            tk.messagebox.showinfo("챔피언 추천 알림 / 아군o 상대o", 출력)
        elif 아군존재 == 3 and not 상대존재:  # 아군둘다o 상대x
            아군1승률 = dict(comb_win_rate.loc[아군[0][0]][:])
            아군2승률 = dict(comb_win_rate.loc[아군[1][0]][:])
            추천픽리스트1, 추천픽리스트2, 최종추천 = [], [], []
            for k, v in 아군1승률.items():
                추천픽리스트1.append([k, v])
            for k, v in 아군2승률.items():
                추천픽리스트2.append([k, v])
            for 픽 in zip(추천픽리스트1, 추천픽리스트2):
                최종추천.append([픽[0][0], 픽[0][1] * 픽[1][1]])

            최종추천.sort(key=lambda x: x[1], reverse=True)

            for i in range(len(최종추천)):
                if 최종추천[i][0] in ban:
                    del 최종추천[최종추천.index(i)]
            for _ in range(5):
                for key, value in champ_dict.items():
                    if value == 최종추천[_][0]:
                        출력 += key + "   "
                        break;
            tk.messagebox.showinfo("챔피언 추천 알림 / 아군o 상대o", 출력)

        elif 아군존재 == 0 and 상대존재:  # 아군x 상대o다
            상대승률 = dict(total_win_rate.loc[상대[0]][:])
            상대승률 = sorted(상대승률.items(), key=lambda x: x[1])
            추천픽리스트 = []
            n = 0
            for 추천픽, 승률 in 상대승률:
                if n == 추천갯수:  # 10개 까지 추천해줌
                    break
                if 추천픽 in list(position_dict.keys()):
                    추천픽리스트.append([추천픽, 1 - 승률])
                    n += 1
            for i in range(len(추천픽리스트)):
                if 추천픽리스트[i][0] in ban:
                    del 추천픽리스트[추천픽리스트.index(i)]
            for _ in range(5):
                for key, value in champ_dict.items():
                    if value == 추천픽리스트[_][0]:
                        출력 += key + "   "
                        break;
            tk.messagebox.showinfo("챔피언 추천 알림 / 아군x 상대o", 출력)

        elif (아군존재 == 1 or 아군존재 == 2) and 상대존재: # 아군 1명 상대 1명 존
            아군승률 = dict(comb_win_rate.loc[아군[0]][:])
            상대승률 = dict(total_win_rate.loc[상대[0]][:])

            추천픽리스트1, 추천픽리스트2, 최종추천, 리얼최종추천 = [], [], [], []
            for k, v in 아군승률.items():
                추천픽리스트1.append([k, v])

            for k, v in 상대승률.items():
                추천픽리스트2.append([k, round(1 - v, 4)])

            for 픽 in zip(추천픽리스트1, 추천픽리스트2):
                최종추천.append([픽[0][0], 픽[0][1] * 픽[1][1]])

            최종추천.sort(key=lambda x: x[1], reverse=True)

            for 추천픽, 승률 in 최종추천:
                if 추천픽 in list(position_dict.keys()):
                    if 추천픽 != 상대[0]:
                        리얼최종추천.append([추천픽, 승률])
            for i in range(len(리얼최종추천)):
                if 리얼최종추천[i][0] in ban:
                    del 리얼최종추천[리얼최종추천.index(i)]
            for _ in range(5):
                for key, value in champ_dict.items():
                    if value == 리얼최종추천[_][0]:
                        출력 += key + "   "
                        break;
            tk.messagebox.showinfo("챔피언 추천 알림 / 아군o 상대o", 출력)

        elif (아군존재 == 1 or 아군존재 == 2) and not 상대존재: # 아군 1명존재 상대 x
            아군승률 = dict(comb_win_rate.loc[아군[0]][:])
            아군승률 = sorted(아군승률.items(), key=lambda x: x[1], reverse=True)
            추천픽리스트 = []
            n = 0
            for 추천픽, 승률 in 아군승률:
                if n == 추천갯수:
                    break;
                if 추천픽 in list(position_dict.keys()):
                    추천픽리스트.append([추천픽, 승률])
                    n += 1
            for i in range(len(추천픽리스트)):
                if 추천픽리스트[i][0] in ban:
                    del 추천픽리스트[추천픽리스트.index(i)]
            for _ in range(5):
                for key, value in champ_dict.items():
                    if value == 추천픽리스트[_][0]:
                        출력 += key + "   "
                        break;
            tk.messagebox.showinfo("챔피언 추천 알림 / 아군o 상대x", 출력)
        else:
            tk.messagebox.showinfo("안녕", '원하는 챔피언을 직접 선택하세요 ')


root.mainloop()