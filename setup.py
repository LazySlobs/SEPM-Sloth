import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name="Lazy Sloth Voice Assistant",
    version="1.0.0",
    description="Lazy Sloth Voice Assistant",
    author="Quach Gia Vi - Scrum Master- Developer - (https://github.com/s3757317)"
           "Bui Manh Dai Duong - UI/UX Designer- Developer - (https://github.com/koumi15cancer)"
           "Nguyen Bao Tri - Tester - Developer - (https://github.com/nguyenbaotri)"
           "Ha Gia Bao - Developer for Manager Directory and Voice recognition in 1st sprint - (https://github.com/baogia0912)",
    options={'build_exe': {'include_files': files}},
    executables=[target]

)