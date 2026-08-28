import tkinter as tk
from pathlib import Path
from tkinter import messagebox
import json

notes_dir = Path.home() / ".xtodo"
notes_dir.mkdir(exist_ok=True)

json_path = notes_dir / "data.json"

try:
    with open(json_path, "r") as file:
        todos = json.load(file)
except (json.JSONDecodeError, FileNotFoundError):
    todos = []


def save_todos():
    with open(json_path, "w") as file:
        json.dump(todos, file, indent=4)


def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


def add_todo():
    add_window = tk.Toplevel(root)
    add_window.title("Create Todo")
    add_window.geometry("300x150")

    add_todo_label = tk.Label(
        add_window,
        text="Enter Your New Todo Name:",
        font=("Arial", 14, "bold")
    )
    add_todo_label.pack(padx=10, pady=10)

    todo_entry = tk.Entry(add_window, width=24)
    todo_entry.pack(padx=10, pady=10)

    def confirm_todo():
        todo_name = todo_entry.get().strip()

        if todo_name:
            todos.append({
                "task": todo_name,
                "done": False
            })

            save_todos()
    
        show_todos()            

    confirm_button = tk.Button(
            add_window,
            text="Save",
            font=("Arial", 18, "bold"),
            command=confirm_todo,
            fg="White",
            bg="green",
            activebackground="darkgreen",
            activeforeground="white"
        )
    confirm_button.pack(padx=10, pady=10, side="bottom")




def show_todos():
    clear_window()

    checkbox_states = []

    tk.Label(
        root,
        text="XGTodo",
        font=("Arial", 24, "bold"),
        fg="blue"
    ).pack(padx=10, pady=10)

    if todos:

        for todo in todos:

            check_state = tk.IntVar(
                value=1 if todo["done"] else 0
            )

            checkbox_states.append(check_state)

            if todo["done"]:
                todo_font = ("Arial", 14, "overstrike")
                todo_color = "green"
            else:
                todo_font = ("Arial", 14)
                todo_color = "black"

            tk.Checkbutton(
                root,
                text=todo["task"],
                variable=check_state,
                font=todo_font,
                fg=todo_color
            ).pack(padx=10, pady=5)

    else:

        tk.Label(
            root,
            text="Nothing to show here. Add a todo to start!",
            font=("Arial", 10)
        ).pack(padx=20, pady=20)

    # -------------------------
    # EDIT TODO
    # -------------------------

    def edit_todo():

        selected_indexes = [
            index
            for index, state in enumerate(checkbox_states)
            if state.get() == 1
        ]

        if not selected_indexes:
            messagebox.showerror(
                "No Todo Selected",
                "Please check a todo before editing it."
            )
            return

        if len(selected_indexes) > 1:
            messagebox.showerror(
                "Multiple Todos Selected",
                "Please select only one todo to edit."
            )
            return

        index = selected_indexes[0]

        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Todo")
        edit_window.geometry("300x150")

        tk.Label(
            edit_window,
            text="Please Edit The Todo Name:",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        edit_entry = tk.Entry(
            edit_window,
            width=25
        )
        edit_entry.pack(pady=5)

        edit_entry.insert(
            0,
            todos[index]["task"]
        )

        def save_edit():

            new_name = edit_entry.get().strip()

            if not new_name:
                messagebox.showerror(
                    "Empty Todo",
                    "Todo name cannot be empty."
                )
                return

            todos[index]["task"] = new_name

            save_todos()

            edit_window.destroy()

            show_todos()

        tk.Button(
            edit_window,
            text="Save",
            command=save_edit,
            fg="White",
            bg="green",
            activebackground="darkgreen",
            activeforeground="white"
            
        ).pack(pady=10, side="bottom")

    # -------------------------
    # CONFIRM / UNCONFIRM
    # -------------------------

    def toggle_complete():

        selected_indexes = [
            index
            for index, state in enumerate(checkbox_states)
            if state.get() == 1
        ]

        if not selected_indexes:
            messagebox.showerror(
                "No Todo Selected",
                "Please check a todo first."
            )
            return

        for index in selected_indexes:

            todos[index]["done"] = not todos[index]["done"]

        save_todos()

        show_todos()

    # -------------------------
    # DELETE
    # -------------------------

    def delete_todos():

        selected_indexes = [
            index
            for index, state in enumerate(checkbox_states)
            if state.get() == 1
        ]

        if not selected_indexes:
            messagebox.showerror(
                "No Todo Selected",
                "Please check a todo before deleting it."
            )
            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete the selected todo?"
        )

        if answer:

            global todos

            todos = [
                todo
                for index, todo in enumerate(todos)
                if index not in selected_indexes
            ]

            save_todos()

            show_todos()

    # -------------------------
    # BOTTOM BUTTONS
    # -------------------------

    frame = tk.Frame(root)
    frame.pack(side="bottom", fill="x")

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)
    frame.grid_columnconfigure(3, weight=1)

    # Edit
    tk.Button(
        frame,
        text="Edit",
        command=edit_todo,
        fg="White",
        bg="gold",
        activebackground="dark goldenrod",
        activeforeground="white"
    ).grid(row=0, column=0, sticky="ew")

    # Add
    tk.Button(
        frame,
        text="Add todo",
        command=add_todo,
        fg="White",
        bg="blue",
        activebackground="darkblue",
        activeforeground="white"
    ).grid(row=0, column=1, sticky="ew")

    # Confirm / Unconfirm
    confirm_text = "Unconfirm" if any(
        todo["done"] for todo in todos
    ) else "Confirm"

    tk.Button(
        frame,
        text=confirm_text,
        command=toggle_complete,
        fg="White",
        bg="green",
        activebackground="darkgreen",
        activeforeground="white"
    ).grid(row=0, column=2, sticky="ew")

    # Delete
    tk.Button(
        frame,
        text="Delete",
        command=delete_todos,
        fg="White",
        bg="red",
        activebackground="darkred",
        activeforeground="white"
    ).grid(row=0, column=3, sticky="ew")




root = tk.Tk()
root.title("XGTodo")
root.geometry("300x300")

show_todos()

root.mainloop()
