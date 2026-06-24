from enum import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    DELIVERY_BOY = "DELIVERY_BOY"
    CUSTOMER = "CUSTOMER"