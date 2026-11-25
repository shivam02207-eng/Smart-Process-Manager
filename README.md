
# Smart Process Manager

A simplified process management application developed
using Python and psutil on macOS.

## Features

- Display running processes
- PID and PPID
- CPU usage
- Memory usage
- Process state
- Start student-created process
- Pause process
- Resume process
- Terminate process
- Change process priority
- Display process hierarchy

## Technologies

- Python 3
- psutil
- subprocess
- macOS

## Setup

Clone:

    git clone https://github.com/YOUR-USERNAME/Smart-Process-Manager.git

Enter folder:

    cd Smart-Process-Manager

Create virtual environment:

    python3 -m venv venv

Activate:

    source venv/bin/activate

Install:

    pip install psutil

Run:

    python3 process_manager.py

## Concepts

- PID and PPID
- Process management
- Process states
- Process control
- Process hierarchy
- Scheduling priority

## Platform Note

This educational project is implemented on macOS.
It demonstrates process management through Python
and psutil. Linux-specific system calls such as fork(),
exec() and wait() are not directly implemented
in this macOS version.

## Author

Operating System Project

