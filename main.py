from dns.dnssec import allow_all_policy
from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from typing import List, Optional
from datetime import datetime, date, timedelta
import os
from dotenv import load_dotenv

from db import supabase
from models import (
    # Main models
    Business, BusinessHours, ServiceCategory, Service, Staff, Client,
    StaffService, StaffSchedule, Appointment, AppointmentReminder,
    SpecialBusinessHours, Payment, ClientNote,

    # Create models
    BusinessCreate, BusinessHoursCreate, ServiceCategoryCreate, ServiceCreate,
    StaffCreate, ClientCreate, StaffServiceCreate, StaffScheduleCreate,
    AppointmentCreate, AppointmentReminderCreate, SpecialBusinessHoursCreate,
    PaymentCreate, ClientNoteCreate,

    # Update models
    BusinessUpdate, BusinessHoursUpdate, ServiceCategoryUpdate, ServiceUpdate,
    StaffUpdate, ClientUpdate, StaffScheduleUpdate, AppointmentUpdate,
    AppointmentReminderUpdate, SpecialBusinessHoursUpdate, PaymentUpdate
)

app = FastAPI(title="Appointment Scheduler API")


# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,  # Allow cookies to be included in requests
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Appointment Scheduler API"}


# Business endpoints
@app.get("/businesses/", response_model=List[Business])
def get_businesses():
    response = supabase.table("businesses").select("*").execute()
    return response.data


