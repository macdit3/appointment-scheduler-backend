import os
from dotenv import load_dotenv
from supabase import create_client, Client
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)

# Business functions
def get_business(business_id):
    """Get a business by ID"""
    response = supabase.table("businesses").select("*").eq("id", business_id).execute()
    return response.data[0] if response.data else None

def update_business(business_id, business_data):
    """Update a business by ID"""
    response = supabase.table("businesses").update(business_data).eq("id", business_id).execute()
    return response.data[0] if response.data else None

# Business hours functions
def get_business_hours(business_id):
    """Get all business hours for a business"""
    response = supabase.table("business_hours").select("*").eq("business_id", business_id).execute()
    return response.data

def get_business_hours_by_day(business_id, day_of_week):
    """Get business hours for a specific day"""
    response = supabase.table("business_hours").select("*").eq("business_id", business_id).eq("day_of_week", day_of_week).execute()
    return response.data[0] if response.data else None

def create_business_hours(business_id, day_of_week, open_time, close_time, is_closed=False):
    """Create business hours for a specific day"""
    business_hours_data = {
        "business_id": business_id,
        "day_of_week": day_of_week,
        "open_time": open_time,
        "close_time": close_time,
        "is_closed": is_closed
    }
    response = supabase.table("business_hours").insert(business_hours_data).execute()
    return response.data[0] if response.data else None

def update_business_hours(business_hours_id, business_hours_data):
    """Update business hours by ID"""
    response = supabase.table("business_hours").update(business_hours_data).eq("id", business_hours_id).execute()
    return response.data[0] if response.data else None

# Special business hours functions
def get_special_business_hours(business_id):
    """Get all special business hours for a business"""
    response = supabase.table("special_business_hours").select("*").eq("business_id", business_id).execute()
    return response.data

def get_special_business_hours_by_date(business_id, date):
    """Get special business hours for a specific date"""
    response = supabase.table("special_business_hours").select("*").eq("business_id", business_id).eq("date", date).execute()
    return response.data[0] if response.data else None

def create_special_business_hours(business_id, date, is_closed=False, open_time=None, close_time=None, description=None):
    """Create special business hours for a specific date"""
    special_hours_data = {
        "business_id": business_id,
        "date": date,
        "is_closed": is_closed,
        "open_time": open_time,
        "close_time": close_time,
        "description": description
    }
    response = supabase.table("special_business_hours").insert(special_hours_data).execute()
    return response.data[0] if response.data else None

def update_special_business_hours(special_hours_id, special_hours_data):
    """Update special business hours by ID"""
    response = supabase.table("special_business_hours").update(special_hours_data).eq("id", special_hours_id).execute()
    return response.data[0] if response.data else None

# Service category functions
def get_service_categories(business_id):
    """Get all service categories for a business"""
    response = supabase.table("service_categories").select("*").eq("business_id", business_id).execute()
    return response.data

def get_service_category(category_id):
    """Get a service category by ID"""
    response = supabase.table("service_categories").select("*").eq("id", category_id).execute()
    return response.data[0] if response.data else None

def create_service_category(business_id, name, description=None):
    """Create a new service category"""
    category_data = {
        "business_id": business_id,
        "name": name,
        "description": description
    }
    response = supabase.table("service_categories").insert(category_data).execute()
    return response.data[0] if response.data else None

def update_service_category(category_id, category_data):
    """Update a service category by ID"""
    response = supabase.table("service_categories").update(category_data).eq("id", category_id).execute()
    return response.data[0] if response.data else None

# Service functions
def get_services(business_id):
    """Get all services for a business"""
    response = supabase.table("services").select("*").eq("business_id", business_id).execute()
    return response.data

def get_services_by_category(category_id):
    """Get all services for a specific category"""
    response = supabase.table("services").select("*").eq("category_id", category_id).execute()
    return response.data

def get_service(service_id):
    """Get a service by ID"""
    response = supabase.table("services").select("*").eq("id", service_id).execute()
    return response.data[0] if response.data else None

def create_service(business_id, name, duration, price, category_id=None, description=None, buffer_time=0, max_clients=1, is_active=True):
    """Create a new service"""
    service_data = {
        "business_id": business_id,
        "category_id": category_id,
        "name": name,
        "description": description,
        "duration": duration,
        "buffer_time": buffer_time,
        "max_clients": max_clients,
        "price": price,
        "is_active": is_active
    }
    response = supabase.table("services").insert(service_data).execute()
    return response.data[0] if response.data else None

