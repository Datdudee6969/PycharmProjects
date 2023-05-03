import csv

import re



# Open the CSV file and read the data
with open('city-of-seattle-2012-expenditures-dollars.csv') as csvfile:
    reader = csv.DictReader(csvfile)


    # Create a dictionary to store the department and their expenses
    department_expenses = {}

    # Loop through the data and store the department name and the corresponding expense in the dictionary
    for row in reader:
        department = row['Department']
        expense = row['2012 Actual']

        # Check if the expense is not empty

        if expense:
            expense = float(expense)

            # Add the expense to the corresponding department in the dictionary
            if department in department_expenses:
                department_expenses[department] += expense
            else:
                department_expenses[department] = expense

    # Print the department name and the corresponding expense in a neat format
    for department, expense in department_expenses.items():
        # Format the expense using regex to add commas and a dollar sign
        formatted_expense = '$' + re.sub(r'(\d{3})(?=\d)', r'\1,', '{:.2f}'.format(expense))

        # Print the department name and the corresponding expense in a neat format
        print(f'Department:{department}\n{formatted_expense}\n')
