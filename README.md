# Python, SQL, HTML, CSS, JS Formatter

## Usage

- `pip install -r requirements.txt`
- `python multiple_formatter.py --files C:\Adir\Bdir\mytest.sql,D:\mtest.html,C:\HiDir\mfile.py`

## Information for Windows

- If it doesn't work even though you run it with admin privileges, try this

* `PowerShell -Command "Start-Process powershell.exe \"-command \"\"{python C:\Important\multiple_formatter.py --files C:\Adir\Bdir\mytest.sql,D:\mtest.html,C:\HiDir\mfile.py}\"\"\" -Verb RunAs"`

- Note that I specifically typed the path to the python file. If you're not sure what to write, focus here

* `PowerShell -Command "Start-Process powershell.exe \"-command \"\"!!!!!python C:\Important\multiple_formatter.py --files C:\Adir\Bdir\mytest.sql,D:\mtest.html,C:\HiDir\mfile.py!!!!!\"\"\" -Verb RunAs"`

- Remove the exclamation marks after writing the code to run.
- I know, it's still complicated but I couldn't find another way :D

## What does it do ?

- With this tool you can save your python, sql, html, css, js files and make them look nice when you open them again.
