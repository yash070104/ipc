FROM python:3.9

# Install psycopg2 library
RUN pip install psycopg2-binary

# Copy Python script and image file to the container
COPY adt.py C:\Users\Yash\Desktop\ade\adt.py
COPY image.png C:\Users\Yash\Desktop\ade\image.png

# Set the working directory
WORKDIR /app

# Run the Python script
CMD ["python", "adt.py"]
