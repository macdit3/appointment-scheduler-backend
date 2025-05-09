from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, time, date

# Business model
class Business(BaseModel):
    id: Optional[int] = None
    name: str
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    timezone: str = "UTC"
    cancellation_policy: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Business hours model
class BusinessHours(BaseModel):
    id: Optional[int] = None
    business_id: int
    day_of_week: int  # 0-6 (Monday-Sunday)
    open_time: time
    close_time: time
    is_closed: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Service category model
class ServiceCategory(BaseModel):
    id: Optional[int] = None
    business_id: int
    name: str
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Service model
class Service(BaseModel):
    id: Optional[int] = None
    business_id: int
    category_id: Optional[int] = None
    name: str
    description: Optional[str] = None
    duration: int  # in minutes
    buffer_time: int = 0  # in minutes
    max_clients: int = 1
    price: float
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Staff model
class Staff(BaseModel):
    id: Optional[int] = None
    business_id: int
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    position: Optional[str] = None
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Client model
class Client(BaseModel):
    id: Optional[int] = None
    business_id: int
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    preferred_staff_id: Optional[int] = None
    notes: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Staff services model
class StaffService(BaseModel):
    id: Optional[int] = None
    staff_id: int
    service_id: int
    created_at: Optional[datetime] = None

# Staff schedule model
class StaffSchedule(BaseModel):
    id: Optional[int] = None
    staff_id: int
    day_of_week: int  # 0-6 (Monday-Sunday)
    start_time: time
    end_time: time
    is_working: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Appointment model
class Appointment(BaseModel):
    id: Optional[int] = None
    business_id: int
    client_id: int
    service_id: int
    staff_id: Optional[int] = None
    start_time: datetime
    end_time: datetime
    status: str = "scheduled"  # scheduled, confirmed, completed, cancelled, no-show
    notes: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Appointment reminder model
class AppointmentReminder(BaseModel):
    id: Optional[int] = None
    appointment_id: int
    reminder_type: str  # email, sms
    scheduled_time: datetime
    sent_at: Optional[datetime] = None
    status: str = "pending"  # pending, sent, failed
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Special business hours model
class SpecialBusinessHours(BaseModel):
    id: Optional[int] = None
    business_id: int
    date: date
    is_closed: bool = False
    open_time: Optional[time] = None
    close_time: Optional[time] = None
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Payment model
class Payment(BaseModel):
    id: Optional[int] = None
    appointment_id: int
    amount: float
    payment_method: str
    payment_status: str = "pending"  # pending, completed, failed, refunded, partially_refunded
    transaction_id: Optional[str] = None
    payment_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Client note model
class ClientNote(BaseModel):
    id: Optional[int] = None
    client_id: int
    staff_id: Optional[int] = None
    note_text: str
    created_at: Optional[datetime] = None

# Request and response models for API operations
class BusinessCreate(BaseModel):
    name: str
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    timezone: str = "UTC"
    cancellation_policy: Optional[str] = None

class BusinessUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    timezone: Optional[str] = None
    cancellation_policy: Optional[str] = None

class BusinessHoursCreate(BaseModel):
    business_id: int
    day_of_week: int
    open_time: time
    close_time: time
    is_closed: bool = False

class BusinessHoursUpdate(BaseModel):
    day_of_week: Optional[int] = None
    open_time: Optional[time] = None
    close_time: Optional[time] = None
    is_closed: Optional[bool] = None

class ServiceCategoryCreate(BaseModel):
    business_id: int
    name: str
    description: Optional[str] = None

class ServiceCategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class ServiceCreate(BaseModel):
    business_id: int
    category_id: Optional[int] = None
    name: str
    description: Optional[str] = None
    duration: int
    buffer_time: int = 0
    max_clients: int = 1
    price: float
    is_active: bool = True

class ServiceUpdate(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    duration: Optional[int] = None
    buffer_time: Optional[int] = None
    max_clients: Optional[int] = None
    price: Optional[float] = None
    is_active: Optional[bool] = None

class StaffCreate(BaseModel):
    business_id: int
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    position: Optional[str] = None
    is_active: bool = True

class StaffUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    position: Optional[str] = None
    is_active: Optional[bool] = None

class ClientCreate(BaseModel):
    business_id: int
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    preferred_staff_id: Optional[int] = None
    notes: Optional[str] = None

class ClientUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    preferred_staff_id: Optional[int] = None
    notes: Optional[str] = None

class StaffServiceCreate(BaseModel):
    staff_id: int
    service_id: int

class StaffScheduleCreate(BaseModel):
    staff_id: int
    day_of_week: int
    start_time: time
    end_time: time
    is_working: bool = True

class StaffScheduleUpdate(BaseModel):
    day_of_week: Optional[int] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    is_working: Optional[bool] = None

class AppointmentCreate(BaseModel):
    business_id: int
    client_id: int
    service_id: int
    staff_id: Optional[int] = None
    start_time: datetime
    notes: Optional[str] = None

class AppointmentUpdate(BaseModel):
    client_id: Optional[int] = None
    service_id: Optional[int] = None
    staff_id: Optional[int] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    status: Optional[str] = None
    notes: Optional[str] = None

class AppointmentReminderCreate(BaseModel):
    appointment_id: int
    reminder_type: str
    scheduled_time: datetime

class AppointmentReminderUpdate(BaseModel):
    reminder_type: Optional[str] = None
    scheduled_time: Optional[datetime] = None
    sent_at: Optional[datetime] = None
    status: Optional[str] = None

class SpecialBusinessHoursCreate(BaseModel):
    business_id: int
    date: date
    is_closed: bool = False
    open_time: Optional[time] = None
    close_time: Optional[time] = None
    description: Optional[str] = None

class SpecialBusinessHoursUpdate(BaseModel):
    is_closed: Optional[bool] = None
    open_time: Optional[time] = None
    close_time: Optional[time] = None
    description: Optional[str] = None

class PaymentCreate(BaseModel):
    appointment_id: int
    amount: float
    payment_method: str

class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    payment_method: Optional[str] = None
    payment_status: Optional[str] = None
    transaction_id: Optional[str] = None
    payment_date: Optional[datetime] = None

class ClientNoteCreate(BaseModel):
    client_id: int
    staff_id: Optional[int] = None
    note_text: str