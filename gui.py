import tkinter as tk
from WeatherToSong import getSong
import webbrowser
from PIL import ImageTk, Image
import urllib.request

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("530x600")
        self.master.resizable(0, 0)
        self.pack()
        self.create_widgets()
        self.city = None
        self.tempRequest = None
        self.weatherApi = None
        self.path = None
        self.songUri = None
        self.imageUrl = None

    def create_widgets(self):
        self.createLabels()
        self.createButton()

    def createLabels(self):
        self.cityLabel = tk.Label(self.master, text="Enter a City and Country")
        self.cityEntry = tk.Entry(self.master, width=30)
        self.cityLabel.place(x=10, y=20)
        self.cityEntry.place(x=150, y=20)

        self.tempOption = tk.Label(self.master, text="Do you want to use the Temperature? Y/N")
        self.tempEntry = tk.Entry(self.master, width=10)
        self.tempOption.place(x=10, y=60)
        self.tempEntry.place(x=240, y=60)

        self.apiLabel = tk.Label(self.master, text="Input Weather API Key")
        self.apiEntry = tk.Entry(self.master, width=40)
        self.apiLabel.place(x=10, y=100)
        self.apiEntry.place(x=140, y=100)

        self.pathLabel = tk.Label(self.master, text="Input PATH for browser")
        self.pathEntry = tk.Entry(self.master, width=60)
        self.pathLabel.place(x=10, y=140)
        self.pathEntry.place(x=150, y=140)

    def createButton(self):
        self.submit = tk.Button(self.master, text="Submit Info", activebackground="green", activeforeground="pink",
                                command=self.submitData)
        self.submit.place(relx=0.5, y=180, anchor="center")

    def submitData(self):
        self.city = self.cityEntry.get()
        self.tempRequest = self.tempEntry.get()
        self.weatherApi = self.apiEntry.get()
        self.path = self.pathEntry.get()

        self.songUri, self.imageUrl = getSong(cityAndCountry=self.city, useTemp=self.tempRequest, key=self.weatherApi)
        self.printPicture()

        self.cityEntry.delete(0, 'end')
        self.tempEntry.delete(0, 'end')

    def printPicture(self):
        urllib.request.urlretrieve(self.imageUrl, "image.jpg")
        picture = Image.open("image.jpg")
        self.image = ImageTk.PhotoImage(picture)

        self.spotifyPicture = tk.Label(self.master, image=self.image)
        self.spotifyPicture.place(relx=0.5, y=360, anchor="center")

        self.playButton = tk.Button(self.master, text="Play Song", activebackground="blue", activeforeground="pink",
                                    background="white", command=self.playSong)

        self.playButton.place(relx=0.5, y=540, anchor="center")

    def playSong(self):
        website = f"open.spotify.com/track/{self.songUri}"

        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(self.path))
        webbrowser.get('chrome').open_new_tab(website)


root = tk.Tk()
app = Application(master=root)
app.mainloop()