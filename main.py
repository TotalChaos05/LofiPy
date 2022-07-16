import sys
import time
import tkinter as tk
import tkinter.ttk as ttk
import pygetwindow as gw
import keyboard
import pafy
import vlc
from pynput import mouse


def menu():
    window = tk.Tk()

    window.title("LofiPy")
    window.geometry('425x350')
    window.tk.call('source', 'forest-dark.tcl')
    ttk.Style().theme_use('forest-dark')

    window.resizable(False, False)

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

    op1 = ttk.Radiobutton(window,
                          style='TRadiobutton',
                          value=1,
                          text='lofi hip hop radio - beats to relax/study to',
                          variable=sel)

    op2 = ttk.Radiobutton(window,
                          style='TRadiobutton',
                          value=2, text='lofi hip hop radio - beats to sleep/chill to',
                          variable=sel)

    op3 = ttk.Radiobutton(window,
                          style='TRadiobutton',
                          value=3,
                          text='custom livestream',
                          variable=sel, )

    text_input = ttk.Entry(window,
                           exportselection=False,
                           textvariable=text)

    ok_button = ttk.Button(window,
                           style='TButton',
                           text="Ok",
                           command=ok_button_command)
    instructions = tk.Label(window,
                            text='''
A dedicated app for playing Lofi Girl's YouTube Livestreams

Esc: Exit Video Player
                            
F11: Fullscreen

Scroll Wheel: Volume Up/Down''',
                            font=("Thoma", 12))

    title = tk.Label(window,
                     text="LofiPy",
                     font=("Thoma", 44))

    title.grid(column=0, row=4, columnspan=2)

    instructions.grid(column=0, row=5, columnspan=2)
    op1.grid(column=0, row=0, sticky='w')
    op2.grid(column=0, row=1, sticky='w')
    op3.grid(column=0, row=2, sticky='w')
    text_input.grid(column=1, row=2, sticky='w')
    ok_button.grid(column=0, row=3, columnspan=2, sticky='nsew')

    window.mainloop()


def playvideo(url):
    video = pafy.new(url)
    # getting best stream
    best = video.getbest()
    # creating vlc media player object
    media = vlc.MediaPlayer(best.url)
    media.play()
    # start playing video

    desired_window_name = "VLC (Direct3D11 output)"
    # for some reason vlc doesn't like it when this isn't her

    current_window = gw.getActiveWindow().title



    def on_scroll(x, y, dx, dy):
        if desired_window_name == current_window:
            vlc.libvlc_audio_set_volume(p_mi=media, i_volume=vlc.libvlc_audio_get_volume(media) + (dy * 5))

    listener = mouse.Listener(
        on_scroll=on_scroll)
    listener.start()





    while True:
        if keyboard.is_pressed('Esc') and desired_window_name == current_window:
            print('exiting...')
            sys.exit(0)
        elif keyboard.is_pressed('f11') and desired_window_name == current_window:
            vlc.libvlc_toggle_fullscreen(p_mi=media)
            time.sleep(.5)
        else:
            try:
                current_window = gw.getActiveWindow().title
            except Exception:
                pass


            desired_window_name = "VLC (Direct3D11 output)"
            # for some reason vlc doesn't like it when this isn't here
            pass


menu()
