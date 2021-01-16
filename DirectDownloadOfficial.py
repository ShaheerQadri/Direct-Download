from tkinter import *
import pytube 

#Variables
url = StringVar()

#Functions
def download():
    video_url=url.get()   #variable gathering URL from user input
    try:                #use try and catch to make sure no errors, and if errors, to make sure app doesnt crash
        youtube = pytube.Youtube(video_url)   #class is initialized

        video = youtube.streams.first       #Getting all quality streams available (HD, 360p, etc), first means get the first available 
        
        video.download("Desktop")           #Saves to desktop
        notif.conflict(fg="green", text="Video downloaded successfully")
    except Exception as e:
        print(e)
        notif.conflict(fg="red", text="Video could not be downloaded")

#For the GUI window/app
main = Tk() #Creates the GUI app.
main.title("Direct Download")         #Window Title

#Texts
Label(main, text="Youtube Direct Downloader", fg="red", font=("Arial",15)).grid(sticky=N,padx=100,row=0)  #Title
Label(main, text="Please enter the url of the video: ", font=("Arial",12)).grid(sticky=N,row=1, pady=15)  #Subtitle
notif = Label(main, font=("Arial",12))
notif.grid(sticky=N, pady=1, row=4)

#User Input
Entry(main, width=50, textvariable=url).grid(sticky=N,row=2)

#Button
Button(main, width=20, text="Download", font=("Arial",12), command=download).grid(sticky=N, row=3, pady=15)
main.mainloop()