def update_service(service_id, service_data):
    """Update a service by ID"""
    response = supabase.table("services").update(service_data).eq("id", service_id).execute()
    return response.data[0] if response.data else None

# Staff functions
def get_staff(business_id):
    """Get all staff for a business"""
    response = supabase.table("staff").select("*").eq("business_id", business_id).execute()
    return response.data

def get_staff_member(staff_id):
    """Get a staff member by ID"""
    response = supabase.table("staff").select("*").eq("id", staff_id).execute()
    return response.data[0] if response.data else None

def create_staff_member(business_id, first_name, last_name, email=None, phone=None, position=None, is_active=True):
    """Create a new staff member"""
    staff_data = {
        "business_id": business_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "position": position,
        "is_active": is_active
    }
    response = supabase.table("staff").insert(staff_data).execute()
    return response.data[0] if response.data else None

def update_staff_member(staff_id, staff_data):
    """Update a staff member by ID"""
    response = supabase.table("staff").update(staff_data).eq("id", staff_id).execute()
    return response.data[0] if response.data else None

# Staff services functions
def get_staff_services(staff_id):
    """Get all services for a staff member"""
    response = supabase.table("staff_services").select("*,services(*)").eq("staff_id", staff_id).execute()
    return response.data

def assign_service_to_staff(staff_id, service_id):
    """Assign a service to a staff member"""
    staff_service_data = {
        "staff_id": staff_id,
        "service_id": service_id
    }
    response = supabase.table("staff_services").insert(staff_service_data).execute()
    return response.data[0] if response.data else None

def remove_service_from_staff(staff_id, service_id):
    """Remove a service from a staff member"""
    response = supabase.table("staff_services").delete().eq("staff_id", staff_id).eq("service_id", service_id).execute()
    return response.data[0] if response.data else None

# Staff schedules functions
def get_staff_schedules(staff_id):
    """Get all schedules for a staff member"""
    response = supabase.table("staff_schedules").select("*").eq("staff_id", staff_id).execute()
    return response.data

def get_staff_schedule_by_day(staff_id, day_of_week):
    """Get staff schedule for a specific day"""
    response = supabase.table("staff_schedules").select("*").eq("staff_id", staff_id).eq("day_of_week", day_of_week).execute()
    return response.data[0] if response.data else None

def create_staff_schedule(staff_id, day_of_week, start_time, end_time, is_working=True):
    """Create a staff schedule for a specific day"""
    schedule_data = {
        "staff_id": staff_id,
        "day_of_week": day_of_week,
        "start_time": start_time,
        "end_time": end_time,
        "is_working": is_working
    }
    response = supabase.table("staff_schedules").insert(schedule_data).execute()
    return response.data[0] if response.data else None

def update_staff_schedule(schedule_id, schedule_data):
    """Update a staff schedule by ID"""
    response = supabase.table("staff_schedules").update(schedule_data).eq("id", schedule_id).execute()
    return response.data[0] if response.data else None

# Client functions
def get_clients(business_id):
    """Get all clients for a business"""
    response = supabase.table("clients").select("*").eq("business_id", business_id).execute()
    return response.data

def get_client(client_id):
    """Get a client by ID"""
    response = supabase.table("clients").select("*").eq("id", client_id).execute()
    return response.data[0] if response.data else None

def create_client(business_id, first_name, last_name, email=None, phone=None, date_of_birth=None, preferred_staff_id=None, notes=None):
    """Create a new client"""
    client_data = {
        "business_id": business_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "date_of_birth": date_of_birth,
        "preferred_staff_id": preferred_staff_id,
        "notes": notes
    }
    response = supabase.table("clients").insert(client_data).execute()
    return response.data[0] if response.data else None

def update_client(client_id, client_data):
    """Update a client by ID"""
    response = supabase.table("clients").update(client_data).eq("id", client_id).execute()
    return response.data[0] if response.data else None

# Client notes functions
def get_client_notes(client_id):
    """Get all notes for a client"""
    response = supabase.table("client_notes").select("*,staff(first_name,last_name)").eq("client_id", client_id).execute()
    return response.data

def create_client_note(client_id, note_text, staff_id=None):
    """Create a new note for a client"""
    note_data = {
        "client_id": client_id,
        "staff_id": staff_id,
        "note_text": note_text
    }
    response = supabase.table("client_notes").insert(note_data).execute()
    return response.data[0] if response.data else None

