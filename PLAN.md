# Saanjh Ki Roti API

## Project Requirements and Implementation Plan

### Project Overview

Saanjh Ki Roti is a home-cooked tiffin subscription service operating in Vijaynagar, Kota. The business currently manages customer subscriptions, meal preparation, deliveries, billing, complaints, and reporting manually through notebooks and WhatsApp.

The objective of this project is to build a FastAPI-based backend system that digitizes the entire business workflow, reduces food wastage, improves delivery tracking, automates billing, and provides operational visibility through dashboards and reports.

---

# 1. Business Goals

The system must help Saanjh:

1. Know exactly how many tiffins to prepare every day.
2. Track customer subscriptions and pauses.
3. Manage deliveries across routes.
4. Handle billing and payments.
5. Record and resolve customer complaints.
6. Store customer identity documents.
7. Generate monthly business reports.
8. Allow customers to manage pauses themselves.
9. Reduce manual notebook work.

---

# 2. User Roles

## 2.1 Admin (Saanjh)

Full system access.

Permissions:

* Manage customers
* Manage subscriptions
* Manage plans
* Manage deliveries
* Manage complaints
* Manage payments
* Generate reports
* Upload customer documents
* Reassign routes

---

## 2.2 Delivery Boy

Limited access.

Permissions:

* View assigned route only
* View assigned deliveries
* Update delivery status
* Retry failed deliveries
* View own performance

Restrictions:

* Cannot access other routes
* Cannot access customer payments
* Cannot access complaints

---

## 2.3 Customer

Permissions:

* View subscription
* View billing history
* Request plan pause
* View delivery status
* View complaint history

Restrictions:

* Cannot access other customers' data

---

# 3. Functional Requirements

---

## Module 1: Customer Management

### Features

Create Customer

Store:

* Full Name
* Mobile Number
* Alternate Number
* Address
* Route
* Diet Preference
* Aadhaar/License Image
* Referral Code
* Referred By

### Validations

* Mobile number must be unique.
* Duplicate customer creation should be prevented.
* Existing customer may be merged by admin.

### Customer Status

* Active
* Paused
* Auto-Paused
* Cancelled

---

## Module 2: Plan Management

### Supported Plans

#### Monthly Veg

* ₹2800
* Lunch Only

#### Monthly Premium

* ₹3500
* Lunch + Dinner

#### Weekly Saver

* ₹750
* Lunch + Dinner

#### Diabetic Special

* ₹3800
* Lunch + Dinner

### Plan Configuration

Each plan stores:

* Name
* Price
* Billing Cycle
* Portion Size
* Daily Food Cost
* Supported Diet Types
* Active Status

---

## Module 3: Subscription Management

### Features

Customer can subscribe to:

* One active plan at a time

Track:

* Start Date
* End Date
* Renewal Date
* Current Price Snapshot
* Billing Cycle

### Important Rule

If plan pricing changes:

Existing subscriptions continue at old price until next renewal.

Reason:

Prevents billing disputes.

---

## Module 4: Pause Management

### Rules

Customer may pause:

* Maximum 7 days per billing cycle

Unused paused days:

* Carry forward only within limit

Beyond 7 days:

* Expire

### Pause Workflow

Customer requests pause:

Pending → Approved → Active

Store:

* Pause Start Date
* Pause End Date
* Reason
* Approved By

---

## Module 5: Daily Meal Planning

Purpose:

Generate cooking requirements every morning.

Categories:

* Veg
* Non-Veg
* Jain
* Diabetic

System calculates:

Total Active Deliveries
− Paused Customers
− Failed Renewals
− Auto-Paused Accounts

Output:

Daily Preparation Sheet

Example:

Veg: 38
Jain: 10
Diabetic: 8
Non-Veg: 11

Total: 67

---

## Module 6: Add-On Orders

Supported Add-Ons:

* Extra Paneer
* Raita
* Salad
* Friday Kheer

Rules:

* Must be ordered before 9:00 AM.
* Add-on linked to specific delivery date.

Status:

* Pending
* Accepted
* Rejected
* Prepared

---

## Module 7: Route Management

Routes:

### East Vijaynagar

Approx 22 deliveries

### West Vijaynagar

Approx 18 deliveries

### Indra Vihar

Approx 25 deliveries

Each customer belongs to one route.

Each route assigned to one delivery boy.

---

## Module 8: Delivery Management

### Delivery Status Flow

Prepared
↓
Out For Delivery
↓
Delivered

Alternative:

Prepared
↓
Out For Delivery
↓
Failed
↓
Retry Scheduled
↓
Delivered OR Missed

---

### Failed Delivery Reasons

* Customer Not Home
* Wrong Address
* Cancelled Midway
* Other

### Retry Rules

One retry allowed at 8 PM.

Second failure:

Status = Missed

Missed day counts against plan.

---

## Module 9: Billing System

### Billing Schedule

Monthly Plans:

1st of every month

Weekly Plans:

Every Monday

### Invoice Data

* Invoice Number
* Customer
* Plan
* Amount
* Discounts
* Due Date
* Final Amount

Statuses:

* Pending
* Paid
* Overdue

---

## Module 10: Payment Management

