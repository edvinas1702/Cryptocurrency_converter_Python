import tkinter as tk
from tkinter import ttk, W, END
import requests
import bs4



# Creating window
window = tk.Tk()
window.title("Cryptocurrency converter")
window.geometry('650x450')

count = 0


def clicked():
    global count

    count += 1

    if(count == 1):
        currentlabel.destroy()


def click():

    clicked()


    if(count % 2 != 0):

        euroLabel.grid_forget()
        dollarLabel.grid(row=1, column=0, sticky=W)

    elif(count % 2 == 0):

        dollarLabel.grid_forget()
        euroLabel.grid(row=1, column=0, sticky=W)




def convertcurrency():

    if(count == 0 or count % 2 == 0):#if Euro is chosen

        if(combobox.get() == 'Bitcoin'):
            print("BITCOIN METHOD")
            url = 'https://bitflyer.com/en-eu/bitcoin-chart'

            res = requests.get(url)

            soup = bs4.BeautifulSoup(res.text,'lxml')

            for item in soup.select(".p-currencyInfo__price"):

                value = item.text

            value = value.replace("\r", "").replace("\n", "").replace(" ","").replace(",","").replace("*EUR","")

            btc_value = float(value)

            #value of the 1st text box
            current_text_entry = int(textentry.get())

            converted_amount = current_text_entry / btc_value
            converted_amount = f'{converted_amount:.5f}'[:-1]

            textentry2.delete(0, END)
            textentry2.insert(0, converted_amount)

        elif(combobox.get() == 'Ethereum'):
            print("ETHEREUM METHOD")
            url = 'https://bitflyer.com/en-eu/ethereum-chart'

            res = requests.get(url)

            soup = bs4.BeautifulSoup(res.text,'lxml')

            for item in soup.select(".p-currencyInfo__price"):

                value = item.text

            value = value.replace("\r", "").replace("\n", "").replace(" ","").replace(",","").replace("*EUR","")

            eth_value = float(value)
            print(f'eth_value:{eth_value}')

            current_text_entry = int(textentry.get())
            print(f'current_text_entry:{current_text_entry}')

            converted_amount = current_text_entry / eth_value
            converted_amount = f'{converted_amount:.5f}'[:-1]
            print(f'converted_amount:{converted_amount}')

            textentry2.delete(0, END)
            textentry2.insert(0, converted_amount)

    elif(count % 2 != 0):#else if USD is chosen
        if(combobox.get() == 'Bitcoin'):
            print("BITCOIN METHOD")
            url = 'https://bitflyer.com/en-us/bitcoin-chart'

            res = requests.get(url)

            soup = bs4.BeautifulSoup(res.text,'lxml')

            for item in soup.select(".p-currencyInfo__price"):

                value = item.text

            value = value.replace("\r", "").replace("\n", "").replace(" ","").replace(",","").replace("*USD","")

            btc_value = float(value)

            #value of the 1st text box
            current_text_entry = int(textentry.get())

            converted_amount = current_text_entry / btc_value
            converted_amount = f'{converted_amount:.5f}'[:-1]

            textentry2.delete(0, END)
            textentry2.insert(0, converted_amount)

        elif(combobox.get() == 'Ethereum'):
            print("ETHEREUM METHOD")
            url = 'https://bitflyer.com/en-us/ethereum-chart'

            res = requests.get(url)

            soup = bs4.BeautifulSoup(res.text,'lxml')

            for item in soup.select(".p-currencyInfo__price"):

                value = item.text

            value = value.replace("\r", "").replace("\n", "").replace(" ","").replace(",","").replace("*USD","")

            eth_value = float(value)
            print(f'eth_value:{eth_value}')

            current_text_entry = int(textentry.get())
            print(f'current_text_entry:{current_text_entry}')

            converted_amount = current_text_entry / eth_value
            converted_amount = f'{converted_amount:.5f}'[:-1]
            print(f'converted_amount:{converted_amount}')

            textentry2.delete(0, END)
            textentry2.insert(0, converted_amount)




currentlabel = tk.Label(window, text="Current currency: Euros", fg="black")
currentlabel.place(relx=.0, rely=.0)


dollarLabel = tk.Label(window, text="Switched to Dollars.", fg="black")
dollarLabel.grid(row=1, column=0, sticky=W)
dollarLabel.grid_forget()

euroLabel = tk.Label(window, text="Switched to Euros.", fg="black")
euroLabel.grid(row=1, column=0, sticky=W)
euroLabel.grid_forget()


# Cryptocurrency selection label
ttk.Label(window, text = "Select cryptocurrency:").place(relx=.0, rely=.15)

#Adding a combobox
n = tk.StringVar()
combobox = ttk.Combobox(window, width = 25, textvariable = n)
combobox.place(relx=.0, rely=.202)

# Choosing values for combobox
combobox['values'] = ('Bitcoin', 'Ethereum')


# Shows Bitcoin as a default value
combobox.current(0)

tk.Button(window, text="Change your currency € / $", width=23, command=click) .place(relx=.0, rely=.05)


#1st text entry box
textentry = tk.Entry(window, width=20)
textentry.place(relx=.3, rely=.4, anchor="center")

#2nd text entry box
textentry2 = tk.Entry(window, width=20)
textentry2.place(relx=.6, rely=.4, anchor="center")


#Convert button
convertButton = tk.Button(window, text="Convert currency", width=13, command=convertcurrency)
convertButton.place(relx=.45, rely=.5, anchor="center")


window.mainloop()