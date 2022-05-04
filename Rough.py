#import
from tkinter import *
import tkinter .messagebox as mb
import sqlite3


#connecting to database
connector = sqlite3.connect('contacts.db')
cursor = connector.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS CONTACT_BOOK (S_NO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, EMAIL TEXT, PHONE_NUMBER TEXT, ADDRESS TEXT)")


#GUI window
root = Tk()
root.title("Micah's Contact Book")
root.geometry('700x550')
root.resizable(0, 0)


#color and font
lf_bg = 'Gray70'
cf_bg = 'Gray57'
rf_bg = 'Gray35'
frame_font = ("Garamond", 14)


#stringvar
name_strvar = StringVar()
phone_strvar = StringVar()
eamil_strvar = StringVar()


#creation placement
Label(root, text='CONTACT BOOK', font=("Noto Sans CJK TC", 15, "bold"), bg='Black', fg='White').pack(side=TOP, fill=X)


#framing
left_frame = Frame(root, bg=lf_bg)
left_frame.place(relx=0, relheight=1, y=30, relwidth=0.3)
center_frame = Frame(root, bg=cf_bg)
center_frame.place(relx=0.3, relheight=1, y=30, relwidth=0.3)
right_frame = Frame(root, bg=rf_bg)
right_frame.place(relx=0.6, relheight=1, y=30, relwidth=0.4)


#THE BIG BOI

