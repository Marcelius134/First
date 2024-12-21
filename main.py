import os
from tkinter.font import names


class Task:
    def __init__(self, Taskname, Complete=False):
        self.Complete= Complete
        self.Taskname= Taskname

    def complete(self):
        self.Complete = True

    def uncomplete(self):
        self.Complete = False

    def __str__(self):
        return f"[Completed] {self.Taskname}" if self.Complete else "[uncomplete] {self.Taskname}"





class TaskManager:
    def __init__(self, FileName ="Task.txt"):
        self.file = FileName
        self.task= []
#Görev ekleme
    def addTask(self, taskName):
        task = Task(taskName)
        self.task.append(task)
#görevin tamamlanma durumunu kontrol etme
    def CompleteTask(self, Task):
        if 0 <= Task < len(self.task):
            self.task[Task].complete()
        else:
            print("invalid number")

#görevi kaldırma
    def removeTask(self, TaskNum):
        if 0 <= TaskNum < len(self.task):
            self.task.pop(TaskNum)
            print(f"Task removed: {TaskNum}")
        else:
            print("invalid number")


#görevi gösteren def

    def showTask(self):
       if not self.task:
           print("No task")
       else:
           print("Tasks:")
           for i, task in enumerate(self.task):
                print(f"{i+1}. {task}")
#Görevleri kaydeden method
    def saveTask(self):
        with open(self.file, "w") as file:
            for task in self.task:
                file.write(f"{task}\n")

                task_status = "1" if task.Complete else "0"
                file.write(f"{task_status}\n")
                print("task saved")
#Görev yükleyen def
def loadTask(self):
    if os.path.exists(self.file):
        with open(self.file, "r") as file:
            self.tasks = []
            for line in file:
                task, status = line.split("\n")
                self.tasks.append(Task(task, status == "1"))
                print("Tasks loaded")





def main():
    manager = TaskManager()


    while True:
        print("1.Add Task")
        print("2.Complete task")
        print("3.Remove task")
        print("4.List task")
        print("5. Exit")

        ch= input("Choose your option: ")

        if ch == "1":
            task = input("Task name: ")
            manager.addTask(task)
        elif ch == "2":
            manager.showTask()
            str = int(input("Choose task number to complete: "))
            manager.completeTask(str)
        elif ch == "3":
            manager.showTask()
            str = int(input("Choose task number to remove: "))
            manager.removeTask()
        elif ch == "4":
            manager.showTask()
        elif ch == "5":
         manager.saveTask()
        print("Exiting")
        break
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()








