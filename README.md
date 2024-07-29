# SplitAPI -  Daily Expenses Sharing Application

## Overview

SpiltAPI is the Django based daily-expenses sharing application.This
application will allow users to add expenses and split them based on three
different methods: exact amounts, percentages, and equal splits.

## Directory Structure

```
SplitAPI/
.
├── Back end Intern Assignment (1).pdf
├── README.md
├── db.sqlite3
├── kuldeepAPI
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── admin.cpython-312.pyc
│   │   ├── apps.cpython-312.pyc
│   │   ├── models.cpython-312.pyc
│   │   ├── serializers.cpython-312.pyc
│   │   └── views.cpython-312.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-312.pyc
│   │       ├── __init__.cpython-310.pyc
│   │       └── __init__.cpython-312.pyc
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── splitapi
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-312.pyc
    │   ├── settings.cpython-312.pyc
    │   ├── urls.cpython-312.pyc
    │   └── wsgi.cpython-312.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```


This structure organizes the project's files and directories according to Django conventions.


## Getting Started

To set up and run the Django project with Django REST Framework:

1. Install Django and Django REST Framework:

    ```bash
    pip install django djangorestframework
    pip install django-filter 
    pip install markdown
    ```

2. Navigate to the project directory:

    ```bash
    cd SPILTAPI/
    ```

3. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

4. Start the development server:

    ```bash
    python manage.py runserver
    ```

