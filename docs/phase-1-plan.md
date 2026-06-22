# SAANJH KI ROTI API

# PHASE 1 IMPLEMENTATION PLAN

Version: 1.0

Purpose:
This document defines the detailed implementation plan for Phase 1 of the
Saanjh Ki Roti API project.

Phase 1 focuses on:

1. Project Foundation Setup
2. Database Configuration
3. Authentication System
4. User Management Foundation
5. Plan Management Foundation
6. Health Monitoring Endpoint

No customer, subscription, delivery, billing, complaint or reporting
business logic will be implemented in this phase.

These modules are planned for later phases.

---

# 1. PHASE 1 OBJECTIVES

The objective of Phase 1 is to create a secure and runnable FastAPI
application that provides:

- Project structure
- Database connection
- Authentication infrastructure
- User model
- Plan model
- Login functionality
- User registration functionality
- Protected route support
- Admin authorization support
- Health endpoint
- Plan endpoints

At the end of Phase 1 the system should allow:

1. User Registration
2. User Login
3. JWT Token Generation
4. JWT Token Validation
5. Admin-only Plan Creation
6. Plan Retrieval

---

# 2. TECHNOLOGY STACK

## Backend Framework

FastAPI

Reason:

- Recommended by project brief
- Built-in OpenAPI documentation
- Dependency Injection support
- Strong typing

---

## Database

SQLite

Reason:

- Lightweight
- No separate server required
- Suitable for internship project

---

## ORM

SQLModel

Reason:

- Recommended by FastAPI ecosystem
- Combines SQLAlchemy and Pydantic
- Supports typed database models
- Reduces duplication

---

## Authentication

OAuth2 Password Flow + JWT

Reason:

- Recommended in FastAPI tutorial
- Swagger Authorize button support
- Secure stateless authentication

---

## Password Hashing

Passlib + Bcrypt

Reason:

- Secure password storage
- Plain passwords never stored

---

# 3. PROJECT STRUCTURE

app/

├── main.py

├── core/

│   ├── config.py

│   ├── database.py

│   └── security.py

├── models/

│   ├── __init__.py

│   ├── user.py

│   └── plan.py

├── routers/

│   ├── auth.py

│   ├── plans.py

│   └── health.py

├── schemas/

│   ├── auth.py

│   └── plan.py

├── dependencies/

│   └── auth.py

└── scripts/

    └── create_admin.py

tests/

requirements.txt

.env.example

.gitignore

README.md

---

# 4. BUILD PROCESS

Step 1

Create repository

saanjh-ki-roti-api

---

Step 2

Create virtual environment

python -m venv venv

---

Step 3

Activate virtual environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

---

Step 4

Install dependencies

pip install -r requirements.txt

---

Step 5

Create .env file

Copy values from .env.example

---

Step 6

Run application

uvicorn app.main:app --reload

---

Step 7

Create admin account

python app/scripts/create_admin.py

---

Step 8

Verify API

Open:

http://127.0.0.1:8000/docs

---

# 5. FILE RESPONSIBILITIES

## main.py

Purpose:

Application entry point.

Responsibilities:

- Create FastAPI application
- Register routers
- Create database tables on startup

Functions:

create_app() -> FastAPI

Output:

FastAPI application instance

---

## core/config.py

Purpose:

Load environment variables.

Class:

Settings

Fields:

DATABASE_URL: str

JWT_SECRET_KEY: str

JWT_ALGORITHM: str

ACCESS_TOKEN_EXPIRE_MINUTES: int

Output:

Global settings object

---

## core/database.py

Purpose:

Database setup.

Functions:

create_db_and_tables() -> None

Creates all SQLModel tables.

---

get_session()

Output:

Session

Used by dependency injection.

---

## core/security.py

Purpose:

Authentication utilities.

Functions:

hash_password(
    password: str
) -> str

Input:

Plain password

Output:

Hashed password

---

verify_password(
    password: str,
    hashed_password: str
) -> bool

