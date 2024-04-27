import pyodbc
from PIL import Image
from io import BytesIO

# Connect to MSSQL
try:
    conn = pyodbc.connect(
        r'DRIVER={SQL Server};'
        r'SERVER=YASH-VICTUS\SQLEXPRESS;'
        r'DATABASE=image_db;'
        r'UID=sa;'
        r'PWD=1234;'
    )
    print('Database connected successfully.')

except pyodbc.Error as e:
    print(f'Database connection error: {e}')
    exit(1)

cursor = conn.cursor()

# Create a table to store images if it doesn't exist
cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Images]') AND type in (N'U'))
    CREATE TABLE Images (
        ImageID INT PRIMARY KEY IDENTITY(1,1),
        ImageData VARBINARY(MAX)
    )
''')
conn.commit()

# Define functions to interact with images in the database

def insert_image(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
    cursor.execute('INSERT INTO Images (ImageData) VALUES (?)', (image_data,))
    conn.commit()
    print('Image inserted successfully.')

def retrieve_image(image_id, output_path):
    cursor.execute('SELECT ImageData FROM Images WHERE ImageID = ?', (image_id,))
    row = cursor.fetchone()
    if row:
        image_data = row.ImageData
        image = Image.open(BytesIO(image_data))
        image.save(output_path)
        print(f'Image retrieved and saved to {output_path}.')
    else:
        print('Image not found.')

# Example usage
# Insert image
insert_image('random_image.png')

# Retrieve image
retrieve_image(17, 'output_image.png')

# Close connection
conn.close()















