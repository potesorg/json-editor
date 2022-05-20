import tkinter as tk
import sys
from JsonEditor import Editor, JsonEditor

if __name__ == '__main__':
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))
    width = sys.argv[1]
    height = sys.argv[2]
    root = tk.Tk()
    root.geometry(f"{width}x{height}")
    editor = Editor(root)
    editor.set_title('Config editor')
    root.mainloop()