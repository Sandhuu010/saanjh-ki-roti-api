# SAANJH KI ROTI API

# 1. PROJECT REQUIREMENTS

## 1.1 Project Objective

Saanjh Ki Roti is a home-cooked tiffin subscription service operating in Vijaynagar, Kota.

The objective of this project is to build a FastAPI-based backend system that digitizes:

* Customer Management

* Subscription Management (with Pause Management)

* Daily Meal Planning (Lunch + Dinner)

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
* Approve pauses (with 7-day cap enforcement)
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

### Pause Management: 
Customers can request pauses, capped at 7 days per billing cycle. Admin approves/rejects. Auto-pause if dues >10 days late.

### Customer Management:
 CRUD, document upload, route assignment, referral tracking

### Plan Management: 
Monthly Veg, Monthly Premium, Weekly Saver, Diabetic Special

### Subscription Management:
 Create, renew, change, pause, auto-pause overdue

### Add-On Orders:
 Paneer, Raita, Salad, Friday Kheer (cutoff 9 AM)

### Daily Meal Planning:
 Separate counts for Lunch and Dinner by diet type

### Delivery Management:
 Status tracking, retry handling, meal type separation

### Billing Management:
 Invoices, payments, discounts, khaata, reminders 5 days before due date

### Complaint Management: 
SLA monitoring, overdue detection, compensation tracking

### Reporting:
 Dashboard, monthly PDF reports, email delivery

---

# 2. IMPLEMENTATION PLAN

## Technology Stack

### Backend

FastAPI

### Database

SQLite

### Database Access Layer

SQLModel

* Reason:

- Recommended by the project brief
- Combines database models and API schemas in typed classes
- Reduces duplication between models and request/response schemas
- Provides validation and database mapping together
- Keeps the project aligned with the FastAPI learning stack

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
* SQLModel setup
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
* Daily Meal Count Generation (Lunch/Dinner)

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
│   ├── meal_planner.py
│   ├── deliveries.py
│   ├── payments.py
│   ├── complaints.py
│   └── reports.py
├── routers/
│   ├── customers_router.py
│   ├── plans_router.py
│   ├── subscriptions_router.py
│   ├── pauses_router.py
│   ├── addon_orders_router.py
│   ├── meal_planner_router.py
│   ├── deliveries_router.py
│   ├── payments_router.py
│   ├── complaints_router.py
│   └── reports_router.py
├── models/
│   ├── user.py
│   ├── customer.py
│   ├── delivery_boy.py
│   ├── plan.py
│   ├── subscription.py
│   ├── pause.py
│   ├── addon_order.py
│   ├── route.py
│   ├── delivery.py
│   ├── payment.py
│   ├── invoice.py
│   ├── complaint.py
│   └── notification.py
├── services/
│   ├── meal_planner_service.py
│   ├── subscription_service.py
│   ├── billing_service.py
│   └── complaint_service.py
├── uploads/
├── reports/
└── tests/


---

# 4. FILE RESPONSIBILITIES

## main.py

Application entry point

Initializes FastAPI app

Registers routers from routers/

Configures middleware and exception handlers

## core/config.py

Centralized configuration

Settings class with JWT secret, DB path, SMTP credentials

## core/database.py

SQLModel session handling

Functions: get_session(), close_session()

## core/security.py

Password hashing and verification

JWT creation and decoding

Role-based access utilities

## core/constants.py

System constants: SLA hours, addon cutoff, pause cap

## api/ (Business Logic Endpoints)

* customers.py: CRUD for customers, document upload, route assignment

* plans.py: Manage plans (create, update, list)

* subscriptions.py: Create, renew, change subscriptions

* pauses.py: Pause requests, approvals, history retrieval
             Responsibility: mention enforcement of 7‑day cap.

* addon_orders.py: Place add-on orders, enforce cutoff

* meal_planner.py:Generate daily meal counts grouped by diet type and meal type (Lunch/Dinner).

* deliveries.py: Update delivery status, retry failed deliveries

* payments.py: Record payments, apply discounts, manage khaata

* complaints.py: Log complaints, SLA monitoring, overdue detection

* reports.py: Dashboard summaries, monthly PDF reports

## routers/ (FastAPI Routers)

Each file registers endpoints from api/ into FastAPI app

Example: customers_router.py imports api/customers.py and registers routes under /customers

## models/ (SQLModel Classes)

* user.py: User authentication and roles

* customer.py: Customer details, linked to User

* delivery_boy.py: Delivery boy info, linked to User