Supported Modes

* Cash
* UPI
* Khaata

Store:

* Amount
* Date
* Payment Mode
* Reference Number

### Discounts

#### Early Payment

10% Discount

Condition:

Payment before due date.

---

#### Referral Discount

5% Discount

Condition:

Referred customer completes first paid month.

Applied only once.

---

### Auto Pause Rule

If invoice remains unpaid:

More than 10 days after due date

System automatically pauses subscription.

---

## Module 11: Complaint Management

Complaint Types

* Late Delivery
* Cold Food
* Wrong Order
* Missing Item
* Taste Complaint
* Other

---

### Severity Levels

#### Low

Resolution within 48 hours

#### Medium

Resolution within 24 hours

#### High

Resolution within 6 hours

---

### Complaint Status

Open
↓
In Progress
↓
Resolved
↓
Closed

Store:

* Resolution Notes
* Compensation Given
* Resolution Time

---

## Module 12: Dashboard

Single-screen overview.

Display:

### Today's Numbers

* Total Deliveries
* Delivered
* Pending
* Failed
* Retried

### By Plan

* Monthly Veg
* Premium
* Weekly Saver
* Diabetic

### By Route

* East Vijaynagar
* West Vijaynagar
* Indra Vihar

### Revenue

* Today's Revenue
* Outstanding Amount

---

## Module 13: Document Management

Store:

* Aadhaar Images
* Driving License Images

Linked directly to customer profile.

Requirements:

* Secure storage
* File validation
* Image preview

---

## Module 14: Monthly Reports

Generated automatically.

PDF Report contains:

### Business Summary

* Total Revenue
* Total Deliveries
* Active Customers

### Operations

* Tiffins Served
* Paused Customers
* Failed Deliveries

### Complaints

* Total Complaints
* Resolved Complaints
* Average Resolution Time

### Delivery Performance

* Deliveries Per Route
* Deliveries Per Delivery Boy

Delivered through email.

---

# 4. Non-Functional Requirements

## Security

* JWT Authentication
* Password Hashing
* Role Based Access Control

## Performance

* API Response < 500ms
* Support 500+ customers

## Reliability

* Data Backup
* Audit Logs

## Scalability

* Modular Architecture
* Easy addition of routes and plans

---

# 5. Database Design (High Level)

### Users

* id
* name
* phone
* role

### Customers

* id
* user_id
* address
* route_id
* diet_type

### Plans

* id
* name
* price

### Subscriptions

* id
* customer_id
* plan_id

### Pauses

* id
* subscription_id

### Deliveries

* id
* customer_id
* route_id
* status

### Routes

* id
* name

### DeliveryBoys

* id
* user_id

### Payments

* id
* customer_id
* amount

### Invoices

* id
* customer_id

### Complaints

* id
* customer_id

### AddOns

* id
* name

### Documents

* id
* customer_id
* file_path

### Reports

* id
* month
* file_path

---

# 6. Things That Can Go Wrong

## Customer Related

* Duplicate phone numbers
* Multiple active subscriptions
* Invalid document uploads

## Plan Related

* Plan price changes during billing cycle
* Customer switches plan mid-cycle

## Delivery Related

* Delivery boy resigns
* Route reassignment required
* Delivery marked delivered accidentally

## Billing Related

* Partial payments
* Khaata settlement mismatch
* Failed UPI payment

## Pause Related

* Overlapping pause requests
* Pause exceeding allowed limit

## Complaint Related

* SLA violation
* Complaint reopened after resolution

## Reporting Related

* Missing data in monthly reports
* Report generation failure

---

# 7. Technical Stack

Backend:

* FastAPI

Database:

* PostgreSQL

ORM:

* SQLAlchemy

Authentication:

* JWT

Migrations:

* Alembic

File Storage:

* Local Storage / S3 Compatible Storage

Background Jobs:

* APScheduler / Celery

PDF Reports:

* ReportLab

Email Service:

* SMTP

Testing:

* Pytest

Documentation:

* Swagger/OpenAPI

---

# 8. Development Phases

## Phase 1

Foundation

* Project Setup
* Database Setup
* Authentication
* User Roles

## Phase 2

Customer & Plan Management

* Customers
* Plans
* Subscriptions
* Documents

## Phase 3

Operations

* Pause System
* Add-ons
* Meal Planning
* Routes

## Phase 4

Delivery System

* Deliveries
* Retry Logic
* Route Assignment

## Phase 5

Billing & Payments

* Invoices
* Payments
* Discounts
* Auto Pause

## Phase 6

Complaints

* Complaint Tracking
* SLA Monitoring
* Compensation

## Phase 7

Reports & Dashboard

* Analytics APIs
* Monthly PDF Reports
* Email Reports

## Phase 8

Customer Self-Service

* Pause Requests
* Subscription View
* Billing History

---

# Success Criteria

The project will be considered successful when:

1. Daily cooking quantities are automatically generated.
2. Deliveries can be tracked in real time.
3. Billing and payment reminders are automated.
4. Complaints are monitored with SLAs.
5. Monthly reports are generated automatically.
6. Customers can pause plans without WhatsApp.
7. Manual notebook operations are eliminated.
