import pymysql

# Connect to MySQL
conn = pymysql.connect(host='localhost', user='root', password='Root@123', database='subscribers_db')
cursor = conn.cursor()

# Test if subscribers table exists
cursor.execute("SHOW TABLES LIKE 'subscribers'")
result = cursor.fetchone()

assert result, "ERROR: subscribers table does not exist!"

# Test if subscription_date column exists (to be added in Step 6)
cursor.execute("SHOW COLUMNS FROM subscribers LIKE 'subscription_date'")
result = cursor.fetchone()

assert result, "ERROR: subscription_date column missing!"

print("All tests passed successfully!")

conn.close()
