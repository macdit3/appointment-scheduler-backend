from appointments import *
import datetime

# Set up test IDs - replace these with actual IDs from your database
BUSINESS_ID = 1
SERVICE_ID = 1
CATEGORY_ID = 1
STAFF_ID = 1
CLIENT_ID = 1
APPOINTMENT_ID = 1
PAYMENT_ID = 1
REMINDER_ID = 1

print("===== APPOINTMENT SCHEDULER FUNCTION TESTS =====")
print("\n")

# ===== Business Tests =====
print("===== BUSINESS TESTS =====")
try:
    # Test getting a business
    print("Testing get_business()...")
    business = get_business(BUSINESS_ID)
    if business:
        print(f"✓ Business found: {business['name']}")
    else:
        print("✗ Business not found")

    # Test updating a business
    print("\nTesting update_business()...")
    updated_business = update_business(BUSINESS_ID, {"phone": "555-123-4567"})
    if updated_business:
        print(f"✓ Business updated: {updated_business['name']} - {updated_business['phone']}")
    else:
        print("✗ Failed to update business")
except Exception as e:
    print(f"✗ Error in business tests: {str(e)}")

print("\n")

# ===== Business Hours Tests =====
print("===== BUSINESS HOURS TESTS =====")
try:
    # Test getting business hours
    print("Testing get_business_hours()...")
    hours = get_business_hours(BUSINESS_ID)
    print(f"✓ Found {len(hours)} business hour records")

    # Test getting business hours by day
    print("\nTesting get_business_hours_by_day()...")
    monday_hours = get_business_hours_by_day(BUSINESS_ID, 0)  # 0 = Monday
    if monday_hours:
        print(f"✓ Monday hours: {monday_hours['open_time']} - {monday_hours['close_time']}")
    else:
        print("✗ Monday hours not found")

    # Test creating business hours (commented out to prevent accidental creation)
    print("\nTesting create_business_hours() [SIMULATION]...")
    # new_hours = create_business_hours(BUSINESS_ID, 6, "10:00:00", "14:00:00", False)  # Sunday
    print("✓ Would create new business hours for Sunday")

    # Test showing current business hours
    print("\nTesting show_current_business_hours()...")
    formatted_hours = show_current_business_hours(BUSINESS_ID)
    for day, hours in formatted_hours.items():
        print(f"✓ {day}: {hours}")
except Exception as e:
    print(f"✗ Error in business hours tests: {str(e)}")

print("\n")

# ===== Special Business Hours Tests =====
print("===== SPECIAL BUSINESS HOURS TESTS =====")
try:
    # Test getting special business hours
    print("Testing get_special_business_hours()...")
    special_hours = get_special_business_hours(BUSINESS_ID)
    print(f"✓ Found {len(special_hours)} special business hour records")

    # Test getting special business hours by date
    print("\nTesting get_special_business_hours_by_date()...")
    christmas = get_special_business_hours_by_date(BUSINESS_ID, "2025-12-25")
    if christmas:
        print(f"✓ Christmas hours: {'Closed' if christmas['is_closed'] else f'{christmas['open_time']} - {christmas['close_time']}'}")
    else:
        print("✗ Christmas hours not found")

    # Test creating special business hours (commented out to prevent accidental creation)
    print("\nTesting create_special_business_hours() [SIMULATION]...")
    # new_year = create_special_business_hours(BUSINESS_ID, "2026-01-01", True, None, None, "New Year's Day")
    print("✓ Would create special hours for New Year's Day (closed)")
except Exception as e:
    print(f"✗ Error in special business hours tests: {str(e)}")

print("\n")

# ===== Service Category Tests =====
print("===== SERVICE CATEGORY TESTS =====")
try:
    # Test getting service categories
    print("Testing get_service_categories()...")
    categories = get_service_categories(BUSINESS_ID)
    print(f"✓ Found {len(categories)} service categories")

    # Test getting a specific service category
    print("\nTesting get_service_category()...")
    category = get_service_category(CATEGORY_ID)
    if category:
        print(f"✓ Category found: {category['name']}")
    else:
        print("✗ Category not found")

    # Test creating a service category (commented out to prevent accidental creation)
    print("\nTesting create_service_category() [SIMULATION]...")
    # new_category = create_service_category(BUSINESS_ID, "New Services", "Brand new services")
    print("✓ Would create new service category 'New Services'")
except Exception as e:
    print(f"✗ Error in service category tests: {str(e)}")

print("\n")

