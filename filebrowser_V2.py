import tkinter as tk
import os
from tkinter import filedialog

class FileBrowser:
    def __init__(self, master):
        self.master = master
        self.master.title("File Browser")

        self.current_directory = os.getcwd()

        self.create_widgets()
        self.update_file_list()

    def create_widgets(self):
        self.file_list = tk.Listbox(self.master, width=50, height=20)
        self.file_list.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.path_label = tk.Label(self.master, text=self.current_directory)
        self.path_label.pack(side=tk.TOP, fill=tk.X)

        self.up_button = tk.Button(self.master, text="Up", command=self.go_up)
        self.up_button.pack(side=tk.LEFT)

        self.open_button = tk.Button(self.master, text="Open", command=self.open_file)
        self.open_button.pack(side=tk.LEFT)

    def update_file_list(self):
        self.file_list.delete(0, tk.END)
        for filename in os.listdir(self.current_directory):
            if os.path.isdir(os.path.join(self.current_directory, filename)):
                self.file_list.insert(tk.END, f"[DIR] {filename}")
            else:
                self.file_list.insert(tk.END, filename)

    def go_up(self):
        parent_directory = os.path.dirname(self.current_directory)
        if parent_directory:
            self.current_directory = parent_directory
            self.update_file_list()
            self.path_label.configure(text=self.current_directory)

    def open_file(self):
        selected_filename = self.file_list.get(tk.ACTIVE)
        if selected_filename:
            filepath = os.path.join(self.current_directory, selected_filename)
            if os.path.isdir(filepath):
                self.current_directory = filepath
                self.update_file_list()
                self.path_label.configure(text=self.current_directory)
            else:
                os.startfile(filepath)

def main():
    root = tk.Tk()
    file_browser = FileBrowser(root)
    root.mainloop()

if __name__ == "__main__":
    main()