# Appointment functions
def get_appointments(business_id, status=None, start_date=None, end_date=None):
    """Get appointments for a business with optional filters"""
    query = supabase.table("appointments").select("*,clients(first_name,last_name),services(name),staff(first_name,last_name)").eq("business_id", business_id)
    
    if status:
        query = query.eq("status", status)
    
    if start_date:
        query = query.gte("start_time", start_date)
    
    if end_date:
        query = query.lte("start_time", end_date)
    
    response = query.order("start_time").execute()
    return response.data

def get_client_appointments(client_id, status=None):
    """Get appointments for a specific client"""
    query = supabase.table("appointments").select("*,services(name),staff(first_name,last_name)").eq("client_id", client_id)
    
    if status:
        query = query.eq("status", status)
    
    response = query.order("start_time").execute()
    return response.data

def get_appointment(appointment_id):
    """Get an appointment by ID"""
    response = supabase.table("appointments").select("*,clients(first_name,last_name),services(name),staff(first_name,last_name)").eq("id", appointment_id).execute()
    return response.data[0] if response.data else None

def get_available_slots(service_id, date):
    """Get available time slots for a service on a specific date"""
    # First, get the service to know its duration
    service_response = supabase.table("services").select("*,businesses(*)").eq("id", service_id).execute()
    if not service_response.data:
        return []

    service = service_response.data[0]
    business = service["businesses"]
    duration = service["duration"]

    # Get business hours for the specific day
    day_of_week = datetime.strptime(date, "%Y-%m-%d").strftime("%A").lower()
    hours_str = business["business_hours"][day_of_week]

    if hours_str == "closed":
        return []

    # Parse hours
    start_time, end_time = hours_str.split("-")
    start_hour, start_minute = map(int, start_time.split(":"))
    end_hour, end_minute = map(int, end_time.split(":"))

    # Create time slots
    slots = []
    current = datetime.strptime(f"{date} {start_hour}:{start_minute}", "%Y-%m-%d %H:%M")
    end = datetime.strptime(f"{date} {end_hour}:{end_minute}", "%Y-%m-%d %H:%M")

    while current + timedelta(minutes=duration) <= end:
        slots.append(current.strftime("%H:%M"))
        current += timedelta(minutes=duration)

    # Get booked appointments for that day
    appointments_response = supabase.table("appointments").select("start_time").eq("service_id", service_id).eq("date", date).execute()
    booked_times = [appointment["start_time"] for appointment in appointments_response.data]

    # Filter out booked slots
    available_slots = [slot for slot in slots if slot not in booked_times]

    return available_slots

def create_appointment(business_id, client_id, service_id, start_time, staff_id=None, notes=None):
    """Create a new appointment"""
    # Get service to calculate end_time
    service = get_service(service_id)
    if not service:
        return None
    
    # Parse start_time
    start_datetime = datetime.fromisoformat(start_time)
    
    # Calculate end_time
    end_datetime = start_datetime + timedelta(minutes=service["duration"])
    
    appointment_data = {
        "business_id": business_id,
        "client_id": client_id,
        "service_id": service_id,
        "staff_id": staff_id,
        "start_time": start_datetime.isoformat(),
        "end_time": end_datetime.isoformat(),
        "status": "scheduled",
        "notes": notes
    }

    response = supabase.table("appointments").insert(appointment_data).execute()
    return response.data[0] if response.data else None