* plan.py: Plan definitions with pricing and billing cycle

* subscription.py: Subscription details, snapshot pricing, auto-pause flag

* pause.py: Pause history, linked to subscription

* addon_order.py: Add-on orders with cutoff enforcement

* route.py: Delivery routes and status

* delivery.py: Delivery records with meal type (Lunch/Dinner)

* payment.py: Payment records with mode and reference

* invoice.py: Invoice details with due date and status

* complaint.py: Complaint records with SLA and resolution

* notification.py: Payment reminders and other notifications

## services/ (Business Rules)

* meal_planner_service.py: Generate meal counts by diet type and meal type

* subscription_service.py: Enforce 7-day pause cap, auto-pause overdue subscriptions

* billing_service.py: Invoice generation, payment reminders 5 days before due date

* complaint_service.py: SLA monitoring, overdue detection, compensation tracking

## uploads/

Stores customer documents (Aadhaar, license)

## reports/

Stores generated PDF reports

## tests/

Unit and integration tests for all modules

# 5. DATABASE MODELS

## User

File: models/user.py

Purpose: Authentication and authorization.

All system users (Admin, Delivery Boy, Customer) have a corresponding User record.

Fields: id: int

username: str

phone: str

password_hash: str

role: str

is_active: bool

created_at: datetime

Possible Roles:

ADMIN

DELIVERY_BOY

CUSTOMER

Notes:

- JWT tokens reference User.id
- Password hashes are stored in password_hash
- Authentication is performed against User records


## Customer

File:

models/customer.py

Fields:

id: int

user_id : int

name: str

phone: str

alternate_phone: str

address: str

route_id: int

diet_type: DietType

status: str

document_path: str

referred_by_customer_id: int | None

created_at: datetime

* Relationship : Customer.user_id -> User.id

* Purpose : stores customer-specific business information
            Authentication information is stored in user.

---

## DeliveryBoy

File:

models/delivery_boy.py

Fields:

id: int

user_id: int

assigned_route_id: int

status: str

created_at: datetime

* Relationship:

DeliveryBoy.user_id → User.id

* Purpose:

Stores delivery-specific information.

Authentication information is stored in User.


## Plan

Fields:

id: int

name: str

price_paise: int

billing_cycle: BillingCycle

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

auto_paused_due_to_dues: bool.

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

addon_type: AddonType

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

meal_type: str (enum: LUNCH, DINNER)

status: DeliveryStatus

failure_reason: str

retry_count: int

created_at: datetime

---

## Payment

Fields:

id: int

customer_id: int

amount_paise: int

payment_mode: PaymentMode

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

severity: ComplaintSeverity

sla_hours: int

due_at: datetime

resolved_at: datetime

status: ComplaintStatus

resolution_note: str

## Notification : 
id , customer_id, type , message, scheduled_at, status

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

## “Pause requests exceeding 7 days per billing cycle are rejected.”

## “Subscriptions auto‑paused if dues >10 days overdue.”

## “Payment reminders generated 5 days before due date, persisted in Notification table.”

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

POST /subscriptions/pause (enforces 7-day cap)

GET /subscriptions/{id}

GET /subscriptions/{id}/pauses (pause history)

POST /addon-orders

GET /addon-orders/{customer_id}

PATCH /deliveries/{id}/status

POST /payments

POST /payments/reminders/run → generates reminders 5 days before due date.

POST /complaints

GET /complaints/{id}

GET /dashboard

GET /reports/monthly

GET /meal-plan/today (Lunch + Dinner counts)

---

# 9. DEFINITION OF DONE (V1)

1. GET /plans returns active plans.

2. POST /customers creates customer and rejects duplicate phones.

3. POST /subscriptions stores price_snapshot_paise.

4. POST /subscriptions/pause creates pause record and enforces 7‑day cap.

5. GET pause history returns pause dates.

6. POST /addon-orders rejects requests after 09:00 AM.

7. GET /meal-plan/today returns exact cooking quantities grouped by diet type and meal type.

8. Delivery status can be updated.

9. Failed delivery can be retried once.

10. Payment endpoint supports Cash, UPI and Khaata.

11. Complaint endpoint calculates SLA and due_at.

12. Complaint API returns overdue status.

13. Dashboard API returns totals by route, plan and delivery status.

14. Monthly report API generates summary report.

15. All endpoints return valid JSON and HTTP status codes.

16. Subscriptions auto‑paused if dues >10 days late.

17. Payment reminders generated 5 days before due date.

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
