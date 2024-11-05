# Expense Tracker API

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Endpoints](#endpoints)
  - [User Authentication](#user-authentication)
  - [Expense Management](#expense-management)
  - [Budget Management](#budget-management)
  - [Analytics](#analytics)
- [Examples](#examples)
- [Contribution](#contribution)

---

## Overview

The Enhanced Expense Tracker API is a powerful tool for managing personal finances. It enables users to keep track of their expenses, categorize them, set budgets, and view detailed analytics over a specified time period.

## Features

- JWT-based User Authentication
- CRUD operations for managing expenses and budgets
- Category-wise breakdown of expenses
- Advanced analytics with:
  - Total expenses within a date range
  - Category-wise expenses
  - Remaining budget for each category

## Tech Stack

- **Backend**: Django, Django Rest Framework
- **Authentication**: JWT (JSON Web Tokens) for secure user authentication
- **Database**: SQLite (default, replaceable with PostgreSQL or other databases)

## Installation

### Prerequisites

- Python 3.8+
- Django 4+
- Django Rest Framework
- Django REST Framework SimpleJWT

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/TooniMike/ExpenseTracker.git
   cd expense-tracker-api
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

5. Start the server:
   ```bash
   python manage.py runserver
   ```

### Authentication

To use this API, users must authenticate via JWT. Register or log in to obtain a token, then include this token in the `Authorization` header for subsequent requests.

### Endpoints

#### User Authentication

| Method | Endpoint              | Description               |
| ------ | --------------------- | ------------------------- |
| POST   | `/api/register/`      | Register a new user       |
| POST   | `/api/token/`         | Obtain JWT token          |
| POST   | `/api/token/refresh/` | Refresh expired JWT token |

#### Expense Management

| Method | Endpoint              | Description                     |
| ------ | --------------------- | ------------------------------- |
| GET    | `/api/expenses/`      | Retrieve all expenses           |
| POST   | `/api/expenses/`      | Create a new expense            |
| GET    | `/api/expenses/<id>/` | Retrieve a single expense by ID |
| PUT    | `/api/expenses/<id>/` | Update an existing expense      |
| DELETE | `/api/expenses/<id>/` | Delete an expense               |

#### Budget Management

| Method | Endpoint             | Description               |
| ------ | -------------------- | ------------------------- |
| GET    | `/api/budgets/`      | Retrieve all budgets      |
| POST   | `/api/budgets/`      | Create a new budget       |
| GET    | `/api/budgets/<id>/` | Retrieve a budget by ID   |
| PUT    | `/api/budgets/<id>/` | Update an existing budget |
| DELETE | `/api/budgets/<id>/` | Delete a budget           |

#### Analytics

| Method | Endpoint                   | Description                                                               |
| ------ | -------------------------- | ------------------------------------------------------------------------- |
| GET    | `/api/analytics/detailed/` | Get analytics for total and category-wise expenses with remaining budgets |

### Examples

**`GET /api/analytics/detailed/?start_date=2024-01-01&end_date=2024-01-31`**
Authorization: Bearer <token>

#### Authentication

To obtain a JWT token, make a `POST` request to `/api/token/` with your username and password:

```http
POST /api/token/
Content-Type: application/json

{
    "username": "yourusername",
    "password": "yourpassword"
}

The response will include a token, which you should add to the Authorization header for authenticated requests.

#### Contribution
We welcome contributions! If you'd like to contribute to this project.
```
