from tkinter import * 
import requests

root = Tk()
root.geometry("300x200")
root.title("URL Shortner")




def change() : 
    link = linkvar.get()
    url = "https://api.apilayer.com/short_url/hash"

    payload = f"{link}".encode("utf-8")
    headers= {"apikey": "oSuyI00nLsek8z5xMbX6DOp7PHrFgrmM"}
    response = requests.request("POST", url, headers=headers, data = payload)
    result = response.json()["short_url"]
    

linkvar = StringVar()
resultvar = StringVar()

linklab = Label(root, text="Enter the link : ", font="monospace 10")

linkent = Entry(root, textvariable=linkvar)

shot = Button(root, text="Shorten", command=change)

linklab.place(relx=0.1, rely=0.2)
linkent.place(relx=0.45, rely=0.22)
root.mainloop()  