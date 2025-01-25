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

## Directory Structure

```
DjangoApplication/
├── user_auth/
│   ├── migrations/
│   ├── templates/
│   │   ├── user_auth/
│   │   │   ├── login.html
│   │   │   ├── signup.html
│   │   │   ├── forgot_password.html
│   │   │   ├── change_password.html
│   │   │   ├── dashboard.html
│   │   │   ├── profile.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── DjangoApplication/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
```

## Implementation Details

### Models
- The `CustomUser` model extends the default `AbstractUser` to include additional fields like `joined` and `last_updated`.

### Forms
- `CustomUserCreationForm` validates unique email addresses and ensures proper password confirmation.

### Views
- Login, Signup, and Dashboard views handle user authentication and data display.
- The `dashboard` view fetches `joined` and `last_updated` dates to display on the dashboard.

### Templates
- Custom templates are used for each page. Each template extends a base layout to ensure consistency.

## Validation and Error Handling
- **Email Validation**: Prevents duplicate email addresses during signup.
- **Password Requirements**: Ensures passwords are at least 8 characters long.
- **Authentication Protection**: Restricts access to authenticated pages like the dashboard and profile.

## Notes
- Make sure to configure email settings in `settings.py` to enable password reset functionality.
- The application uses SQLite as the default database. You can switch to another database by updating the `DATABASES` configuration in `settings.py`.

## Video Demonstration
Record a video demonstrating the following:
1. Signup with a unique email.
2. Login with the registered account.
3. Access the dashboard to view user details.
4. Test the validation for duplicate email addresses during signup.
5. Change the password and log back in with the new credentials.
6. Logout functionality.

## Contact
If you encounter issues or have questions, feel free to raise them in the repository's issue tracker.
