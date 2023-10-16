import sqlite3
from os import system

system("cls")


class Database:
    def __init__(self, db_file_name: str):
        self.db = sqlite3.connect(f"db/{db_file_name}", check_same_thread=False)
        self.sql = self.db.cursor()

        print(f"[i] Connected new database {db_file_name}.")

    def get_tasks(self) -> list:
        self.sql.execute("SELECT * FROM todo_tasks")
        tasks = self.sql.fetchall()
        print("[i] Tasks loaded.")

        return tasks

    def create_task(self, title: str, description: str):
        if len(description):
            self.sql.execute(f"INSERT INTO todo_tasks (task_title, task_description) VALUES ('{title}', '{description}')")
        else:
            self.sql.execute(f"INSERT INTO todo_tasks (task_title) VALUES ('{title}')")

        self.db.commit()
        print(f"[i] Created new task \"{title}\".")

    def delete_task(self, _id: int):
        self.sql.execute(f"DELETE FROM todo_tasks WHERE id={_id}")
        self.db.commit()
        print(f"[i] Task number {_id} deleted successfully.")


if __name__ == '__main__':
    print("This file is not allowed to start as a main file!")
