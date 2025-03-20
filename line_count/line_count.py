import os
import tkinter as tk
from tkinter import filedialog, messagebox

def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        total_lines = len(lines)
        non_empty_lines = [line for line in lines if line.strip()]
        comment_lines = [line for line in non_empty_lines if line.strip().startswith('#')]
        code_and_comment_lines = len(non_empty_lines)
        code_lines = [line for line in non_empty_lines if not line.strip().startswith('#')]
        
        return total_lines, code_and_comment_lines, len(code_lines)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0, 0, 0

def browse_files():
    files = filedialog.askopenfilenames(title="Select Files", filetypes=[("All Files", "*.*")])
    file_list.extend(files)
    update_file_display()

def remove_selected_file():
    selected_index = file_display.curselection()
    if selected_index:
        file_list.pop(selected_index[0])
        update_file_display()

def update_file_display():
    file_display.delete(0, tk.END)
    for file in file_list:
        file_display.insert(tk.END, file)

def calculate_lines():
    if not file_list:
        messagebox.showwarning("Warning", "No files selected. Please add files to analyze.")
        return
    
    if not (total_var.get() or code_comment_var.get() or code_only_var.get()):
        messagebox.showwarning("Warning", "Please select at least one option to calculate lines.")
        return
    
    total_lines_all = 0
    code_and_comment_lines_all = 0
    code_lines_all = 0

    for file in file_list:
        total, code_and_comment, code = count_lines(file)
        total_lines_all += total
        code_and_comment_lines_all += code_and_comment
        code_lines_all += code
    
    results = []
    if total_var.get():
        results.append(f"Total {total_lines_all} lines (including code, comments, and empty lines)")
    if code_comment_var.get():
        results.append(f"Total {code_and_comment_lines_all} lines of code and comments (excluding empty lines)")
    if code_only_var.get():
        results.append(f"Total {code_lines_all} lines of code (excluding comments and empty lines)")
    
    messagebox.showinfo("Results", "\n".join(results))

# GUI setup
root = tk.Tk()
root.title("Code Line Counter")

file_list = []

main_frame = tk.Frame(root)
main_frame.pack(pady=10)

file_list_frame = tk.Frame(main_frame)
file_list_frame.grid(row=0, column=0, padx=10)

tk.Label(file_list_frame, text="Selected Files:").pack()
file_display = tk.Listbox(file_list_frame, width=80, height=10)
file_display.pack()

button_frame = tk.Frame(main_frame)
button_frame.grid(row=0, column=1, padx=10)

browse_button = tk.Button(button_frame, text="Browse", command=browse_files)
browse_button.pack(fill=tk.X, pady=5)

remove_button = tk.Button(button_frame, text="Remove", command=remove_selected_file)
remove_button.pack(fill=tk.X, pady=5)

option_frame = tk.Frame(main_frame)
option_frame.grid(row=1, column=0, sticky="w", padx=15, pady=5)

total_var = tk.BooleanVar()
code_comment_var = tk.BooleanVar()
code_only_var = tk.BooleanVar()

chk_code_only = tk.Checkbutton(option_frame, variable=code_only_var)
chk_code_only.grid(row=0, column=0, pady=2)

chk_code_comment = tk.Checkbutton(option_frame, variable=code_comment_var)
chk_code_comment.grid(row=1, column=0, pady=2)

chk_total = tk.Checkbutton(option_frame, variable=total_var)
chk_total.grid(row=2, column=0, pady=2)

tk.Label(option_frame, text="Total lines of code (excluding comments and empty lines)").grid(row=0, column=1, sticky="w", padx=10)
tk.Label(option_frame, text="Total lines of code and comments (excluding empty lines)").grid(row=1, column=1, sticky="w", padx=10)
tk.Label(option_frame, text="Total lines (including code, comments, and empty lines)").grid(row=2, column=1, sticky="w", padx=10)

run_frame = tk.Frame(main_frame)
run_frame.grid(row=1, column=1, padx=10)

calculate_button = tk.Button(run_frame, text="Calculate Lines", command=calculate_lines)
calculate_button.pack(fill=tk.X, pady=10)

root.mainloop()