def update_appointment_status(appointment_id, status):
    """Update the status of an appointment"""
    valid_statuses = ["scheduled", "confirmed", "completed", "cancelled", "no-show"]
    if status not in valid_statuses:
        raise ValueError(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
    
    response = supabase.table("appointments").update({"status": status}).eq("id", appointment_id).execute()
    return response.data[0] if response.data else None

# Appointment reminders functions
def get_appointment_reminders(appointment_id):
    """Get all reminders for an appointment"""
    response = supabase.table("appointment_reminders").select("*").eq("appointment_id", appointment_id).execute()
    return response.data

def create_appointment_reminder(appointment_id, reminder_type, scheduled_time):
    """Create a new appointment reminder"""
    valid_types = ["email", "sms"]
    if reminder_type not in valid_types:
        raise ValueError(f"Invalid reminder type. Must be one of: {', '.join(valid_types)}")
    
    reminder_data = {
        "appointment_id": appointment_id,
        "reminder_type": reminder_type,
        "scheduled_time": scheduled_time,
        "status": "pending"
    }
    
    response = supabase.table("appointment_reminders").insert(reminder_data).execute()
    return response.data[0] if response.data else None

def send_appointment_reminder(reminder_id):
    """Send an appointment reminder (mock function)"""
    # In a real application, this would integrate with email/SMS services
    # For now, we'll just update the status to "sent"
    
    # Get the reminder
    reminder_response = supabase.table("appointment_reminders").select("*,appointments(*)").eq("id", reminder_id).execute()
    if not reminder_response.data:
        return None
    
    reminder = reminder_response.data[0]
    
    # Update the reminder status
    response = supabase.table("appointment_reminders").update({
        "status": "sent",
        "sent_at": datetime.now().isoformat()
    }).eq("id", reminder_id).execute()
    
    return response.data[0] if response.data else None

def send_all_pending_reminders():
    """Send all pending reminders that are due"""
    # Get all pending reminders where scheduled_time is in the past
    now = datetime.now().isoformat()
    reminders_response = supabase.table("appointment_reminders").select("id").eq("status", "pending").lte("scheduled_time", now).execute()
    
    sent_reminders = []
    for reminder in reminders_response.data:
        sent_reminder = send_appointment_reminder(reminder["id"])
        if sent_reminder:
            sent_reminders.append(sent_reminder)
    
    return sent_reminders

# Payment functions
def get_payments(appointment_id=None):
    """Get payments with optional appointment filter"""
    if appointment_id:
        response = supabase.table("payments").select("*").eq("appointment_id", appointment_id).execute()
    else:
        response = supabase.table("payments").select("*").execute()
    
    return response.data

def create_payment(appointment_id, amount, payment_method):
    """Create a new payment for an appointment"""
    payment_data = {
        "appointment_id": appointment_id,
        "amount": amount,
        "payment_method": payment_method,
        "payment_status": "pending",
        "payment_date": datetime.now().isoformat()
    }
    
    response = supabase.table("payments").insert(payment_data).execute()
    return response.data[0] if response.data else None

def process_payment(payment_id, transaction_id=None):
    """Process a payment (mock function)"""
    # In a real application, this would integrate with payment processors
    # For now, we'll just update the status to "completed"
    
    payment_data = {
        "payment_status": "completed",
        "transaction_id": transaction_id or f"TRANS-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    }
    
    response = supabase.table("payments").update(payment_data).eq("id", payment_id).execute()
    return response.data[0] if response.data else None

def refund_payment(payment_id, amount=None):
    """Refund a payment (mock function)"""
    # Get the payment
    payment_response = supabase.table("payments").select("*").eq("id", payment_id).execute()
    if not payment_response.data:
        return None
    
    payment = payment_response.data[0]
    
    # Determine refund status
    if amount and amount < payment["amount"]:
        status = "partially_refunded"
    else:
        status = "refunded"
        amount = payment["amount"]
    
    # Update the payment
    response = supabase.table("payments").update({
        "payment_status": status
    }).eq("id", payment_id).execute()
    
    return response.data[0] if response.data else None

# Utility functions
def show_current_business_hours(business_id):
    """Show the current business hours in a formatted way"""
    business_hours = get_business_hours(business_id)
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    formatted_hours = {}
    
    for day_num, day_name in enumerate(days):
        day_hours = next((h for h in business_hours if h["day_of_week"] == day_num), None)
        
        if day_hours and not day_hours["is_closed"]:
            formatted_hours[day_name] = f"{day_hours['open_time']} - {day_hours['close_time']}"
        else:
            formatted_hours[day_name] = "Closed"
    
    return formatted_hours

def view_current_appointments(business_id, date=None):
    """View appointments for today or a specific date"""
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    start_of_day = f"{date}T00:00:00"
    end_of_day = f"{date}T23:59:59"
    
    appointments = get_appointments(business_id, start_date=start_of_day, end_date=end_of_day)
    
    # Format appointments for display
    formatted_appointments = []
    for appointment in appointments:
        client_name = f"{appointment['clients']['first_name']} {appointment['clients']['last_name']}"
        service_name = appointment['services']['name']
        start_time = datetime.fromisoformat(appointment['start_time']).strftime("%H:%M")
        end_time = datetime.fromisoformat(appointment['end_time']).strftime("%H:%M")
        
        staff_name = "Unassigned"
        if appointment['staff'] and appointment['staff']['first_name']:
            staff_name = f"{appointment['staff']['first_name']} {appointment['staff']['last_name']}"
        
        formatted_appointments.append({
            "id": appointment['id'],
            "time": f"{start_time} - {end_time}",
            "client": client_name,
            "service": service_name,
            "staff": staff_name,
            "status": appointment['status']
        })
    
    return formatted_appointments