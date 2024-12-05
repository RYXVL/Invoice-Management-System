# INVOICE MANAGEMENT SYSTEM

1. It is **recommended** that this software is **run on a Windows** machine as one of the libraries used (tkinter) to build this software sometimes causes unexpected results on other operating systems
2. Install python 3.11 (**https://www.python.org/downloads/**)
3. Install MySQL python connector using the command: 
```bash
pip install mysql-connector-python
```
4. Make sure before the execution of this program, that the correct **python interpreter (3.11)** is used
5. Take the dump file called **ims_dump** and dump it on workbench so the database is initialized with the data needed.
6. For initial configuration so that the software connects to the correct database on your local MySQL server successfully, please insert your username and password inside main.py’s **connection_params_tables** dictionary against the **user** and **password** keys respectively.
7. Finally to run the project, be on the project’s root folder and run the following command: 
```bash
python main.py
```