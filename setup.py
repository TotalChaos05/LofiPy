from cx_Freeze import setup, Executable
import sys
includefiles = ['forest-dark.tcl', "forest-dark"]
includes = []
excludes = ['']
packages = ['sys', 'time', 'tkinter', 'keyboard', 'pafy', 'vlc', 'pygetwindow', 'pynput']



exe = [Executable("main.py", base = 'win32gui', icon='icon.ico')]


setup(
    name = 'LofiPy',
    version = '1.0',
    description = 'LofiPy',
    author = 'Basil',
    author_email = 'ba...@null.com',
    options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}},
    executables = exe
)