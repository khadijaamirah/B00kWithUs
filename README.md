# B00kWithUs – Secure Booking Management System Web Application

## 1. Project Description
B00KWithUS is a secure web-based booking management system developed using the Django framework. The system allows users to register, authenticate, and manage bookings through a web interface, while administrators oversee system operations and user activities.

The project emphasizes secure software development practices, following the OWASP Top 10 and OWASP Application Security Verification Standard (ASVS). Multiple security controls are implemented to mitigate common web application threats such as SQL injection, cross-site scripting (XSS), broken authentication, and unauthorized access. The system adopts a three-tier architecture (Presentation, Application, and Data layers) to improve security, maintainability, and scalability.

## 2. Installation Steps

### Prerequisites
- Python 3.10+
- pip (Python package manager)
- Git (optional, for repository cloning)

### Steps
Follow these steps to install the project:

#### 1. Clone the repository
```bash
git clone https://github.com/khadijaamirah/B00kWithUs.git
cd B00kWithUs
```
#### 2. Create & activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate #(Windows)
Source venv/bin/activate #(macOS/Linux)
```
#### 3. Install dependencies
```bash
pip install -r requirements.txt
```
#### 4. Configure environment variables
```bash
#Create a .env file based on .env.example
cp .env.example .env
#Fill in your own SECRET_KEY and other config values
```

## 3. Security Features Summary
The system implements the following security features:

- Server-side input validation using Django Forms and regex-based whitelisting
- Protection against SQL Injection using Django ORM (no raw SQL queries)
- Cross-Site Scripting (XSS) prevention via output encoding and input validation
- Secure authentication using Django’s built-in authentication framework
- Multi-factor authentication (OTP) for login verification
- Rate limiting on login attempts to prevent brute-force attacks
- Session-based access control using login_required decorators
- Secure cookie configuration (HttpOnly, SameSite)
- Environment-based configuration for sensitive settings (SECRET_KEY, DEBUG)
- Security headers and Content Security Policy (CSP)
- Audit logging of security-relevant events

## 4. How to Run the Application
After installation:

#### 1. Apply database migrations
```bash
python manage.py migrate
```
#### 2. Create Static files
```bash
mkdir staticfiles
python manage.py collectstatic
```
#### 3. Create an admin user (Optional)
```bash
python manage.py createsuperuser
```
#### 4. Start the server
```bash
python manage.py runserver
```
#### 5. Open browser and go to:
```bash
http://127.0.0.1:8000/ 
```
#### 6. Register a user or log in with an existing account

## 5. Dependencies
This project uses the following dependencies:
- Django – Web framework
- django-ratelimit – Brute-force protection
- django-auditlog – Audit logging of user activities
- django-csp – Content Security Policy enforcement
- djangorestframework – API support
- python-dotenv / django-environ – Environment-based configuration

#### You can install all dependencies with:
```bash
pip install -r requirements.txt
```

## 6. Screenshots of System
Below are screenshots demonstrating key features of the working application:

#### Home Page
<img width="414" height="337" alt="image" src="https://github.com/user-attachments/assets/7d64af37-50d5-4abe-8835-137997efcffe" />

#### Registration Page
<img width="372" height="462" alt="image" src="https://github.com/user-attachments/assets/3f4643bc-1dac-4a0d-9db6-e3a7c9f16893" />

#### Login Page
<img width="352" height="384" alt="image" src="https://github.com/user-attachments/assets/4c7e350c-cd19-4d96-97ee-0a3e9b3cc53d" />

#### Verify OTP
#(OTP will be shown on the terminal)

<img width="490" height="275" alt="image" src="https://github.com/user-attachments/assets/ddad958d-5389-4881-a682-5850612bbe26" />

#### Test Backend API
<img width="355" height="104" alt="image" src="https://github.com/user-attachments/assets/098fcdbd-096e-4548-ac35-a04e86619502" />

#### Booking Page
#(Users can create new booking and view, edit or delete their existing bookings)

<img width="529" height="207" alt="image" src="https://github.com/user-attachments/assets/890d5029-96f9-4176-961c-dd92f74d3387" />

#### Booking Form
<img width="374" height="261" alt="image" src="https://github.com/user-attachments/assets/f6e5cb69-f496-4a6c-a6f0-5d6d7c4a853d" />

#### Admin Panel
#(Admin must log in one more time to verify their identity)

<img width="493" height="379" alt="image" src="https://github.com/user-attachments/assets/a0ddeb61-8169-4ec9-b4ba-8013e5ad8c14" />

#### Administration Site
#(Displays all bookings, existing users & audit logs)

<img width="940" height="272" alt="image" src="https://github.com/user-attachments/assets/617ae255-84f7-4c74-a46a-65e95eac0fd0" />
