import mysql.connector

try:
    conn = mysql.connector.connect(
        user="root",
        password="germanshepherd",
        host="localhost",
        port=3306,
        database="datamodelling",
        autocommit=True
    )
    
    if conn.is_connected():
        print("Connected!") 

except mysql.connector.Error as e:
    print("Error connecting to MySQL:", str(e))

# Creating a cursor
cur = conn.cursor()

#inserting data
try:
    cur.execute("CREATE TABLE IF NOT EXISTS students (student_id INT, name VARCHAR(30), \
                age INT, gender VARCHAR(6), subject VARCHAR(10), marks INT);")
    print("Table created successfully")
except mysql.connector.Error as e:
    print("Error creating table:", str(e))

try:
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks) \
                VALUES(%s, %s, %s, %s, %s, %s)", 
                (1, "Raj", 23, "Male", "Python", 85))
except mysql.connector.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks) \
                VALUES(%s, %s, %s, %s, %s, %s)", 
                (2, "Priya", 22, "Female", "Python", 86))
except mysql.connector.Error as e:
    print("Error: Inserting Rows")
    print(e)

#executing select statement
try:
    cur.execute("SELECT * FROM students;")
except mysql.connector.Error as e:
    print("Error: select *")
    print(e)

#fetching the rows
row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()
# Close the cursor and connection
cur.close()
conn.close()

