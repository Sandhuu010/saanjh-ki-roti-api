# SAANJH KI ROTI API

# 1. PROJECT REQUIREMENTS

## 1.1 Project Objective

Saanjh Ki Roti is a home-cooked tiffin subscription service operating in Vijaynagar, Kota.

The objective of this project is to build a FastAPI-based backend system that digitizes:

* Customer Management
* Subscription Management
* Daily Meal Planning
* Add-On Orders
* Delivery Tracking
* Billing & Payments
* Complaint Management
* Monthly Reporting
* Customer Self-Service

The system should reduce manual notebook work, minimize food wastage, automate billing, and provide operational visibility.

---

## 1.2 User Roles

### Admin (Saanjh)

Permissions:

* Manage customers
* Manage plans
* Manage subscriptions
* Approve pauses
* Manage deliveries
* Manage complaints
* Manage payments
* Generate reports
* Upload customer documents
* Reassign routes

---

### Delivery Boy

Permissions:

* View assigned route
* View assigned deliveries
* Update delivery status
* Retry failed delivery

Restrictions:

* Cannot access payments
* Cannot access complaints
* Cannot view other routes

---

### Customer

Permissions:

* View subscription
* View invoices
* View delivery status
* Request pause
* Place add-on orders
* View complaint history

---

## 1.3 Functional Requirements

### Customer Management

* Create customer
* Update customer
* Upload Aadhaar/License
* Assign route
* Maintain referral information

### Plan Management

Supported Plans:

1. Monthly Veg
2. Monthly Premium
3. Weekly Saver
4. Diabetic Special

### Subscription Management

* Create subscription
* Renew subscription
* Change plan
* Pause subscription

### Add-On Order Management

Supported Add-ons:

* Extra Paneer
* Raita
* Salad
* Friday Kheer

Rules:

* Orders accepted before 09:00 AM
* Orders after cutoff rejected automatically

### Daily Meal Planning

Generate daily cooking counts:

* Veg
* Non-Veg
* Jain
* Diabetic

### Delivery Management

Statuses:

* Prepared
* Out For Delivery
* Delivered
* Failed
* Retry Scheduled
* Missed

### Billing Management

* Generate invoices
* Record payments
* Apply discounts
* Manage khaata

### Complaint Management

Complaint Types:

* Late Delivery
* Cold Food
* Wrong Order
* Missing Item
* Taste Complaint
* Other

### Reporting

Generate:

* Dashboard Summary
* Monthly PDF Reports

---

# 2. IMPLEMENTATION PLAN

## Technology Stack

### Backend

FastAPI

### Database

SQLite

### Database Access

sqlite3

### Authentication

JWT

### File Storage

Local File System

### PDF Generation

ReportLab

### Email Service

SMTP

---

## Phase 1 – Foundation

Deliverables:

* FastAPI Setup
* SQLite Setup
* Authentication
* Health Endpoint
* Plan Endpoints

Demo APIs:

GET /health

GET /plans

POST /plans

---

## Phase 2 – Customer Module

* Customer CRUD
* Document Upload
* Route Assignment

---

## Phase 3 – Plan & Subscription Module

* Plan Management
* Subscription Management
* Pause Management

---

## Phase 4 – Add-On & Meal Planning

* Add-On Orders
* Daily Meal Count Generation

---

## Phase 5 – Delivery Module

* Delivery Tracking
* Retry Handling
* Route Assignment

---

## Phase 6 – Billing Module

* Invoice Generation
* Payments
* Discounts
* Khaata

---

## Phase 7 – Complaint Module

* Complaint Tracking
* SLA Monitoring
* Compensation Tracking

---

## Phase 8 – Reports & Dashboard

* Dashboard APIs
* PDF Reports
* Email Reports

---

# 3. PROJECT STRUCTURE

app/

├── main.py

├── core/

│   ├── config.py

│   ├── database.py

│   ├── security.py

│   └── constants.py

├── api/

│   ├── customers.py

│   ├── plans.py

│   ├── subscriptions.py

│   ├── pauses.py

│   ├── addon_orders.py

│   ├── deliveries.py

│   ├── payments.py

│   ├── complaints.py

│   └── reports.py

├── models/

├── schemas/

├── services/

├── uploads/

├── reports/

└── tests/

---

# 4. FILE RESPONSIBILITIES

## main.py

Purpose:

Application entry point.

Functions:

create_app() -> FastAPI

---

## core/config.py

Purpose:

Application configuration.

Class:

Settings

Fields:

JWT_SECRET: str

DATABASE_PATH: str

SMTP_EMAIL: str

SMTP_PASSWORD: str

---

## core/database.py

Purpose:

Database connection handling.

