#Importing Packages
import covid
import matplotlib.pyplot as plt
from tkinter import *

#Creating Instances
root = Tk()

# width x Height of Window
root.geometry('570x320')


#Title of window
root.title("Covid 19 Information And Update")
root.resizable(0,0)

#Title icon
root.iconbitmap('icon.ico')

#Banner Image
cover_image = PhotoImage(file='covid-19.png')
lib = Label(image=cover_image).pack()

#Label for Text
lib2 =Label(root,text="Enter The Country Name To Search....👇",font='Verdana 12 bold',fg='#666699')
lib2.pack(anchor='nw')


#Entry widget
input_value = StringVar()
entry_0 = Entry(root,bd=5,fg='Black',justify=CENTER,relief=SUNKEN,font='Verdana 10',width=55,textvariable=input_value)
entry_0.place(x=3, y=285)



#Function to check and plot the covid-19 graph
def run():
    # creating Instances
    cov = covid.Covid()

    # generating data
    country_name = input_value.get()
    virus_data = cov.get_status_by_country_name(country_name)

    # active People
    active = virus_data['active']

    # recover people
    recover = virus_data['recovered']

    # death people
    deaths = virus_data['deaths']

    # ploting the pie plot
    plt.pie([active, recover, deaths], labels=['Active', 'recovered', 'Deaths'], colors=['b', 'g', 'r'],
            explode=(0, 0, 0.2), startangle=180, autopct='%1.1f%%', shadow=True)

    # display the plot
    plt.title(country_name)
    plt.legend()
    plt.show()


#button Widget
btn = Button(root, text='Search', font='arial 10 bold', bg='pale violet red', padx=2, relief=GROOVE, borderwidth=4, activebackground='RED', command=run)
btn.place(x=490, y=282)

#Exiting the Event loop
root.mainloop()











