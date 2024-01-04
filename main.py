import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import seaborn as sns

insta=pd.read_csv('social media influencers - instagram.csv')

import re
def convert(x):
    return re.findall('\d+\.?\d*',x)

def change(file,list1):
    for i in list1:
        file['New '+i]=file[i].apply(convert)
        file['New '+i]=file['New '+i].apply(lambda x: "".join(x))
        file['New '+i]=pd.to_numeric(file['New '+i])
        file['New '+i]=np.where(['M' in j for j in file[i]],file['New '+i]*1000000,
                                np.where(['K' in j1 for j1 in file[i]],file['New '+i]*1000,file['New '+i]))
    return file

insta.head(2)
insta.isnull().sum()

list=['Followers','Engagement avg\r\n']
change(insta,list)

def mostfollowed():
    plt.figure(figsize=(15,10))
    plt.title('Top 15 most followed celebrity on Instagram\n')
    plt.xlabel('Followers in Million')
    sns.barplot(y='Instagram User',x='New Followers',data=insta.sort_values(by='New Followers',ascending=False).head(16))
    plt.show()
   
palette1=['pink','salmon','silver','darkgrey','grey','lightblue','skyblue','teal']
palette2=['lightblue','skyblue','teal','darkblue','silver','grey','darkgrey',]

def plot(file):
    plt.figure(figsize=(18,10))
    file['category'].value_counts().sort_values(ascending=True).plot.barh(color=palette1)
    plt.title("Users vs Category\n")
    plt.xlabel('\nNumber of times category occured')
    plt.ylabel('Category')
    plt.show()

def plot_c(file):
    plt.figure(figsize=(15,10))
    plt.xlabel('\nNumber of times category occured')
    plt.ylabel('Country')
    plt.title("Users vs Audience Country\n")
    file['Audience country'].value_counts().sort_values(ascending=True).plot.barh(color=palette2)
    
def b2():    
    plot(insta)
    
def b3():
    plot_c(insta)

root = tk.Tk()
root.title('PACKAGE')
frm = ttk.Frame(root,padding=150)
frm.grid()
ttk.Label(frm, text="\t  Ｉｎｓｔａｌｙｔｉｃｓ    \n\n").grid(column=0, row=0)
ttk.Label(frm, text="Celebrities with most followers :").grid(column=0, row=2)
ttk.Label(frm, text="Category of Users : ").grid(column=0, row=3)
ttk.Label(frm, text="Audience Country : ").grid(column=0, row=4)
ttk.Label(frm, text="\n\n").grid(column=0, row=5)
button1 = ttk.Button(frm, text="Show", command=mostfollowed).grid(column=1, row=2)
button2 = ttk.Button(frm, text="Show", command=b2).grid(column=1, row=3)
button3 = ttk.Button(frm, text="Show", command=b3).grid(column=1, row=4)
button4 = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=7)
root.mainloop()