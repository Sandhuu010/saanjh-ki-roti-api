# SAANJH KI ROTI API

# 1. PROJECT REQUIREMENTS

## 1.1 Objective

Build a FastAPI backend system for managing:

* Customers
* Subscription Plans
* Deliveries
* Billing
* Complaints
* Reports
* Customer Self-Service

The system should reduce manual bookkeeping and automate daily operations.

---

## 1.2 User Roles

### Admin

Permissions:

* Manage customers
* Manage plans
* Manage subscriptions
* Manage payments
* Manage deliveries
* Manage complaints
* Generate reports

### Delivery Boy

Permissions:

* View assigned deliveries
* Update delivery status

### Customer

Permissions:

* View subscription
* Pause plan
* View bills
* View delivery status

---

## 1.3 Functional Requirements

### Customer Management

* Create customer
* Update customer
* Upload identity proof
* Assign route

### Subscription Management

* Create subscription
* Change plan
* Pause plan
* Renew subscription

### Delivery Management

* Create daily deliveries
* Track delivery status
* Retry failed deliveries

### Billing Management

* Generate invoices
* Record payments
* Apply discounts
* Auto-pause unpaid accounts

### Complaint Management

* Register complaint
* Assign severity
* Track SLA
* Record compensation

### Reporting

* Daily dashboard
* Monthly PDF reports

---

# 2. IMPLEMENTATION PLAN

## Phase 1

Project Setup

* FastAPI setup
* PostgreSQL setup
* SQLAlchemy
* Alembic
* JWT Authentication

## Phase 2

Customer Module

* Customer CRUD
* Document Upload

## Phase 3

Plan & Subscription Module

* Plans
* Subscriptions
* Pause Management

## Phase 4

Delivery Module

* Route Assignment
* Delivery Tracking

## Phase 5

Billing Module

* Invoices
* Payments
* Discounts

## Phase 6

Complaint Module

* Complaint Tracking
* Compensation

## Phase 7

Reports Module

* Dashboard
* PDF Reports

---

# 3. PROJECT FOLDER STRUCTURE

app/

├── main.py

├── core/

│ ├── config.py

│ ├── security.py

│ └── database.py

├── models/

├── schemas/

├── services/

├── repositories/

├── api/

├── utils/

├── reports/

├── uploads/

└── tests/

---

# 4. FILE DETAILS

## main.py

Purpose:

Application entry point.

Functions:

create_app() -> FastAPI

Output:

FastAPI instance

---

## core/config.py

Purpose:

Store application settings.

Class:

Settings

Attributes:

DATABASE_URL: str

JWT_SECRET: str

SMTP_EMAIL: str

SMTP_PASSWORD: str

---

## core/database.py

Purpose:

Database connection setup.

Variables:

engine

SessionLocal

Base

Functions:

get_db()

Return:

Generator

---

## core/security.py

Purpose:

Authentication utilities.

Functions:

hash_password(password: str) -> str

verify_password(password: str, hashed: str) -> bool

create_access_token(user_id: int) -> str

decode_token(token: str) -> dict

---

# 5. DATABASE MODELS

## Customer

File:

models/customer.py

Class:

Customer

Fields:

id: int

name: str

phone: str

alternate_phone: str

address: str

route_id: int

diet_type: str

status: str

created_at: datetime

---

## Plan

File:

models/plan.py

Class:

Plan

Fields:

id: int

name: str

price: float

billing_cycle: str

portion_size: str

food_cost_per_day: float

active: bool

---

## Subscription

File:

models/subscription.py

Class:

Subscription

Fields:

id: int

customer_id: int

plan_id: int

start_date: date

end_date: date

paused_days: int

status: str

---

## Delivery

File:

models/delivery.py

Class:

Delivery

Fields:

id: int

customer_id: int

route_id: int

status: str

delivery_date: date

retry_count: int

---

## Payment

File:

models/payment.py

Class:

Payment

Fields:

id: int

customer_id: int

amount: float

payment_mode: str

reference_number: str

paid_at: datetime

---

## Complaint

File:

models/complaint.py

Class:

Complaint

Fields:

id: int

customer_id: int

title: str

description: str

severity: str

status: str

resolution_note: str

---

# 6. SCHEMAS

Purpose:

Request/Response Validation

Example:

schemas/customer.py

Classes:

CustomerCreate

CustomerUpdate

CustomerResponse

Fields:

name: str

phone: str

address: str

route_id: int

diet_type: str

---

# 7. SERVICES

Purpose:

Business Logic

## customer_service.py

Functions:

create_customer(data: CustomerCreate) -> Customer

update_customer(customer_id: int, data: CustomerUpdate) -> Customer

delete_customer(customer_id: int) -> bool

get_customer(customer_id: int) -> Customer

---

## subscription_service.py

Functions:

create_subscription(customer_id: int, plan_id: int) -> Subscription

pause_subscription(subscription_id: int, days: int) -> Subscription

renew_subscription(subscription_id: int) -> Subscription

---

## delivery_service.py

Functions:

generate_daily_deliveries(date: date) -> list[Delivery]

mark_delivered(delivery_id: int) -> Delivery

mark_failed(delivery_id: int, reason: str) -> Delivery

retry_delivery(delivery_id: int) -> Delivery

---

## payment_service.py

Functions:

generate_invoice(customer_id: int) -> Invoice

record_payment(payment_data: dict) -> Payment

apply_discount(invoice_id: int) -> float

---

## complaint_service.py

Functions:

create_complaint(data: ComplaintCreate) -> Complaint

resolve_complaint(id: int, note: str) -> Complaint

calculate_sla(id: int) -> int

---

# 8. API ENDPOINTS

Customer

POST /customers

GET /customers

GET /customers/{id}

PUT /customers/{id}

DELETE /customers/{id}

Subscription

POST /subscriptions

POST /subscriptions/pause

GET /subscriptions/{id}

Delivery

GET /deliveries/today

PATCH /deliveries/{id}/status

Payments

POST /payments

GET /payments/{id}

Complaints

POST /complaints

PATCH /complaints/{id}/resolve

Reports

GET /reports/dashboard

GET /reports/monthly

---

# 9. EDGE CASES

* Duplicate phone number
* Plan changed during active billing cycle
* Delivery boy resignation
* Failed payment
* Multiple active subscriptions
* Pause limit exceeded
* Invalid document upload
* Complaint reopened
* Retry delivery already completed
* Customer deleted with active subscription

---

# 10. SUCCESS CRITERIA

* Daily cooking quantities generated automatically
* Deliveries tracked digitally
* Billing automated
* Complaints tracked with SLA
* Reports generated automatically
* Customers can pause subscriptions online
