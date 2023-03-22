from tkinter import *
import tkinter.ttk as ttk
from openpyxl import load_workbook

def wid_place():
    global is_done
    if is_done == True:
        return_button.place_forget()
        title.config(text="약품 예측 프로그램")
        x = value.selection()
        for i in value.get_children():
            value.delete(i)
        value.place_forget()

    title.place(relx = 0.5, rely = 0, anchor = 'n')
    event_button.place(relx=0.12, rely=0.8, anchor="center")
    for i in range(12):
        month_button[i].place(relx=0.085 + 0.075 * i, rely=0.6, anchor="center")

def compute(n):
    global num
    global is_done

    is_done = True

    title.config(text="{}월 약품 예측".format(n+1))
    event_button.place_forget()
    for i in range(12):
        month_button[i].place_forget()

    return_button.place(relx=0.02, rely=0.04, anchor="nw")

    style = ttk.Style()
    style.configure("Treeview.Heading", font=(None, 30))

    value.config(columns=["2018", "2019","2020", "2021", "예측"], displaycolumns=["2018", "2019","2020", "2021", "예측"])
    value.place(relx=0.5, rely=0.5, anchor="center")

    value.column("#0", width=100)

    value.column("#1", width=100, anchor="center")
    value.heading("2018", text="2018", anchor="center")

    value.column("#2", width=100, anchor="center")
    value.heading("2019", text="2019", anchor="center")

    value.column("#3", width=100, anchor="center")
    value.heading("2020", text="2020", anchor="center")

    value.column("#4", width=100, anchor="center")
    value.heading("2021", text="2021", anchor="center")

    value.column("#5", width=120, anchor="center")
    value.heading("예측", text="예측", anchor="center")

    # 예측 값
    pred_value = []
    if num.get() == 1:
        temp = 1.3
    else:
        temp = 1
    print(num.get(), temp)
    for i in range(10):
        pred_value.append(round(((value_list[i+1][n+1].value + \
            value_list[i+12][n+1].value * 2 + value_list[i+23][n+1].value * 3 + value_list[i+34][n+1].value * 4) / 10) * temp))

    treelist = [("{}".format(value_list[i+1][0].value), value_list[i+1][n+1].value, \
        value_list[i+12][n+1].value, value_list[i+23][n+1].value, value_list[i+34][n+1].value, pred_value[i]) \
            for i in range(10)]

    for i in range(len(treelist)):
        value.insert('', 'end', text=treelist[i][0], values=treelist[i][1:], iid=str(i)+"번")

# 엑셀 파일 불러오기
load_wb = load_workbook("/Users/junyong/Downloads/약품정리.xlsx", data_only=True) # 디렉토리 수정
load_ws = load_wb['Sheet1']

value_list = [[] for i in range(44)]

for i, val in enumerate(load_ws):
    for j in val:
        value_list[i].append(j)



win = Tk()

# 체육대회 유무
num = IntVar()

is_done = False

win.option_add("*Font", "맑은고딕 45")
win.title("약품 예측 프로그램")
win.geometry("{}x{}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight()))

title = Label(win)
title.config(text = "약품 예측 프로그램", font = "맑은고딕 100")

event_button = Checkbutton()
event_button.config(text="체육대회", variable=num)

return_button = Button()
return_button.config(text="뒤로가기", command=wid_place)

exit_button = Button()
exit_button.config(text="닫기", command=win.destroy)
exit_button.place(relx=0.9, rely=0.8, anchor="center")

value = ttk.Treeview()

month_button = [Button() for i in range(12)]
for i in range(12):
    month_button[i].config(text="{}월".format(i+1), width=2, height=1, command=lambda i=i: compute(i))

wid_place()

win.mainloop()