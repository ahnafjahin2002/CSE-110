def calculate_tax(age, salary, job):
    job = job.lower()
    
    if age < 18 or job == "president" or salary < 10000:
        return 0
    elif 10000 <= salary <= 20000:
        return salary * 0.05
    elif salary > 20000:
        return salary * 0.10

# Taking user input
age = int(input("Age: "))
salary = int(input("Salary: "))
job = input("Job: ")

# Function Call
print(calculate_tax(age, salary, job))