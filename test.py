import random
import tkinter
def click_btn():
    label["text"] = random.choices(["강민영", "고연재", "김기태", "김명은", "김성일", "김연수", "김재일", "노도현", "류가미", "박규환", "박성빈", "박시형", "박의용", "오송화", "이범규", "이보라", "이소윤", "이여름", "이지혜", "이현도", "임성경", "임영효", "임홍선", "장은희", "정연우", "정철우", "주민석", "최지혁"])
    label.update()

root = tkinter.Tk()
root.title("뽑기 프로그램")
root.resizable(False,False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="귀멸의칼날.png")
canvas.create_image(400,300,image=gazou)

label = tkinter.Label(root,text="??", font=("Times New Roman",60), bg="white")
label.place(x=480,y=60)

button = tkinter.Button(root,text="청소당번뽑기", font=("Times New Roman", 36), fg="skyblue", command=click_btn)
button.place(x=460,y=400)
root.mainloop()
