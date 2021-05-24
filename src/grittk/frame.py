import tkinter as tk
from tkinter import ttk
from . import grittk

class Frame(ttk.Frame):
    """
    Gridded Frame object based on a descriptor dictionary
    """
    def __init__(self, master, desc, l10n = {}):
        """
        Creates a gridded frame with widgets based on a descriptor dictionary
        
        :param master: Widget master object
        :param desc: Descriptor dictionary
        :param l10n: Localization dictionary to replace the text property with
        """
    
        # Initialize the frame
        super().__init__(master)
        self.master = master
        
        # Configure the frame to take the entire master
        tk.Grid.rowconfigure(master, 0, weight = 1)
        tk.Grid.columnconfigure(master, 0, weight = 1)        
        self.grid(sticky = 'nwse')
        
        self.create_widgets(desc, l10n)
        self.configure_grid(desc)
        
    def create_widgets(self, desc, l10n):
        # Create widgets
        self.widgets = grittk.create_widgets(self, desc['widgets'], 
                              default_args = desc['default_args'], 
                              default_grid_args = desc['default_grid_args'],
                              l10n = l10n)
        
    def configure_grid(self, desc):
        # Configure the grid
        grittk.configure_grid(self, desc['grid'])
        
if __name__ == '__main__':
    import sys
    from .loader import load
    
    if len(sys.argv) < 2:
        print('Usage: %s <descriptor.yaml> [<l10n.yaml>]' % sys.argv[0])
        sys.exit(1)
    
    desc = load(open(sys.argv[1]))
    l10n = load(open(sys.argv[2])) if len(sys.argv) > 2 else {}
    
    root = tk.Tk()
    root.title(l10n.get('title', sys.argv[1]))
    app = Frame(master = root, desc = desc, l10n = l10n)
    app.mainloop()
    