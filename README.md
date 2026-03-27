# TPL (Table Programming Language) Programming Language
The TPL Programming Language is a programming language for tables.

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
````
