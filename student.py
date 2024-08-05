import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import csv


def open_file():
    """Opens a CSV file and displays its contents in the listbox."""
    global filename
    filename = filedialog.askopenfilename(
        defaultextension=".csv",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*")),
    )
    if filename:
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                listbox.delete(0, tk.END)
                for row in reader:
                    listbox.insert(tk.END, row)
        except Exception as e:
            error_label.config(text=f"Error opening file: {e}")

def save_file():
    """Saves the data in the listbox to a CSV file."""
    global filename
    if filename:
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                for i in range(listbox.size()):
                    writer.writerow(listbox.get(i))
            error_label.config(text="File saved successfully!")
        except Exception as e:
            error_label.config(text=f"Error saving file: {e}")
    else:
        save_as_file()

def save_as_file():
    """Saves the data in the listbox to a new CSV file."""
    global filename
    filename = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*")),
    )
    if filename:
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                for i in range(listbox.size()):
                    writer.writerow(listbox.get(i))
            error_label.config(text="File saved successfully!")
        except Exception as e:
            error_label.config(text=f"Error saving file: {e}")

def add_data():
    """Adds a new student record to the listbox."""
    new_data = [
        name_entry.get(),
        roll_entry.get(),
        science_entry.get(),
        maths_entry.get(),
        percentage_entry.get(),
    ]
    listbox.insert(tk.END, new_data)
    clear_entries()

def clear_entries():
    """Clears all entry fields."""
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    science_entry.delete(0, tk.END)
    maths_entry.delete(0, tk.END)
    percentage_entry.delete(0, tk.END)


def delete_data():
    """Deletes the selected student record from the listbox."""
    try:
        selection = listbox.curselection()
        if selection:
            listbox.delete(selection[0])
        else:
            error_label.config(text="Please select a record to delete.")
    except Exception as e:
        error_label.config(text=f"Error deleting record: {e}")

def update_data():
    """Updates the selected student record with the data in the entry fields."""
    try:
        selection = listbox.curselection()
        if selection:
            listbox.delete(selection[0])
            updated_data = [
                name_entry.get(),
                roll_entry.get(),
                science_entry.get(),
                maths_entry.get(),
                percentage_entry.get(),
            ]
            listbox.insert(selection[0], updated_data)
            clear_entries()
        else:
            error_label.config(text="Please select a record to update.")
    except Exception as e:
        error_label.config(text=f"Error updating record: {e}")

# Create main window
window = tk.Tk()
window.title("Student Information and Marks Logger")
window.configure(bg="lightgreen")

# Create labels and entry fields for student information
name_label = tk.Label(window, text="Name:", bg="lightgreen")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=5, pady=5)

roll_label = tk.Label(window, text="RollNumber:", bg="lightgreen")
roll_label.grid(row=1, column=0, padx=5, pady=5)
roll_entry = tk.Entry(window)
roll_entry.grid(row=1, column=1, padx=5, pady=5)

science_label = tk.Label(window, text="Science_Marks:", bg="lightgreen")
science_label.grid(row=0, column=2, padx=5, pady=5)
science_entry = tk.Entry(window)
science_entry.grid(row=0, column=3, padx=5, pady=5)

maths_label = tk.Label(window, text="Maths_Marks:", bg="lightgreen")
maths_label.grid(row=1, column=2, padx=5, pady=5)
maths_entry = tk.Entry(window)
maths_entry.grid(row=1, column=3, padx=5, pady=5)

percentage_label = tk.Label(window, text="Percentage:", bg="lightgreen")
percentage_label.grid(row=2, column=2, padx=5, pady=5)
percentage_entry = tk.Entry(window)
percentage_entry.grid(row=2, column=3, padx=5, pady=5)

# Create a listbox to display student records
listbox = tk.Listbox(window, width=50, height=10)
listbox.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

# Create buttons for file operations
open_button = tk.Button(window, text="Open", command=open_file, bg="lightblue")
open_button.grid(row=4, column=1, padx=5, pady=5)
save_button = tk.Button(window, text="Save", command=save_file, bg="lightblue")
save_button.grid(row=4, column=3, padx=5, pady=5)

# Create buttons for data manipulation
add_button = tk.Button(window, text="Update/Add", command=add_data, bg="lightblue")
add_button.grid(row=4, column=2, padx=5, pady=5)
delete_button = tk.Button(window, text="Delete", command=delete_data, bg="lightblue")
delete_button.grid(row=4, column=0, padx=5, pady=5)

edit_button = tk.Button(window, text="Edit", command=update_data, bg="lightblue")
edit_button.grid(row=5, column=1, padx=5, pady=5)

# Create a label to display error messages
error_label = tk.Label(window, text="", fg="red", bg="lightgreen")
error_label.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

# Initialize filename variable
filename = None

# Run the main loop
window.mainloop()