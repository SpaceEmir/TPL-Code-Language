# TPL (Table Programming Language) Programming/Coding Language
The TPL Programming/Coding Language is a programming/coding language for tables.

To make a table use the `table` function, for example:<br>
`table "Students"`<br>
This code makes a tables with a headline "Students".<br>
To make the columns use the `columns` function, for example:<br>
`columns "Name","Age","Number"`<br>
To add rows use the `row` function, for example:<br>
`row "Student1",10,135`<br>
To show the table use the `show` function.<br>
An example for a whole code:<br>
```TPL
table "Students"
columns "Name","Age","Number"
row "Student1",10,130
row "Student2",13,145
row "Student3",12,102
```
If you want to code TPL you have to follow the instructions:
1. Install Python
Go to https://www.python.org/downloads/ and download Python 3.13
And go to your terminal and write:
`python --version`
or 
`python3 --version`

2. Install TPL
Type in terminal:
`pipx install https://github.com/SpaceEmir/TPL-Code-Language.git`