Functions:

get_connection() -> sqlite3.Connection

close_connection() -> None

---

## core/security.py

Purpose:

Authentication utilities.

Functions:

hash_password(password: str) -> str

verify_password(password: str, hash: str) -> bool

create_token(user_id: int) -> str

decode_token(token: str) -> dict

---

## core/constants.py

Purpose:

System constants.

Variables:

LOW_SLA_HOURS = 48

MEDIUM_SLA_HOURS = 24

HIGH_SLA_HOURS = 6

ADDON_CUTOFF_HOUR = 9

---

# 5. DATABASE MODELS

## Customer

File:

models/customer.py

Fields:

id: int

name: str

phone: str

alternate_phone: str

address: str

route_id: int

diet_type: str

status: str

document_path: str

referred_by_customer_id: int | None

created_at: datetime

---

## Plan

Fields:

id: int

name: str

price_paise: int

billing_cycle: str

portion_size: str

food_cost_per_day_paise: int

active: bool

---

## Subscription

Fields:

id: int

customer_id: int

plan_id: int

price_snapshot_paise: int

start_date: date

end_date: date

status: str

created_at: datetime

---

## Pause

Fields:

id: int

subscription_id: int

start_date: date

end_date: date

reason: str

approved_by: int

created_at: datetime

Purpose:

Stores complete pause history.

---

## AddonOrder

Fields:

id: int

customer_id: int

delivery_date: date

addon_type: str

quantity: int

price_paise: int

status: str

created_at: datetime

---

## Route

Fields:

id: int

name: str

delivery_boy_id: int

status: str

Possible Values:

ACTIVE

PENDING_REASSIGNMENT

INACTIVE

---

## Delivery

Fields:

id: int

customer_id: int

route_id: int

delivery_date: date

status: str

failure_reason: str

retry_count: int

created_at: datetime

---

## Payment

Fields:

id: int

customer_id: int

amount_paise: int

payment_mode: str

reference_number: str

paid_at: datetime

---

## Invoice

Fields:

id: int

customer_id: int

amount_paise: int

discount_paise: int

final_amount_paise: int

due_date: date

status: str

---

## Complaint

Fields:

id: int

customer_id: int

title: str

description: str

severity: str

sla_hours: int

due_at: datetime

resolved_at: datetime

status: str

resolution_note: str

---

# 6. ENGINEERING DECISIONS

## Duplicate Phone Number

Decision:

Reject duplicate customer creation.

Reason:

Phone number uniquely identifies a customer.

Admin may manually merge records.

---

## Plan Price Changes

Decision:

Snapshot pricing.

Existing subscribers keep old price until renewal.

New subscribers receive updated price.

---

## Delivery Boy Resignation

Decision:

Route status becomes PENDING_REASSIGNMENT.

Admin reassigns route.

Deliveries remain visible to admin during transition.

---

# 7. COMPLAINT SLA RULES

LOW = 48 hours

MEDIUM = 24 hours

HIGH = 6 hours

Overdue Condition:

current_time > due_at

AND

status != RESOLVED

API Response includes:

is_overdue: bool

---

# 8. API ENDPOINTS

GET /health

POST /customers

GET /customers

GET /customers/{id}

PUT /customers/{id}

POST /subscriptions

POST /subscriptions/pause

GET /subscriptions/{id}

POST /addon-orders

GET /addon-orders/{customer_id}

PATCH /deliveries/{id}/status

POST /payments

POST /complaints

GET /complaints/{id}

GET /dashboard

GET /reports/monthly

---

# 9. DEFINITION OF DONE (V1)

1. GET /plans returns active plans.

2. POST /customers creates customer and rejects duplicate phones.

3. POST /subscriptions stores price_snapshot_paise.

4. POST /subscriptions/pause creates pause record.

5. GET pause history returns pause dates.

6. POST /addon-orders rejects requests after 09:00 AM.

7. Daily meal planner returns counts by diet type.

8. Delivery status can be updated.

9. Failed delivery can be retried once.

10. Payment endpoint supports Cash, UPI and Khaata.

11. Complaint endpoint calculates SLA and due_at.

12. Complaint API returns overdue status.

13. Dashboard API returns totals by route, plan and delivery status.

14. Monthly report API generates summary report.

15. All endpoints return valid JSON and HTTP status codes.

---

# 10. SUCCESS CRITERIA

* Daily cooking quantities generated automatically.
* Food wastage reduced by accurate meal planning.
* Delivery tracking available digitally.
* Billing automated.
* Complaints tracked with SLA monitoring.
* Monthly reports generated automatically.
* Customers can pause subscriptions online.
* Manual notebook tracking significantly reduced.
