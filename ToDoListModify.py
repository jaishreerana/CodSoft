import sqlite3

def setup_database():
    with sqlite3.connect("todo.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT CHECK(status IN ('Pending', 'Completed')) NOT NULL DEFAULT 'Pending')
        ''')
        conn.commit()

def insert_task(task_description):
    with sqlite3.connect("todo.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task_description,))
        conn.commit()
    print("✅ Task successfully added!")

def display_tasks():
    with sqlite3.connect("todo.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

    if not tasks:
        print("📌 No tasks available.")
    else:
        print("\n📜 Your Tasks:")
        print("-" * 40)
        for task in tasks:
            status_icon = "✔️" if task[2] == "Completed" else "⏳"
            print(f"🆔 {task[0]} | {task[1]} - {status_icon} {task[2]}")
        print("-" * 40)

def modify_task(task_id, new_description):
    try:
        task_id = int(task_id)
        with sqlite3.connect("todo.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (new_description, task_id))
            if cursor.rowcount == 0:
                print("❌ No task found with that ID.")
            else:
                conn.commit()
                print("🔄 Task updated successfully!")
    except ValueError:
        print("⚠️ Invalid input! Task ID must be a number.")

def remove_task(task_id):
    try:
        task_id = int(task_id)
        with sqlite3.connect("todo.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            if cursor.rowcount == 0:
                print("❌ Task ID not found.")
            else:
                conn.commit()
                print("🗑️ Task deleted successfully!")
    except ValueError:
        print("⚠️ Invalid Task ID! Please enter a valid number.")

def complete_task(task_id):
    try:
        task_id = int(task_id)
        with sqlite3.connect("todo.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET status = 'Completed' WHERE id = ?", (task_id,))
            if cursor.rowcount == 0:
                print("❌ Task ID not found.")
            else:
                conn.commit()
                print("✅ Task marked as completed!")
    except ValueError:
        print("⚠️ Invalid Task ID! Please enter a number.")

def main():
    setup_database()
    
    while True:
        print("\n📌 To-Do List Manager")
        print("1️⃣ Add New Task")
        print("2️⃣ Show All Tasks")
        print("3️⃣ Edit Task")
        print("4️⃣ Delete Task")
        print("5️⃣ Mark as Completed")
        print("6️⃣ Exit")

        choice = input("🔹 Select an option: ")

        if choice == '1':
            task = input("📝 Enter task description: ")
            insert_task(task)
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            task_id = input("✏️ Enter task ID to modify: ")
            new_task = input("🔄 Enter new task description: ")
            modify_task(task_id, new_task)
        elif choice == '4':
            task_id = input("🗑️ Enter task ID to delete: ")
            remove_task(task_id)
        elif choice == '5':
            task_id = input("✔️ Enter task ID to mark as completed: ")
            complete_task(task_id)
        elif choice == '6':
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("⚠️ Invalid option! Please try again.")

if __name__ == "__main__":
    main()