Output:

True or False

---

create_access_token(
    user_id: int,
    role: str
) -> str

Output:

JWT token

---

decode_access_token(
    token: str
) -> dict

Output:

JWT payload

Example:

{
  "user_id": 1,
  "role": "ADMIN"
}

---

## create_admin.py

Purpose:

Create first admin account.

Rules:

1. Runs only when executed directly.
2. Reads ADMIN_USERNAME from environment.
3. Reads ADMIN_PASSWORD from environment.
4. If admin already exists, exits gracefully.
5. Safe to run multiple times.

---


# 6. DATABASE MODELS

## User

Purpose:

Authentication and authorization.

Fields:

id: int

username: str

phone: str

password_hash: str

role: str

is_active: bool

created_at: datetime

Allowed Roles:

ADMIN

DELIVERY_BOY

CUSTOMER

Relationships:

Future customer and delivery modules
will reference User.id.

---

## Plan

Purpose:

Store available tiffin plans.

Fields:

id: int

name: str

price_paise: int

billing_cycle: str

portion_size: str

food_cost_per_day_paise: int

active: bool

Billing Cycle Values:

WEEKLY

MONTHLY

---

# 7. REQUEST/RESPONSE SCHEMAS

## RegisterRequest

Fields:

username: str

phone: str

password: str

Output:

Created User

---

## LoginRequest

OAuth2PasswordRequestForm

Fields:

username

password

Output:

JWT Token

---

## TokenResponse

Fields:

access_token: str

token_type: str

---

## PlanCreate

Fields:

name: str

price_paise: int

billing_cycle: str

portion_size: str

food_cost_per_day_paise: int

active: bool

---

# 8. AUTHENTICATION FLOW

Step 1

User registers

POST /auth/register

---

Step 2

User logs in

POST /auth/token

---

Step 3

JWT token generated

---

Step 4

User clicks Authorize in Swagger

---

Step 5

Token sent in Authorization header

Bearer <token>

---

Step 6

Protected routes validate token

---

# 9. AUTHORIZATION FLOW

Dependency:

get_current_user()

Purpose:

Protected Route Pattern

Example:

GET /plans

Depends(get_current_user)

POST /plans

Depends(get_current_admin)

Validate JWT

Return authenticated user

---

Dependency:

get_current_admin()

Purpose:

Ensure role == ADMIN

Return admin user

Otherwise:

403 Forbidden

---

OAuth2PasswordBearer

tokenUrl="/auth/token"

# 10. API ENDPOINTS

## Health

GET /health

Purpose:

Application health check

Response:

{
  "status": "ok"
}

---

## Register User

POST /auth/register

Purpose:

Create user account

Authentication:

Not Required

---

## Login

POST /auth/token

Purpose:

Generate JWT

Authentication:

Not Required

---

## Get Plans

GET /plans

Purpose:

Retrieve plans

Authentication:

Required

---

## Create Plan

POST /plans

Purpose:

Create plan

Authentication:

Required

Authorization:

ADMIN only

---

# 11. ERROR HANDLING

400

Validation error

---

401

Authentication failed

---

403

Authorization failed

---

404

Resource not found

---

500

Server error

---

# 12. SECURITY RULES

Passwords stored only as hashes.

JWT secret loaded from environment.

No credentials committed to Git.

Database files excluded from Git.

.env excluded from Git.

Admin password loaded from environment.

---

# 13. DEFINITION OF DONE

Phase 1 is complete when:

1. Application starts successfully.

2. Database tables are created automatically.

3. User registration works.

4. User login works.

5. JWT token is generated.

6. Swagger Authorize button works.

7. Protected routes require authentication.

8. Admin-only routes reject non-admin users.

9. GET /health returns status.

10. GET /plans returns plan list.

11. POST /plans creates plan.

12. .env is not committed.

13. Database file is not committed.

14. API documentation available at /docs.

15. All endpoints return valid HTTP status codes.