import sys
import vlc
import pafy
import keyboard
import tkinter as tk
import tkinter.ttk as ttk
import time


def menu():
    window = tk.Tk()

    window.title("LofiPy")
    window.geometry('500x700')
    window.tk.call('source', 'forest-light.tcl')
    ttk.Style().theme_use('forest-light')

    def ok_button_command():

        choice = sel.get()
        customurl = text.get()
        window.destroy()
        if choice == 1:
            playvideo('https://www.youtube.com/watch?v=jfKfPfyJRdk')

        elif choice == 2:
            playvideo('https://www.youtube.com/watch?v=rUxyKA_-grg')

        elif choice == 3:
            playvideo(customurl)
            window.destroy()

    sel = tk.IntVar()
    text = tk.StringVar()

    op1 = ttk.Radiobutton(window, style='TRadiobutton', value=1, text='lofi hip hop radio - beats to relax/study to', variable=sel)
    op2 = ttk.Radiobutton(window, style='TRadiobutton', value=2, text='lofi hip hop radio - beats to sleep/chill to', variable=sel)
    op3 = ttk.Radiobutton(window, style='TRadiobutton', value=3, text='custom livestream', variable=sel)
    textInput = ttk.Entry(window, exportselection=False, textvariable=text)
    ok_button = ttk.Button(window, style='TButton', text="Ok", command=ok_button_command)
    instructions = tk.Text(window,)
    instructions.pack(side='right')
    instructions.insert(1.0, '''LofiPy 
                        A dedicated app for playing Lofi Girl's YouTube Livestreams
                        Esc: Exit Video Player
                        F11: Fullscreen''')
    op1.grid(column=0, row=0, sticky='w')
    op2.grid(column=0, row=1, sticky='w')
    op3.grid(column=0, row=2, sticky='w')
    textInput.grid(column=1, row=2, sticky='w')
    ok_button.grid(column=0, row=3)



    window.mainloop()


def playvideo(url):
    video = pafy.new(url)
    # getting best stream
    best = video.getbest()
    # creating vlc media player object
    media = vlc.MediaPlayer(best.url)
    # start playing video
    media.play()

    while True:
        if keyboard.is_pressed('Esc'):
            print('exiting...')
            sys.exit(0)
        elif keyboard.is_pressed('f11'):
            vlc.libvlc_toggle_fullscreen(p_mi=media)
            time.sleep(.5)
        else:
            #for some reason vlc doesn't like it when this isn't here
            pass





menu()



