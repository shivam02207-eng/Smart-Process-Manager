
import psutil
import subprocess

student_processes = {}

# 1. Display running processes
def display_processes():
    print("\nPID\tPPID\tCPU%\tMEM%\tSTATE\tNAME")

    for p in psutil.process_iter(
        ['pid', 'ppid', 'name', 'status', 'memory_percent']
    ):
        try:
            info = p.info
            cpu = p.cpu_percent(interval=0)

            print(
                f"{info['pid']}\t"
                f"{info['ppid']}\t"
                f"{cpu}\t"
                f"{info['memory_percent']:.2f}\t"
                f"{info['status']}\t"
                f"{info['name']}"
            )

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


# 2. Start student process
def start_process():
    p = subprocess.Popen(["sleep", "300"])
    student_processes[p.pid] = p

    print("\nStudent process started!")
    print("PID:", p.pid)


# 3. Get student-created process
def get_student_process():
    try:
        pid = int(input("Enter student process PID: "))

        if pid not in student_processes:
            print("This PID was not started by this application.")
            return None

        proc = student_processes[pid]

        if proc.poll() is not None:
            print("Process already exited.")
            student_processes.pop(pid, None)
            return None

        return psutil.Process(pid)

    except ValueError:
        print("Invalid PID.")
        return None

    except psutil.NoSuchProcess:
        print("Process not found.")
        return None


# 4. Pause process
def pause_process():
    p = get_student_process()

    if p:
        try:
            p.suspend()
            print("Process paused.")

        except psutil.Error as e:
            print("Error:", e)


# 5. Resume process
def resume_process():
    p = get_student_process()

    if p:
        try:
            p.resume()
            print("Process resumed.")

        except psutil.Error as e:
            print("Error:", e)


# 6. Terminate process
def terminate_process():
    p = get_student_process()

    if p:
        try:
            p.terminate()
            p.wait(timeout=3)

            student_processes.pop(p.pid, None)

            print("Process terminated.")

        except psutil.TimeoutExpired:
            print("Process did not exit in time.")

        except psutil.Error as e:
            print("Error:", e)


# 7. Change process priority
def change_priority():
    p = get_student_process()

    if p:
        try:
            priority = int(input("Enter nice value (-20 to 19): "))

            if not -20 <= priority <= 19:
                print("Priority must be between -20 and 19.")
                return

            p.nice(priority)
            print("Priority changed.")

        except psutil.AccessDenied:
            print("Permission denied by macOS.")

        except psutil.Error as e:
            print("Error:", e)


# 8. Display process hierarchy
def display_hierarchy():
    processes = []

    for p in psutil.process_iter(['pid', 'ppid', 'name']):
        try:
            processes.append(p.info)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    process_ids = {p['pid'] for p in processes}
    children = {}

    for p in processes:
        children.setdefault(p['ppid'], []).append(p)

    def print_tree(pid, level=0, visited=None):
        if visited is None:
            visited = set()

        for p in children.get(pid, []):
            child_pid = p['pid']

            if child_pid in visited:
                continue

            visited.add(child_pid)

            print(
                "  " * level +
                f"|-- {p['name']} (PID: {child_pid})"
            )

            print_tree(child_pid, level + 1, visited)

    print("\nPROCESS HIERARCHY\n")

    roots = [
        p for p in processes
        if p['ppid'] not in process_ids
    ]

    visited = set()

    for root in roots:
        if root['pid'] not in visited:
            visited.add(root['pid'])

            print(
                f"{root['name']} (PID: {root['pid']})"
            )

            print_tree(root['pid'], 1, visited)


# 9. Main menu
def main():
    while True:
        print("\n===== SMART PROCESS MANAGER =====")
        print("1. Display running processes")
        print("2. Start student process")
        print("3. Pause student process")
        print("4. Resume student process")
        print("5. Terminate student process")
        print("6. Change process priority")
        print("7. Display process hierarchy")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            display_processes()

        elif choice == '2':
            start_process()

        elif choice == '3':
            pause_process()

        elif choice == '4':
            resume_process()

        elif choice == '5':
            terminate_process()

        elif choice == '6':
            change_priority()

        elif choice == '7':
            display_hierarchy()

        elif choice == '8':
            for pid, proc in list(student_processes.items()):
                if proc.poll() is None:
                    proc.terminate()

            print("Application closed.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