5. Access the application at [http://localhost:8000/](http://localhost:8000/).

6. For the Convinience added the Requirements File 
    ```bash 
    pip install -r requirements.txt
    ```

7. For convinience create a conda enviroment with python version 3.12
    ```bash
    conda create --name Enviroment_name python=3.12. 
    ```
     






## Class Diagram

```bash
+------------------+       +-------------------+       +---------------------+       +---------------------+
|       User       |       |      Expense      |       |   ExpensePaidBy     |       |   ExpenseOwedBy     |
+------------------+       +-------------------+       +---------------------+       +---------------------+
| - userId (PK)    |       | - expenseId (PK)  |       | - userId (FK)       |       | - userId (FK)       |
| - name           |       | - desc            |       | - expenseId (FK)    |       | - expenseId (FK)    |
| - email          |       | - amount          |       | - amountPaid        |       | - amountOwed        |
| - mobileNumber   |       | - createdById (FK)|       +---------------------+       +---------------------+
+------------------+       | - createdAt       |       
                           +-------------------+
```


## Database Model

### User

- **userId**: Integer (Primary Key)
- **name**: String (255), Not Null
- **email**: String (255), Unique, Not Null
- **mobileNumber**: String (20), Not Null

### Expense

- **expenseId**: Integer (Primary Key)
- **desc**: String (255), Not Null
- **amount**: Decimal (15, 2), Not Null
- **createdById**: Integer, Not Null
- **createdAt**: Timestamp, Default: Current Timestamp

### ExpensePaidBy

- **userId**: Integer (Foreign Key to User.userId, Primary Key)
- **expenseId**: Integer (Foreign Key to Expense.expenseId, Primary Key)
- **amount**: Decimal (15, 2), Not Null

### ExpenseOwedBy

- **userId**: Integer (Foreign Key to User.userId, Primary Key)
- **expenseId**: Integer (Foreign Key to Expense.expenseId, Primary Key)
- **amount**: Decimal (15, 2), Not Null


## Entity Descriptions

### User

- **userId**: Unique identifier for each user.
- **name**: Name of the user.
- **email**: Email address of the user.
- **mobileNumber**: Mobile number of the user.

### Expense

- **expenseId**: Unique identifier for each expense.
- **desc**: Description of the expense.
- **amount**: Total amount of the expense.
- **createdById**: User ID of the creator of the expense. Default: userId = 1
- **createdAt**: Timestamp indicating when the expense was created.

### ExpensePaidBy

- **user**: User who paid for the expense.
- **expense**: Expense for which the user made a payment.
- **amountPaid**: Amount paid by the user for the expense.

### ExpenseOwedBy

- **user**: User who owes money for the expense.
- **expense**: Expense for which the user owes money.
- **amountOwed**: Amount owed by the user for the expense.

## Relationships

- The `User` entity is associated with the `UserExpensePaid` and `UserExpenseOwed` entities.
- The `Expense` entity is associated with the `UserExpensePaid` and `UserExpenseOwed` entities.


# Splitwise API Documentation

### 1. Get Users

- **Endpoint:** `/users`  
- **Method:** GET  
- **Description:** Retrieves a list of all users.  

    
- **Response Format:**
    ```json 
    "users": [
        {
        "userId": 1,
        "name": "mayank sharma",
        "email": "mayank.sharma@example.com",
        "mobileNumber": "9817147714"
        },
       
    ]
    
    ```

### 2. Add User

- **Endpoint:** `/add_user`  
- **Method:** POST  
- **Description:** Adds a new user to the system.  
- **Request Format:**
    ```json
    {
    "name": "mayank sharma",
    "email": "mayank.sharma@example.com",
    "mobileNumber": "9817147714"
    }
    ```
- **Response Format:**
    ```json
    {
    "message": "User added successfully",
    "user_id": 1,
    "name": "mayank sharma",
    "email": "mayank.sharma@example.com",
    "mobileNumber": "9817147714"
    }
    ```

### 3. Add Expense

**Equal Split**
- **Endpoint:** `/add_expense`
- **Method:** POST
- **Description:** Adds a new expense along with expense-related details.
- **Request Format:**
    ```json
    {
        "expense_type": "EXACT",
        "desc": "paytm",
        "total_amount": 600,
        "paidBy": {
            "1": 300,
            "3": 300
        },
        "owedBy": {
            "1": 100,
            "3": 200,
            "4": 300
        },
        "created_by_id" : 3
    }
    ```
- **Response Format:**
    ```json
    {
    "message": "Expense split Exact  added successfully"  
    }
    ```

**Exact Split**
- **Endpoint:** `/add_expense`
- **Method:** POST
- **Description:** Adds a new expense along with expense-related details.
- **Request Format:**
    ```json
    {
        "expense_type": "EXACT",
        "desc": "paytm",
        "total_amount": 600,
        "paidBy": {
            "1": 300,
            "3": 300
        },
        "owedBy": {
            "1": 100,
            "3": 200,
            "4": 300
        },
        "created_by_id" : 3
    }
    ```
- **Response Format:**
    ```json
    {
    "message": "Expense split exactly added successfully"  
    }
    ```

**Percent Split**
- **Endpoint:** `/add_expense`
- **Method:** POST
- **Description:** Adds a new expense along with expense-related details.
- **Request Format:**
    ```json
    {
    "expense_type": "PERCENT",
    "desc": "paytm",
    "total_amount": 700,
    "paidBy": {
        "1": 700
    },
    "owedBy": {
        "1": 20,
        "2": 33,
        "3": 47
    },
    "created_by_id" : 1
    }
    ```

- **Response Format:**
    ```json
    {
    "message": "Expense split by percentage added successfully"  
    }
    ```

### 4. Get Expenses of particular User 

**Individaul Expenses**
- **Endpoint:** `/expenses/id`
- **Method:** GET
- **Description:** Find the expenses related to the partucular Uid .
- **Response Format:**
    ```json
    
    "message": {
                "total_paid": 4600.0,
                "total_owed": 1760.0,
                "total_balance": 2840.0,
                "expenses": [
                    {}]
    }
    ```

### 5.Get Overall Expenses 

**Overall Expenses**
- **Endpoint:** `/expenses`
- **Method:** GET
- **Description:** Find the overall expenses for all the User  .
- **Response Format:**
    ```json
    {
    "message": 
                {
                "Kuldeep Gour ": 2840.0,
                "Vanshaj Duggal ": 924.0,
                "David Dan": 1016.0,
                "Rajesh Gour": 900.0
            } 
    }
    ```

### 6.Get CSV for the Expenses of all the User
**Overall Expenses**
- **Endpoint:** `/download_balance_sheet`
- **Method:** GET
- **Description:** Download the balance sheet  .










