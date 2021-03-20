import tkinter
from tkinter import filedialog
import eel


def get_file_path():
    root = tkinter.Tk()
    # topmost指定(最前面)
    root.attributes('-topmost', True)
    root.withdraw()
    root.lift()
    root.focus_force()
    file_path = tkinter.filedialog.askopenfilename(parent=root)
    eel.update_path(file_path)
    return 1
    



