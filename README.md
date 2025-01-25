# user-dashboard-app
# Django User Authentication and Dashboard Application

## Overview
This is a Django-based application that provides user authentication functionality, including features such as signup, login, password management, and a user dashboard. The app demonstrates the use of Django's built-in authentication system, forms, and templates to create a secure and user-friendly experience.

## Features

### 1. **User Authentication**
- Users can log in using their email or username and password.
- Passwords are securely hashed using Django's built-in authentication framework.

### 2. **Signup**
- Users can register with a username, email, and password.
- Includes validation to prevent duplicate email registrations.

### 3. **Forgot Password**
- Allows users to reset their password by entering their email address.
- A password reset email is sent with a link to reset their password.

### 4. **Change Password**
- Authenticated users can change their password by providing the old password and confirming the new one.

### 5. **Dashboard**
- Displays a personalized greeting for the logged-in user.
- Shows user details such as `Joined Date` and `Last Updated` date.
- Links to the profile page, change password page, and logout functionality.

### 6. **Profile Page**
- Displays user details including username, email, date joined, and last updated.

### 7. **Logout**
- Users can securely log out of the application.

## Installation Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-link>
   cd <repository-folder>
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   Access the app at [http://127.0.0.1:8000](http://127.0.0.1:8000).




## Validation and Error Handling
- **Email Validation**: Prevents duplicate email addresses during signup.
- **Password Requirements**: Ensures passwords are at least 8 characters long.
- **Authentication Protection**: Restricts access to authenticated pages like the dashboard and profile.


