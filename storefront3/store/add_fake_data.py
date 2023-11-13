import uuid
from datetime import datetime

from faker import Faker
import mysql.connector

# Connect to your MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345679',
    database='storefront2'
)

# Create a cursor object
cursor = conn.cursor()
# Create Faker instance
fake = Faker()
import secrets
import string
from django.contrib.auth.hashers import make_password

from uuid import uuid4

def generate_password(length=12):
    ans = uuid4()
    print(uuid4())
    return str(ans)
# Define the number of fake records to generate
num_records = 10

def add_users():
    # Loop to create and insert fake data into MySQL
    for _ in range(num_records):
        user_id = 1
        # username = fake.username()
        first_name = fake.first_name()
        last_name = fake.last_name()
        password = generate_password()
        last_login = str(datetime.now())
        date_joined = str(datetime.now())
        is_superuser = 0
        is_staff = 0
        email = fake.email()
        phone = fake.phone_number()
        birth_date = fake.date_of_birth().strftime('%Y-%m-%d')
        membership = fake.random_element(elements=('B', 'S', 'G'))

        ## Define an INSERT query and the data to be inserted
        insert_query = """
        INSERT INTO core_user (password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Sample data to be inserted
        data = (
            password,
            last_login,  # last_login (NULL for example)
            0,     # is_superuser (example values, should match data type)
            first_name,
            last_name,
            first_name[:3],
            0,     # is_staff (example values, should match data type)
            1,     # is_active (example values, should match data type)
            '2023-10-30 12:00:00',  # date_joined (example date and time)
            email
        )

        # Execute the INSERT query
        cursor.execute(insert_query, data)
        print(data)

add_users()
def add_customers():
    # Loop to create and insert fake data into MySQL
    for _ in range(num_records):
        user_id =1
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone = fake.phone_number()
        birth_date = fake.date_of_birth().strftime('%Y-%m-%d')
        membership = fake.random_element(elements=('B', 'S', 'G'))

        # Insert fake data into the MySQL database table
        query = """
            INSERT INTO store_customer (email, phone, birth_date, membership, user_id)
            VALUES (%s, %s, %s, %s, %s)
            """
        values = ( email, phone, birth_date, membership, user_id)
        print(values)

        cursor.execute(query, values)

# Commit the changes and close the connection
conn.commit()
conn.close()