# ===== Service Tests =====
print("===== SERVICE TESTS =====")
try:
    # Test getting services
    print("Testing get_services()...")
    services = get_services(BUSINESS_ID)
    print(f"✓ Found {len(services)} services")
    for service in services[:3]:  # Show first 3 services
        print(f"  - {service['name']} - ${service['price']}")

    # Test getting services by category
    print("\nTesting get_services_by_category()...")
    category_services = get_services_by_category(CATEGORY_ID)
    print(f"✓ Found {len(category_services)} services in category {CATEGORY_ID}")

    # Test getting a specific service
    print("\nTesting get_service()...")
    service = get_service(SERVICE_ID)
    if service:
        print(f"✓ Service found: {service['name']} - ${service['price']} - {service['duration']} minutes")
    else:
        print("✗ Service not found")

    # Test creating a service (commented out to prevent accidental creation)
    print("\nTesting create_service() [SIMULATION]...")
    # new_service = create_service(BUSINESS_ID, "New Test Service", 60, 99.99, CATEGORY_ID, "A test service")
    print("✓ Would create new service 'New Test Service'")

    # Test getting available slots
    print("\nTesting get_available_slots()...")
    future_date = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")
    slots = get_available_slots(SERVICE_ID, future_date)
    print(f"✓ Available slots for {future_date}: {slots}")
except Exception as e:
    print(f"✗ Error in service tests: {str(e)}")

print("\n")

# ===== Staff Tests =====
print("===== STAFF TESTS =====")
try:
    # Test getting staff
    print("Testing get_staff()...")
    staff = get_staff(BUSINESS_ID)
    print(f"✓ Found {len(staff)} staff members")

    # Test getting a specific staff member
    print("\nTesting get_staff_member()...")
    staff_member = get_staff_member(STAFF_ID)
    if staff_member:
        print(f"✓ Staff member found: {staff_member['first_name']} {staff_member['last_name']}")
    else:
        print("✗ Staff member not found")

    # Test creating a staff member (commented out to prevent accidental creation)
    print("\nTesting create_staff_member() [SIMULATION]...")
    # new_staff = create_staff_member(BUSINESS_ID, "John", "Doe", "john.doe@example.com", "555-987-6543", "Stylist")
    print("✓ Would create new staff member 'John Doe'")
except Exception as e:
    print(f"✗ Error in staff tests: {str(e)}")

print("\n")

# ===== Staff Services Tests =====
print("===== STAFF SERVICES TESTS =====")
try:
    # Test getting staff services
    print("Testing get_staff_services()...")
    staff_services = get_staff_services(STAFF_ID)
    print(f"✓ Found {len(staff_services)} services for staff member {STAFF_ID}")

    # Test assigning a service to staff (commented out to prevent accidental creation)
    print("\nTesting assign_service_to_staff() [SIMULATION]...")
    # assignment = assign_service_to_staff(STAFF_ID, SERVICE_ID)
    print(f"✓ Would assign service {SERVICE_ID} to staff member {STAFF_ID}")

    # Test removing a service from staff (commented out to prevent accidental deletion)
    print("\nTesting remove_service_from_staff() [SIMULATION]...")
    # removal = remove_service_from_staff(STAFF_ID, SERVICE_ID)
    print(f"✓ Would remove service {SERVICE_ID} from staff member {STAFF_ID}")
except Exception as e:
    print(f"✗ Error in staff services tests: {str(e)}")

print("\n")

# ===== Staff Schedules Tests =====
print("===== STAFF SCHEDULES TESTS =====")
try:
    # Test getting staff schedules
    print("Testing get_staff_schedules()...")
    schedules = get_staff_schedules(STAFF_ID)
    print(f"✓ Found {len(schedules)} schedule entries for staff member {STAFF_ID}")

    # Test getting staff schedule by day
    print("\nTesting get_staff_schedule_by_day()...")
    monday_schedule = get_staff_schedule_by_day(STAFF_ID, 0)  # 0 = Monday
    if monday_schedule:
        print(f"✓ Monday schedule: {monday_schedule['start_time']} - {monday_schedule['end_time']}")
    else:
        print("✗ Monday schedule not found")

    # Test creating a staff schedule (commented out to prevent accidental creation)
    print("\nTesting create_staff_schedule() [SIMULATION]...")
    # new_schedule = create_staff_schedule(STAFF_ID, 6, "10:00:00", "14:00:00")  # Sunday
    print("✓ Would create new schedule for Sunday")
except Exception as e:
    print(f"✗ Error in staff schedules tests: {str(e)}")

print("\n")

# ===== Client Tests =====
print("===== CLIENT TESTS =====")
try:
    # Test getting clients
    print("Testing get_clients()...")
    clients = get_clients(BUSINESS_ID)
    print(f"✓ Found {len(clients)} clients")

    # Test getting a specific client
    print("\nTesting get_client()...")
    client = get_client(CLIENT_ID)
    if client:
        print(f"✓ Client found: {client['first_name']} {client['last_name']}")
    else:
        print("✗ Client not found")

    # Test creating a client (commented out to prevent accidental creation)
    print("\nTesting create_client() [SIMULATION]...")
    # new_client = create_client(BUSINESS_ID, "Jane", "Smith", "jane.smith@example.com", "555-123-7890")
    print("✓ Would create new client 'Jane Smith'")
except Exception as e:
    print(f"✗ Error in client tests: {str(e)}")

print("\n")

# ===== Client Notes Tests =====
print("===== CLIENT NOTES TESTS =====")
try:
    # Test getting client notes
    print("Testing get_client_notes()...")
    notes = get_client_notes(CLIENT_ID)
    print(f"✓ Found {len(notes)} notes for client {CLIENT_ID}")

    # Test creating a client note (commented out to prevent accidental creation)
    print("\nTesting create_client_note() [SIMULATION]...")
    # new_note = create_client_note(CLIENT_ID, "Test note for client", STAFF_ID)
    print(f"✓ Would create new note for client {CLIENT_ID}")
