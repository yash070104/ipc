import pandas as pd
from tabulate import tabulate

# Create a DataFrame with office employees data
data = {
    'employee_id': list(range(1, 61)),
    'employee_name': [
        'Akash Sharma', 'Neha Gupta', 'Rajesh Patel', 'Kiran Singh', 'Deepak Kumar',
        'Anjali Mishra', 'Rahul Verma', 'Aarti Reddy', 'Suresh Sharma', 'Priya Singh',
        'Ravi Tiwari', 'Pooja Patel', 'Vivek Singh', 'Meera Reddy', 'Sanjay Kumar',
        'Ananya Verma', 'Aruna Gupta', 'Manoj Sharma', 'Shalini Singh', 'Rohit Patel',
        'Nisha Kumar', 'Rajat Mishra', 'Mala Verma', 'Vikram Sharma', 'Shobha Singh',
        'Rajeshwari Patel', 'Gopal Singh', 'Sunita Kumar', 'Vishal Verma', 'Geeta Gupta',
        'Naveen Sharma', 'Madhu Singh', 'Amit Patel', 'Ritu Gupta', 'Arjun Verma',
        'Preeti Sharma', 'Ramesh Singh', 'Kavita Patel', 'Anil Gupta', 'Nandini Singh',
        'Alok Kumar', 'Deepika Verma', 'Prakash Sharma', 'Swati Singh', 'Manish Patel',
        'Sonam Verma', 'Sachin Singh', 'Anjali Gupta', 'Arun Kumar', 'Sneha Patel',
        'Rajendra Singh', 'Vandana Verma', 'Sudhir Sharma', 'Jyoti Singh', 'Sumit Patel',
        'Sangeeta Gupta', 'Ravi Kumar', 'Savita Verma', 'Vikas Singh', 'Poonam Patel'
    ],
    'employee_gender': ['M', 'F'] * 30,
    'employee_age': [25, 28, 32, 30, 27] * 12,
    'employee_department': [
        'HR', 'Finance', 'IT', 'Sales', 'Marketing',
    ] * 12
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(tabulate(df, headers='keys', tablefmt='psql'))

# Group by department and calculate the total age using sum
total_age_by_dept = df.groupby('employee_department')['employee_age'].sum().reset_index()
print("\nTotal Age by Department:")
print(tabulate(total_age_by_dept, headers='keys', tablefmt='psql'))

# Group by department and gender, and calculate the total age using sum
total_age_by_dept_gender = df.groupby(['employee_department', 'employee_gender'], as_index=False)['employee_age'].sum()
print("\nTotal Age by Department and Gender:")
print(tabulate(total_age_by_dept_gender, headers='keys', tablefmt='psql'))

# Group by department, gender, and age, and calculate the total age using sum
total_age_by_dept_gender_age = df.groupby(['employee_department', 'employee_gender', 'employee_age'], as_index=False)['employee_age'].sum()
print("\nTotal Age by Department, Gender, and Age:")
print(tabulate(total_age_by_dept_gender_age, headers='keys', tablefmt='psql'))
