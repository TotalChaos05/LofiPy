from cx_Freeze import setup, Executable
import sys
includefiles = ['forest-dark.tcl', "forest-dark"]
includes = []
excludes = ['']
packages = ['sys', 'time', 'tkinter', 'keyboard', 'pafy', 'vlc', 'pynput']

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

setup(
    name = 'LofiPy',
    version = '1.0',
    description = 'A general enhancement utility',
    author = 'Basil',
    author_email = 'ba...@null.com',
    options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}},
    executables = [Executable('main.py', icon='icon.ico')]
)