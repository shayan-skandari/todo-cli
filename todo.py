import json
import os


# 1️⃣ تابع‌ها
def show_tasks(tasks):
    for i in range(len(tasks)):
        task = tasks[i]
        if task['done']:
            mark = "☑"
        else:
            mark = "☐"
        print(f"{i + 1}. {mark} {task['title']}")


def save_tasks(tasks):
    with open("todos.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)


def load_tasks():
    try:
        with open("todos.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        os.replace("todos.json", "todos_broken.json")
        print("⚠️ todos.json was broken. Saved it as todos_broken.json")
        print("⚠️ Starting with an empty list.")
        return []


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("❌ Title can't be empty")
        return
    new_task = {"title": title, "done": False}
    tasks.append(new_task)
    save_tasks(tasks)
    print("✅ Task added")


def ask_index(tasks):
    try:
        number = int(input("Task number: "))
    except ValueError:
        print("❌ Please enter a number")
        return None

    if number < 1 or number > len(tasks):
        print("❌ No task with that number")
        return None

    return number - 1


def complete_task(tasks):
    show_tasks(tasks)
    index = ask_index(tasks)
    if index is None:
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print("✅ Task completed")


def delete_task(tasks):
    show_tasks(tasks)
    index = ask_index(tasks)
    if index is None:
        return
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"🗑️ Deleted: {removed['title']}")   



# 2️⃣ اجرای برنامه
tasks = load_tasks()

while True:
    print()
    print("===== 📝 Todo =====")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")
    choice = input("choice: ")

    if choice == "1":
        show_tasks(tasks)

    elif choice == "2":
        add_task(tasks)   

    elif choice == "3":
        complete_task(tasks) 

    elif choice == "4":
        delete_task(tasks)       
          
    elif choice == "5":
        print("goodbye 👋")
        break
    else:
        print("❌ Invalid choice")
