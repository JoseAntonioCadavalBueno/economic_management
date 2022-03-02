# economic_management
Balance sheet manager

- Requeriments:
  -  python 3.9
  -  MySQL 8.0
  -  mysql-connector-python
  -  Anaconda 3
  -  HeidiSQL
  -  Eclipse
- How to install mysql-connector-python
  - open Anaconda Prompt (anaconda3)
  - activate your env: "conda activate 'your env'"
  - write this command: "pip install mysql-connector-python"
- Create a Data Base:
  - open heidiSQL
  - import the file "bd/bd_code" or copy the code and execute in a new data base
- Connect python with SQL:
  - open the file "checkconnector.py"
  - just modify the default values with your data base values:
    - host="localhost"
    - user="username"
    - passwd="password"
    - database="name"
  - Run "checkconnector.py" for verify your connection. 
