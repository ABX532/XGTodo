import curses
import time
import os
from pathlib import Path
import keyboard
import json

todos = []

notes_dir = Path.home() / ".xtodo"
notes_dir.mkdir(exist_ok=True)
json_path = notes_dir / "data.json"

# Initialize with empty list if file doesn't exist
if not json_path.exists():
    with open(json_path, "w") as jss:
        json.dump([], jss)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def ascii_title():
    print("""\033[34m
██╗  ██╗████████╗ ██████╗ ██████╗  ██████╗ 
╚██╗██╔╝╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗
 ╚███╔╝    ██║   ██║   ██║██║  ██║██║   ██║
 ██╔██╗    ██║   ██║   ██║██║  ██║██║   ██║
██╔╝ ██╗   ██║   ╚██████╔╝██████╔╝╚██████╔╝
╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ by ABX\033[0m""")

def display_todos(todo_list):
    clear_console()
    ascii_title()
    print(f"""
    ╭──────────── \33[1mXTodo\33[0m ────────────╮
                                
    {todo_list}                            
                                
                                
                                
                                
     \033[47m[A] Add\033[0m   \033[47m[D] Delete\033[0m        
     \033[47m[E] Edit\033[0m  \033[47m[Space] Complete\033[0m
     \033[47m[Q] Quit\033[0m                  
    ╰──────────────────────────────╯""")

# Load existing todos
try:
    with open(json_path, "r") as file:
        todos = json.load(file)
except (json.JSONDecodeError, FileNotFoundError):
    todos = []

display_todos(todos)

# Main loop (you'd need to implement this properly)
while True:
    if keyboard.is_pressed('a') or keyboard.is_pressed('A'):
        todo_name = input("Please Type the Todo's name: ")
        todos.append({
            "task": todo_name,
            "done": False
        })
        
        # Write entire list back to file
        with open(json_path, "w") as file:
            json.dump(todos, file, indent=4)
        
        display_todos(todos)
        print("\033[32mThe Todo Added Succesfully!\033[0m")
        time.sleep(0.5)  # Prevent multiple triggers
    
    # Add handlers for other keys (d, e, space, q)
    if keyboard.is_pressed('q'):
        break
    
    time.sleep(0.1)  # Prevent high CPU usage