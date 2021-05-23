import tkinter as tk
from tkinter import ttk

widget_mapping = {key : getattr(ttk, key) for key in (
    'Button', 
    'Checkbutton', 
    'Entry', 
    'Frame', 
    'Label', 
    'LabelFrame', 
    'Menubutton', 
    'PanedWindow', 
    'Radiobutton', 
    'Scale', 
    'Scrollbar', 
    'Spinbox', 
    'Combobox', 
    'Notebook', 
    'Progressbar', 
    'Separator', 
    'Sizegrip', 
    'Treeview', 
    )
}

def create_widgets(master, desc, default_args = {}, default_grid_args = {}, 
                   l10n = {}):
    """
    Creates gridded widgets based on a descriptor dictionary
    
    :param master: Widget master object
    :param desc: Descriptor dictionary
    :param default_args: Default arguments to pass to the widget constructors
    :param default_grid_args: Default arguments to pass to the grid method
    :param l10n: Localization dictionary to replace the text property with
    :returns: Dictionary of widgets
    """
    
    widgets = {}
    for row, row_desc in enumerate(desc):
        for name, widget_desc in row_desc.items():
            # Merge arguments for this widget
            args = {**default_args, **widget_desc['args']};
            if 'text' in args: # Implement localization
                args['text'] = l10n.get(args['text'], args['text'])
            
            # Create and grid the widget
            widget = widget_mapping[widget_desc['type']](master, **args)
            widget.grid(row = row, **{**default_grid_args, **widget_desc.get('grid', {})})
            
            widgets[name] = widget
            
    return widgets

def configure_grid(master, grid_config):
    """
    Configure a Tkinter object grid
    
    :param master: Widget master obejct
    :param grid_config: Grid configuration
    """
    cols, rows = master.grid_size()
    for col in range(cols):
        tk.Grid.columnconfigure(master, col, **{**grid_config['columns'].get('default', {}),
                                                **grid_config['columns'].get(col, {})})
    for row in range(rows):
        tk.Grid.rowconfigure(master, row, **{**grid_config['rows'].get('default', {}), 
                                             **grid_config['rows'].get(row, {})})