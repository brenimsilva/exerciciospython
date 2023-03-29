import sqlite3

banco = sqlite3.connect("banco.db");

cursor = banco.cursor();

cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)");
 
cursor.execute("INSERT INTO pessoas VALUES('Breno', 29, 'breno@teste.com')");
cursor.execute("INSERT INTO pessoas VALUES('Nícolas', 22, 'nicolas@teste.com')");

banco.commit();

cursor.execute("SELECT * FROM pessoas");
pessoas = cursor.fetchall();

print(pessoas)