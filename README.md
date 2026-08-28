📝 XGTodo

XGTodo is a simple, lightweight, and easy-to-use Todo List desktop application built with Python 🐍 and Tkinter 🖥️.

It provides a clean graphical interface for creating, editing, completing, and deleting your daily tasks.

✨ Features
➕ Add Todos — Create new tasks quickly.
✏️ Edit Todos — Change the name of an existing task.
✅ Complete Todos — Mark tasks as completed.
↩️ Uncomplete Todos — Change completed tasks back to pending.
🗑️ Delete Todos — Remove tasks you no longer need.
💾 Automatic Saving — Your todos are saved automatically.
📂 Persistent Storage — Todos remain available after restarting the application.
🎨 Visual Completion Status — Completed todos are displayed differently.
🪶 Lightweight — Uses only Python's standard library.
🖼️ Screenshot

🛠️ Requirements

Before running XGTodo, make sure you have:

🐍 Python 3
🖥️ Tkinter

No external Python packages are required.

📥 Installation
1️⃣ Clone the repository
git clone https://github.com/ABX532/XGTodo.git

2️⃣ Enter the project directory
cd XGTodo

3️⃣ Run XGTodo
python3 main.py


🎉 That's it! XGTodo should now open in a new window.

📋 Usage
➕ Add a Todo
Click Add Todo.
Enter your task name.
Click Confirm.
Your new Todo will be saved automatically. 💾
✅ Complete a Todo
Select a Todo using its checkbox ☑️.
Click Confirm.
The Todo will be marked as completed.

Completed tasks are displayed differently to make them easy to recognize. 🎨

↩️ Uncomplete a Todo

Changed your mind?

Select a completed Todo and use Unconfirm to mark it as incomplete again.

✏️ Edit a Todo
Select the Todo you want to edit.
Click Edit.
Change the Todo name.
Click Save. 💾
🗑️ Delete a Todo
Select one or more Todos.
Click Delete.
Confirm the deletion.

⚠️ Deleted Todos cannot be recovered.

💾 Data Storage

XGTodo stores your Todo data locally using a JSON file:

~/.xtodo/data.json


Your data is stored locally on your computer and is not uploaded to a server. 🔒

A Todo is stored in the following format:

{
    "task": "Example Todo",
    "done": false
}


Where:

📝 task — The name of the Todo.
✅ done — Whether the Todo is completed.
📁 Project Structure
XGTodo/
├── 📄 main.py
├── 🖼️ xgtodo.png
├── 📖 README.md
└── ⚖️ LICENSE

🧰 Technologies

XGTodo is built using Python's standard library:

🐍 Python 3 — Programming language
🖥️ Tkinter — Graphical User Interface
💾 JSON — Todo data storage
📂 pathlib — File and directory management
🔐 Privacy

XGTodo is a local application.

Your Todo data is stored on your own computer in:

~/.xtodo/data.json


🌐 No account is required.

☁️ No cloud service is required.

🔒 Your Todo data stays local.

🤝 Contributing

Contributions are welcome! 🎉

If you have an idea, find a bug, or want to improve XGTodo:

🍴 Fork the repository.
🌿 Create a new branch.
🛠️ Make your changes.
📤 Submit a Pull Request.

Bug reports and feature suggestions are also welcome through GitHub Issues. 💡

📜 License

XGTodo is licensed under the GNU General Public License v3.0 (GPL-3.0).

See the LICENSE file for more information.

👨‍💻 Author

Created by ABX532.

⭐ Support

If you like XGTodo, consider giving the repository a ⭐ Star on GitHub!

It helps support the project and encourages future improvements. 🚀

📝 XGTodo

Simple tasks. Simple interface. Just get things done. 🚀
