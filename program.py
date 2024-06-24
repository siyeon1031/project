import tkinter
import tkinter.font
window = tkinter.Tk()
window.title('GOOD PM')
window.geometry('600x400+450+200')

frame1 = tkinter.Frame(window, relief='solid', bd=2)
frame1.pack(side='left',fill='both',expand=True)

frame2 = tkinter.Frame(window, relief='solid', bd=2)
frame2.pack(side='right', fill='both', expand=True)

frame3 = tkinter.Frame(frame1, relief='solid', bd=3)
frame3.grid(row=6, column=6)

#굿즈 목록
m = tkinter.Message(frame1,
                    text='굿즈 목록 (1개 선택)',
                    width=80,
                    relief='solid')

m.grid(row=5, column=6)

#함수
def func1():
    price = int(입력1.get()) * int(입력2.get()) * 10
    if cv1.get() == 1:
        price+=9000
    if cv1.get() == 2:
        price+=7000
    if cv1.get() == 3:
        price+=3000
    if cv1.get() == 4:
        price+=5000

    if 0< price < 20000:
        price+=3000
        text.config(text='(배달비 : 3000원)')
    else:
        text.config(text='')


    result.config(text='가격: ' +str(price)+'원')

#프로그램_이름
title_font = tkinter.font.Font(family='맑은 고딕',
                               size=20)

text_font= tkinter.font.Font(family='맑은 고딕',
                             size=12)
text = tkinter.Label(frame2, text= '(배달비 : 3000원)', fg='red')
text.grid(row=2, column=0, columnspan=4)

title = tkinter.Label(frame1,
                      text='GOOD PM',
                      font=title_font)

title.grid(row=0, column=0, columnspan=2)

#상품_가격
cv1 = tkinter.IntVar()
ckb1 =  tkinter.Radiobutton(frame3, text='아크릴 스탠드 - 0.9 ~',
                            variable=cv1, value=1, command=func1)

ckb2 =  tkinter.Radiobutton(frame3, text='칼선 스티커 - 0.7 ~',
                            variable=cv1, value=2, command=func1)

ckb3 =  tkinter.Radiobutton(frame3, text='그립톡 - 0.3 ~',
                            variable=cv1, value=3, command=func1)

ckb4 =  tkinter.Radiobutton(frame3, text='아크릴 키링 - 0.5 ~',
                            variable=cv1, value=4, command=func1)

ckb1.grid(row=5, column=6)
ckb2.grid(row=6, column=6)
ckb3.grid(row=7, column=6)
ckb4.grid(row=8, column=6)

#크기_입력
가로 = tkinter.Label(frame1,
                      text='가로 값:')

가로.grid(row=1, column=0)

세로 = tkinter.Label(frame1,
                      text='세로 값:')

세로.grid(row=3, column=0)

입력1 = tkinter.Entry(frame1)
입력1.grid(row=2, column=0)

입력2 = tkinter.Entry(frame1)
입력2.grid(row=4, column=0)


#계산_버튼
button = tkinter.Button(frame1, text='계산', command=func1)
button.grid(row=0, column=2)

#가격
result = tkinter.Label(frame2,
                      text='가격 : 0원',
                      font=title_font)
result.grid(row=1, column=0, columnspan=1)




window.mainloop()