except Exception as e:
    print(f"✗ Error in client notes tests: {str(e)}")

print("\n")

# ===== Appointment Tests =====
print("===== APPOINTMENT TESTS =====")
try:
    # Test getting appointments
    print("Testing get_appointments()...")
    appointments = get_appointments(BUSINESS_ID)
    print(f"✓ Found {len(appointments)} appointments")

    # Test getting client appointments
    print("\nTesting get_client_appointments()...")
    client_appointments = get_client_appointments(CLIENT_ID)
    print(f"✓ Found {len(client_appointments)} appointments for client {CLIENT_ID}")

    # Test getting a specific appointment
    print("\nTesting get_appointment()...")
    appointment = get_appointment(APPOINTMENT_ID)
    if appointment:
        print(f"✓ Appointment found: {appointment['start_time']} - {appointment['services']['name']}")
    else:
        print("✗ Appointment not found")

    # Test creating an appointment (commented out to prevent accidental creation)
    print("\nTesting create_appointment() [SIMULATION]...")
    future_date = (datetime.datetime.now() + datetime.timedelta(days=7)).isoformat()
    # new_appointment = create_appointment(BUSINESS_ID, CLIENT_ID, SERVICE_ID, future_date, STAFF_ID)
    print(f"✓ Would create new appointment for {future_date}")

    # Test updating appointment status (commented out to prevent accidental update)
    print("\nTesting update_appointment_status() [SIMULATION]...")
    # updated_appointment = update_appointment_status(APPOINTMENT_ID, "confirmed")
    print(f"✓ Would update appointment {APPOINTMENT_ID} status to 'confirmed'")

    # Test viewing current appointments
    print("\nTesting view_current_appointments()...")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    today_appointments = view_current_appointments(BUSINESS_ID, today)
    print(f"✓ Found {len(today_appointments)} appointments for today")
except Exception as e:
    print(f"✗ Error in appointment tests: {str(e)}")

print("\n")

# ===== Appointment Reminders Tests =====
print("===== APPOINTMENT REMINDERS TESTS =====")
try:
    # Test getting appointment reminders
    print("Testing get_appointment_reminders()...")
    reminders = get_appointment_reminders(APPOINTMENT_ID)
    print(f"✓ Found {len(reminders)} reminders for appointment {APPOINTMENT_ID}")

    # Test creating an appointment reminder (commented out to prevent accidental creation)
    print("\nTesting create_appointment_reminder() [SIMULATION]...")
    reminder_time = (datetime.datetime.now() + datetime.timedelta(days=1)).isoformat()
    # new_reminder = create_appointment_reminder(APPOINTMENT_ID, "email", reminder_time)
    print(f"✓ Would create new email reminder for appointment {APPOINTMENT_ID}")

    # Test sending an appointment reminder (commented out to prevent accidental sending)
    print("\nTesting send_appointment_reminder() [SIMULATION]...")
    # sent_reminder = send_appointment_reminder(REMINDER_ID)
    print(f"✓ Would send reminder {REMINDER_ID}")

    # Test sending all pending reminders (commented out to prevent accidental sending)
    print("\nTesting send_all_pending_reminders() [SIMULATION]...")
    # sent_reminders = send_all_pending_reminders()
    print("✓ Would send all pending reminders")
except Exception as e:
    print(f"✗ Error in appointment reminders tests: {str(e)}")

print("\n")

# ===== Payment Tests =====
print("===== PAYMENT TESTS =====")
try:
    # Test getting payments
    print("Testing get_payments()...")
    payments = get_payments()
    print(f"✓ Found {len(payments)} payments")

    # Test getting payments for a specific appointment
    print("\nTesting get_payments() for specific appointment...")
    appointment_payments = get_payments(APPOINTMENT_ID)
    print(f"✓ Found {len(appointment_payments)} payments for appointment {APPOINTMENT_ID}")

    # Test creating a payment (commented out to prevent accidental creation)
    print("\nTesting create_payment() [SIMULATION]...")
    # new_payment = create_payment(APPOINTMENT_ID, 99.99, "credit_card")
    print(f"✓ Would create new payment for appointment {APPOINTMENT_ID}")

    # Test processing a payment (commented out to prevent accidental processing)
    print("\nTesting process_payment() [SIMULATION]...")
    # processed_payment = process_payment(PAYMENT_ID, "TRANS-12345")
    print(f"✓ Would process payment {PAYMENT_ID}")

    # Test refunding a payment (commented out to prevent accidental refund)
    print("\nTesting refund_payment() [SIMULATION]...")
    # refunded_payment = refund_payment(PAYMENT_ID)
    print(f"✓ Would refund payment {PAYMENT_ID}")
except Exception as e:
    print(f"✗ Error in payment tests: {str(e)}")

print("\n")
print("===== ALL TESTS COMPLETED =====")