@app.get("/businesses/{business_id}", response_model=Business)
def get_business(business_id: int):
    response = supabase.table("businesses").select("*").eq("id", business_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Business not found")
    return response.data[0]


@app.post("/businesses/", response_model=Business)
def create_business(business: BusinessCreate):
    response = supabase.table("businesses").insert(business.dict()).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Could not create business")
    return response.data[0]


@app.put("/businesses/{business_id}", response_model=Business)
def update_business(business_id: int, business: BusinessUpdate):
    # Filter out None values
    update_data = {k: v for k, v in business.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    response = supabase.table("businesses").update(update_data).eq("id", business_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Business not found")
    return response.data[0]


# add route
@app.delete("/businesses/{business_id}")
def delete_business(business_id: int):
    response = supabase.table("businesses").delete().eq("id", business_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Business not found")
    return {"message": "Business deleted successfully"}


# Business Hours endpoints
@app.get("/business-hours/", response_model=List[BusinessHours])
def get_all_business_hours(business_id: Optional[int] = None):
    query = supabase.table("business_hours").select("*")
    if business_id:
        query = query.eq("business_id", business_id)
    response = query.execute()
    return response.data


@app.get("/business-hours/{hours_id}", response_model=BusinessHours)
def get_business_hours(hours_id: int):
    response = supabase.table("business_hours").select("*").eq("id", hours_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Business hours not found")
    return response.data[0]


@app.post("/business-hours/", response_model=BusinessHours)
def create_business_hours(hours: BusinessHoursCreate):
    response = supabase.table("business_hours").insert(hours.dict()).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Could not create business hours")
    return response.data[0]


@app.put("/business-hours/{hours_id}", response_model=BusinessHours)
def update_business_hours(hours_id: int, hours: BusinessHoursUpdate):
    update_data = {k: v for k, v in hours.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    response = supabase.table("business_hours").update(update_data).eq("id", hours_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Business hours not found")
    return response.data[0]


@app.delete("/business-hours/{hours_id}")
def delete_business_hours(hours_id: int):
    response = supabase.table("business_hours").delete().eq("id", hours_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Business hours not found")
    return {"message": "Business hours deleted successfully"}


# Service Category endpoints
@app.get("/service-categories/", response_model=List[ServiceCategory])
def get_service_categories(business_id: Optional[int] = None):
    query = supabase.table("service_categories").select("*")
    if business_id:
        query = query.eq("business_id", business_id)
    response = query.execute()
    return response.data


@app.get("/service-categories/{category_id}", response_model=ServiceCategory)
def get_service_category(category_id: int):
    response = supabase.table("service_categories").select("*").eq("id", category_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Service category not found")
    return response.data[0]


@app.post("/service-categories/", response_model=ServiceCategory)
def create_service_category(category: ServiceCategoryCreate):
    response = supabase.table("service_categories").insert(category.dict()).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Could not create service category")
    return response.data[0]


@app.put("/service-categories/{category_id}", response_model=ServiceCategory)
def update_service_category(category_id: int, category: ServiceCategoryUpdate):
    update_data = {k: v for k, v in category.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    response = supabase.table("service_categories").update(update_data).eq("id", category_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Service category not found")
    return response.data[0]


@app.delete("/service-categories/{category_id}")
def delete_service_category(category_id: int):
    response = supabase.table("service_categories").delete().eq("id", category_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Service category not found")
    return {"message": "Service category deleted successfully"}


# Service endpoints
@app.get("/services/", response_model=List[Service])
def get_services(business_id: Optional[int] = None, category_id: Optional[int] = None):
    query = supabase.table("services").select("*")
    if business_id:
        query = query.eq("business_id", business_id)
    if category_id:
        query = query.eq("category_id", category_id)
    response = query.execute()
    return response.data


@app.get("/services/{service_id}", response_model=Service)
def get_service(service_id: int):
    response = supabase.table("services").select("*").eq("id", service_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Service not found")
    return response.data[0]


@app.post("/services/", response_model=Service)
def create_service(service: ServiceCreate):
    response = supabase.table("services").insert(service.dict()).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Could not create service")
    return response.data[0]


@app.put("/services/{service_id}", response_model=Service)
def update_service(service_id: int, service: ServiceUpdate):
    update_data = {k: v for k, v in service.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    response = supabase.table("services").update(update_data).eq("id", service_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Service not found")
    return response.data[0]


@app.delete("/services/{service_id}")
def delete_service(service_id: int):
    response = supabase.table("services").delete().eq("id", service_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"message": "Service deleted successfully"}


# Staff endpoints
@app.get("/staff/", response_model=List[Staff])
def get_staff_members(business_id: Optional[int] = None):
    query = supabase.table("staff").select("*")
    if business_id:
        query = query.eq("business_id", business_id)
    response = query.execute()
    return response.data


@app.get("/staff/{staff_id}", response_model=Staff)
def get_staff_member(staff_id: int):
    response = supabase.table("staff").select("*").eq("id", staff_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return response.data[0]


@app.post("/staff/", response_model=Staff)
def create_staff_member(staff: StaffCreate):
    response = supabase.table("staff").insert(staff.dict()).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Could not create staff member")
    return response.data[0]


@app.put("/staff/{staff_id}", response_model=Staff)
def update_staff_member(staff_id: int, staff: StaffUpdate):
    update_data = {k: v for k, v in staff.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    response = supabase.table("staff").update(update_data).eq("id", staff_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return response.data[0]


@app.delete("/staff/{staff_id}")
def delete_staff_member(staff_id: int):
    response = supabase.table("staff").delete().eq("id", staff_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return {"message": "Staff member deleted successfully"}


# Client endpoints
@app.get("/clients/", response_model=List[Client])
def get_clients(business_id: Optional[int] = None):
    query = supabase.table("clients").select("*")
    if business_id:
        query = query.eq("business_id", business_id)
    response = query.execute()
    return response.data


@app.get("/clients/{client_id}", response_model=Client)
def get_client(client_id: int):
    response = supabase.table("clients").select("*").eq("id", client_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Client not found")
    return response.data[0]


@app.post("/clients/", response_model=Client)
def create_client(client: ClientCreate):
    response = supabase.table("clients").insert(client.dict()).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Could not create client")
    return response.data[0]


@app.put("/clients/{client_id}", response_model=Client)
def update_client(client_id: int, client: ClientUpdate):
    update_data = {k: v for k, v in client.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    response = supabase.table("clients").update(update_data).eq("id", client_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Client not found")
    return response.data[0]


@app.delete("/clients/{client_id}")
def delete_client(client_id: int):
    response = supabase.table("clients").delete().eq("id", client_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"message": "Client deleted successfully"}


# Staff Services endpoints
@app.get("/staff-services/", response_model=List[StaffService])
def get_staff_services(staff_id: Optional[int] = None, service_id: Optional[int] = None):
    query = supabase.table("staff_services").select("*")
    if staff_id:
        query = query.eq("staff_id", staff_id)
    if service_id:
        query = query.eq("service_id", service_id)
    response = query.execute()
    return response.data


@app.post("/staff-services/", response_model=StaffService)
def create_staff_service(staff_service: StaffServiceCreate):
    response = supabase.table("staff_services").insert(staff_service.dict()).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Could not assign service to staff")
    return response.data[0]


@app.delete("/staff-services/")
def delete_staff_service(staff_id: int, service_id: int):
    response = supabase.table("staff_services").delete().eq("staff_id", staff_id).eq("service_id", service_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Staff service assignment not found")
    return {"message": "Service removed from staff successfully"}


# Staff Schedule endpoints
@app.get("/staff-schedules/", response_model=List[StaffSchedule])
def get_staff_schedules(staff_id: Optional[int] = None, day_of_week: Optional[int] = None):
    query = supabase.table("staff_schedules").select("*")
    if staff_id:
        query = query.eq("staff_id", staff_id)
    if day_of_week is not None:
        query = query.eq("day_of_week", day_of_week)
    response = query.execute()
    return response.data


@app.get("/staff-schedules/{schedule_id}", response_model=StaffSchedule)
def get_staff_schedule(schedule_id: int):
    response = supabase.table("staff_schedules").select("*").eq("id", schedule_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Staff schedule not found")
    return response.data[0]


@app.post("/staff-schedules/", response_model=StaffSchedule)
def create_staff_schedule(schedule: StaffScheduleCreate):
    response = supabase.table("staff_schedules").insert(schedule.dict()).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Could not create staff schedule")
    return response.data[0]


@app.put("/staff-schedules/{schedule_id}", response_model=StaffSchedule)
def update_staff_schedule(schedule_id: int, schedule: StaffScheduleUpdate):
    update_data = {k: v for k, v in schedule.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    response = supabase.table("staff_schedules").update(update_data).eq("id", schedule_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Staff schedule not found")
    return response.data[0]


@app.delete("/staff-schedules/{schedule_id}")
def delete_staff_schedule(schedule_id: int):
    response = supabase.table("staff_schedules").delete().eq("id", schedule_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Staff schedule not found")
    return {"message": "Staff schedule deleted successfully"}


# Appointment endpoints
@app.get("/appointments/", response_model=List[Appointment])
def get_appointments(
        business_id: Optional[int] = None,
        client_id: Optional[int] = None,
        staff_id: Optional[int] = None,
        status: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None
):
    query = supabase.table("appointments").select("*")

    if business_id:
        query = query.eq("business_id", business_id)
    if client_id:
        query = query.eq("client_id", client_id)
    if staff_id:
        query = query.eq("staff_id", staff_id)
    if status:
        query = query.eq("status", status)
    if start_date:
        start_datetime = datetime.combine(start_date, datetime.min.time())
        query = query.gte("start_time", start_datetime.isoformat())
    if end_date:
        end_datetime = datetime.combine(end_date, datetime.max.time())
        query = query.lte("start_time", end_datetime.isoformat())

    response = query.order("start_time").execute()
    return response.data


@app.get("/appointments/{appointment_id}", response_model=Appointment)
def get_appointment(appointment_id: int):
    response = supabase.table("appointments").select("*").eq("id", appointment_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return response.data[0]


@app.post("/appointments/", response_model=Appointment)
def create_appointment(appointment: AppointmentCreate):
    # Get service to calculate end_time
    service_response = supabase.table("services").select("*").eq("id", appointment.service_id).execute()
    if not service_response.data:
        raise HTTPException(status_code=404, detail="Service not found")

    service = service_response.data[0]

    # Calculate end_time
    end_time = appointment.start_time + timedelta(minutes=service["duration"])

    # Create appointment data
    appointment_data = appointment.dict()
    appointment_data["end_time"] = end_time
    appointment_data["status"] = "scheduled"

    response = supabase.table("appointments").insert(appointment_data).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Could not create appointment")
    return response.data[0]


@app.put("/appointments/{appointment_id}", response_model=Appointment)
def update_appointment(appointment_id: int, appointment: AppointmentUpdate):
    update_data = {k: v for k, v in appointment.dict().items() if v is not None}

    # If start_time is updated and service_id is provided, recalculate end_time
    if "start_time" in update_data and "service_id" in update_data:
        service_response = supabase.table("services").select("*").eq("id", update_data["service_id"]).execute()
        if service_response.data:
            service = service_response.data[0]
            update_data["end_time"] = update_data["start_time"] + timedelta(minutes=service["duration"])
    # If only start_time is updated, get the current service_id and recalculate end_time
    elif "start_time" in update_data:
        appointment_response = supabase.table("appointments").select("service_id").eq("id", appointment_id).execute()
        if appointment_response.data:
            service_id = appointment_response.data[0]["service_id"]
            service_response = supabase.table("services").select("*").eq("id", service_id).execute()
            if service_response.data:
                service = service_response.data[0]
                update_data["end_time"] = update_data["start_time"] + timedelta(minutes=service["duration"])

    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    response = supabase.table("appointments").update(update_data).eq("id", appointment_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return response.data[0]


@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int):
    response = supabase.table("appointments").delete().eq("id", appointment_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Appointment deleted successfully"}


# Appointment Reminders endpoints
@app.get("/appointment-reminders/", response_model=List[AppointmentReminder])
def get_appointment_reminders(appointment_id: Optional[int] = None, status: Optional[str] = None):
    query = supabase.table("appointment_reminders").select("*")
    if appointment_id:
        query = query.eq("appointment_id", appointment_id)
    if status:
        query = query.eq("status", status)
    response = query.execute()
    return response.data


@app.get("/appointment-reminders/{reminder_id}", response_model=AppointmentReminder)
def get_appointment_reminder(reminder_id: int):
    response = supabase.table("appointment_reminders").select("*").eq("id", reminder_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Appointment reminder not found")
    return response.data[0]


@app.post("/appointment-reminders/", response_model=AppointmentReminder)
def create_appointment_reminder(reminder: AppointmentReminderCreate):
    reminder_data = reminder.dict()
    reminder_data["status"] = "pending"

    response = supabase.table("appointment_reminders").insert(reminder_data).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Could not create appointment reminder")
    return response.data[0]


@app.put("/appointment-reminders/{reminder_id}", response_model=AppointmentReminder)
def update_appointment_reminder(reminder_id: int, reminder: AppointmentReminderUpdate):
    update_data = {k: v for k, v in reminder.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    response = supabase.table("appointment_reminders").update(update_data).eq("id", reminder_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Appointment reminder not found")
    return response.data[0]


@app.delete("/appointment-reminders/{reminder_id}")
def delete_appointment_reminder(reminder_id: int):
    response = supabase.table("appointment_reminders").delete().eq("id", reminder_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Appointment reminder not found")
    return {"message": "Appointment reminder deleted successfully"}


# Special Business Hours endpoints
@app.get("/special-business-hours/", response_model=List[SpecialBusinessHours])
def get_special_business_hours(business_id: Optional[int] = None, date_from: Optional[date] = None,
                               date_to: Optional[date] = None):
    query = supabase.table("special_business_hours").select("*")
    if business_id:
        query = query.eq("business_id", business_id)
    if date_from:
        query = query.gte("date", date_from.isoformat())
    if date_to:
        query = query.lte("date", date_to.isoformat())
    response = query.execute()
    return response.data


@app.get("/special-business-hours/{hours_id}", response_model=SpecialBusinessHours)
def get_special_business_hour(hours_id: int):
    response = supabase.table("special_business_hours").select("*").eq("id", hours_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Special business hours not found")
    return response.data[0]


@app.post("/special-business-hours/", response_model=SpecialBusinessHours)
def create_special_business_hours(hours: SpecialBusinessHoursCreate):
    response = supabase.table("special_business_hours").insert(hours.dict()).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Could not create special business hours")
    return response.data[0]


@app.put("/special-business-hours/{hours_id}", response_model=SpecialBusinessHours)
def update_special_business_hours(hours_id: int, hours: SpecialBusinessHoursUpdate):
    update_data = {k: v for k, v in hours.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    response = supabase.table("special_business_hours").update(update_data).eq("id", hours_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Special business hours not found")
    return response.data[0]


@app.delete("/special-business-hours/{hours_id}")
def delete_special_business_hours(hours_id: int):
    response = supabase.table("special_business_hours").delete().eq("id", hours_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Special business hours not found")
    return {"message": "Special business hours deleted successfully"}


# Payment endpoints
@app.get("/payments/", response_model=List[Payment])
def get_payments(appointment_id: Optional[int] = None, payment_status: Optional[str] = None):
    query = supabase.table("payments").select("*")
    if appointment_id:
        query = query.eq("appointment_id", appointment_id)
    if payment_status:
        query = query.eq("payment_status", payment_status)
    response = query.execute()
    return response.data


@app.get("/payments/{payment_id}", response_model=Payment)
def get_payment(payment_id: int):
    response = supabase.table("payments").select("*").eq("id", payment_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Payment not found")
    return response.data[0]


@app.post("/payments/", response_model=Payment)
def create_payment(payment: PaymentCreate):
    payment_data = payment.dict()
    payment_data["payment_status"] = "pending"
    payment_data["payment_date"] = datetime.now().isoformat()

    response = supabase.table("payments").insert(payment_data).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Could not create payment")
    return response.data[0]


@app.put("/payments/{payment_id}", response_model=Payment)
def update_payment(payment_id: int, payment: PaymentUpdate):
    update_data = {k: v for k, v in payment.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    response = supabase.table("payments").update(update_data).eq("id", payment_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Payment not found")
    return response.data[0]


@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: int):
    response = supabase.table("payments").delete().eq("id", payment_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"message": "Payment deleted successfully"}


# Client Notes endpoints
@app.get("/client-notes/", response_model=List[ClientNote])
def get_client_notes(client_id: Optional[int] = None, staff_id: Optional[int] = None):
    query = supabase.table("client_notes").select("*")
    if client_id:
        query = query.eq("client_id", client_id)
    if staff_id:
        query = query.eq("staff_id", staff_id)
    response = query.execute()
    return response.data

@app.get("/client-notes/{note_id}", response_model=ClientNote)
def get_client_note(note_id: int):
    response = supabase.table("client_notes").select("*").eq("id", note_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Client note not found")
    return response.data[0]

@app.post("/client-notes/", response_model=ClientNote)
def create_client_note(note: ClientNoteCreate):
    response = supabase.table("client_notes").insert(note.dict()).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Could not create client note")
    return response.data[0]

@app.delete("/client-notes/{note_id}")
def delete_client_note(note_id: int):
    response = supabase.table("client_notes").delete().eq("id", note_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Client note not found")
