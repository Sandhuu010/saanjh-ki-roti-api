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

├── services/
│
│   ├── auth_service.py
│
│   └── plan_service.py

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

## Services Layer

Purpose:

Contains business logic.

Responsibilities:

- Validation
- Authorization decisions
- Business rules
- Reusable operations

Routers should only:

- Accept requests
- Call services
- Return responses

Future Examples:

pause_service.py

billing_service.py

delivery_service.py

# 6. DATABASE MODELS

# 6. DATABASE MODELS

## UserRole Enum

Purpose:

Defines allowed user roles in the system.

Allowed Values:

ADMIN

DELIVERY_BOY

CUSTOMER

Validation Rules:

Only enum values may be stored.

Examples Rejected:

admin

Admin

customer

manager

Reason:

Prevents invalid role values from being saved and ensures
authorization checks behave consistently.

---

## User

Purpose:

Authentication and authorization.

Fields:

id: int

username: str

phone: str

password_hash: str

role: UserRole   

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

supports_veg: bool

supports_non_veg: bool

supports_jain: bool

supports_diabetic: bool

includes_lunch: bool

includes_dinner: bool

active: bool

Billing Cycle Values:

WEEKLY

MONTHLY

Purpose:

Defines available subscription plans.

Examples:

Monthly Veg:
supports_veg = true
includes_lunch = true
includes_dinner = false

Monthly Premium:
supports_veg = true
supports_non_veg = true
supports_jain = true
includes_lunch = true
includes_dinner = true

Diabetic Special:
supports_diabetic = true
includes_lunch = true
includes_dinner = true

---

## Money Representation

Decision:

All monetary values are stored as paise integers.

Examples:

₹2800.00

Stored As:

280000

Reason:

- Avoid floating-point precision issues
- No fractional paise exists in Indian currency
- Discount calculations are rounded once
  during invoice generation

Affected Fields:

price_paise

food_cost_per_day_paise

amount_paise

discount_paise

final_amount_paise\

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

## UserResponse

Purpose:

Safe user response returned to clients.

Fields:

id: int

username: str

phone: str

role: str

is_active: bool

created_at: datetime

Excluded Fields:

password_hash

Reason:

Passwords must never be returned in API responses.

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

Checks:

current_user.role == UserRole.ADMIN

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

Success Status:

200 OK

---

## Register User

POST /auth/register

Success Response:

UserResponse

Purpose:

Create user account

Authentication:

Not Required

Success Status:

201 Created

---

## Login

POST /auth/token

Purpose:

Generate JWT

Authentication:

Not Required

Success Status:

200 OK

---

## Get Plans

GET /plans

Purpose:

Retrieve plans

Authentication:

Required

Success Status:

200 OK

---

## Create Plan

POST /plans

Purpose:

Create plan

Authentication:

Required

Authorization:

ADMIN only

Success Status:

201 Created

---

# 11. ERROR HANDLING

## Duplicate Username

Status Code:

409 Conflict

Response:

{
  "detail": "Username already exists"
}

---

## Duplicate Phone Number

Status Code:

409 Conflict

Response:

{
  "detail": "Phone number already exists"
}

---

## Invalid Login

Status Code:

401 Unauthorized

Response:

{
  "detail": "Invalid username or password"
}

---

## Missing Token

Status Code:

401 Unauthorized

Response:

{
  "detail": "Not authenticated"
}

---

## Non-Admin Plan Creation

Status Code:

403 Forbidden

Response:

{
  "detail": "Admin access required"
}

---

## Invalid Plan Data

Status Code:

422 Unprocessable Entity

Response:

{
  "detail": "Validation Error"
}

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

16. UserResponse never exposes password_hash.

17. User.role validation accepts only UserRole enum values.

18. All API success responses return documented HTTP status codes.


---

## Required Automated Tests

test_register_user_success

Purpose:
Verify customer registration succeeds.

Expected:
201 Created

---

test_register_duplicate_username

Purpose:
Verify duplicate username is rejected.

Expected:
409 Conflict

---

test_register_duplicate_phone

Purpose:
Verify duplicate phone number is rejected.

Expected:
409 Conflict

---

test_login_success

Purpose:
Verify valid credentials return JWT token.

Expected:
200 OK

---

test_login_invalid_credentials

Purpose:
Verify invalid credentials are rejected.

Expected:
401 Unauthorized

---

test_get_plans_authenticated

Purpose:
Verify authenticated users can view plans.

Expected:
200 OK

---

test_get_plans_unauthenticated

Purpose:
Verify token is required.

Expected:
401 Unauthorized

---

test_create_plan_admin

Purpose:
Verify admin can create plans.

Expected:
201 Created

---

test_create_plan_customer_forbidden

Purpose:
Verify customer cannot create plans.

Expected:
403 Forbidden