import os
import tkinter as tk
from tkinter import ttk

class FileExplorerGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Explorer")
        
        # Create GUI elements
        self.path_label = ttk.Label(master, text="Enter a directory path:")
        self.path_entry = ttk.Entry(master, width=50)
        self.path_entry.focus()
        self.path_entry.bind("<Return>", self.list_dir)
        self.listbox = tk.Listbox(master, width=80)
        self.scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        
        # Grid GUI elements
        self.path_label.grid(row=0, column=0, padx=10, pady=10)
        self.path_entry.grid(row=0, column=1, padx=10, pady=10)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.scrollbar.grid(row=1, column=2, sticky=tk.NS, padx=0, pady=10)
        
        # Bind double-click on listbox to open file or directory
        self.listbox.bind("<Double-Button-1>", self.open_file_or_dir)
    
    def list_dir(self, event=None):
        """List the contents of a directory"""
        self.listbox.delete(0, tk.END)
        path = self.path_entry.get()
        if os.path.isdir(path):
            with os.scandir(path) as entries:
                for entry in entries:
                    if entry.is_file():
                        self.listbox.insert(tk.END, entry.name)
                    elif entry.is_dir():
                        self.listbox.insert(tk.END, f"[{entry.name}]")
        else:
            self.listbox.insert(tk.END, "Not a valid directory!")
    
    def open_file_or_dir(self, event=None):
        """Open a file or directory"""
        selected = self.listbox.curselection()
        if selected:
            item = self.listbox.get(selected[0])
            path = os.path.join(self.path_entry.get(), item)
            if os.path.isdir(path):
                self.path_entry.delete(0, tk.END)
                self.path_entry.insert(0, path)
                self.list_dir()
            elif os.path.isfile(path):
                os.startfile(path)

def main():
    root = tk.Tk()
    file_explorer = FileExplorerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
