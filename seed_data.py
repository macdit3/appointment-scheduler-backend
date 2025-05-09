import os
from dotenv import load_dotenv
from supabase import create_client, Client
import random
from datetime import datetime, time, timedelta

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

# Sample data for businesses
businesses = [
    {
        "name": "Stylish Cuts Barbershop",
        "address": "123 Main St, Boston, MA",
        "phone": "555-123-4567",
        "email": "info@stylishcuts.example",
        "website": "www.stylishcuts.example",
        "timezone": "America/New_York",
        "cancellation_policy": "24 hours notice required for cancellation"
    },
    {
        "name": "Elegant Nails Salon",
        "address": "456 Oak Ave, Boston, MA",
        "phone": "555-234-5678",
        "email": "info@elegantnails.example",
        "website": "www.elegantnails.example",
        "timezone": "America/New_York",
        "cancellation_policy": "Please provide 12 hours notice for cancellations"
    },
    {
        "name": "Wellness Massage Center",
        "address": "789 Pine Blvd, Boston, MA",
        "phone": "555-345-6789",
        "email": "info@wellnessmassage.example",
        "website": "www.wellnessmassage.example",
        "timezone": "America/New_York",
        "cancellation_policy": "48 hours notice required for cancellation"
    },
    {
        "name": "Perfect Smile Dental",
        "address": "101 Cedar St, Boston, MA",
        "phone": "555-456-7890",
        "email": "info@perfectsmile.example",
        "website": "www.perfectsmile.example",
        "timezone": "America/New_York",
        "cancellation_policy": "24 hours notice required for cancellation"
    },
    {
        "name": "Fitness First Gym",
        "address": "202 Maple Rd, Boston, MA",
        "phone": "555-567-8901",
        "email": "info@fitnessfirst.example",
        "website": "www.fitnessfirst.example",
        "timezone": "America/New_York",
        "cancellation_policy": "No refunds for missed sessions"
    },
    {
        "name": "Serene Spa Retreat",
        "address": "303 Birch Ln, Boston, MA",
        "phone": "555-678-9012",
        "email": "info@serenespa.example",
        "website": "www.serenespa.example",
        "timezone": "America/New_York",
        "cancellation_policy": "48 hours notice required for cancellation"
    },
    {
        "name": "Tech Repair Solutions",
        "address": "404 Elm St, Boston, MA",
        "phone": "555-789-0123",
        "email": "info@techrepair.example",
        "website": "www.techrepair.example",
        "timezone": "America/New_York",
        "cancellation_policy": "No fee for cancellations"
    },
    {
        "name": "Clean Car Auto Detailing",
        "address": "505 Walnut Ave, Boston, MA",
        "phone": "555-890-1234",
        "email": "info@cleancar.example",
        "website": "www.cleancar.example",
        "timezone": "America/New_York",
        "cancellation_policy": "24 hours notice required for cancellation"
    },
    {
        "name": "Pet Grooming Paradise",
        "address": "606 Spruce Blvd, Boston, MA",
        "phone": "555-901-2345",
        "email": "info@petgrooming.example",
        "website": "www.petgrooming.example",
        "timezone": "America/New_York",
        "cancellation_policy": "12 hours notice required for cancellation"
    },
    {
        "name": "Academic Tutoring Center",
        "address": "707 Aspen Rd, Boston, MA",
        "phone": "555-012-3456",
        "email": "info@academictutoring.example",
        "website": "www.academictutoring.example",
        "timezone": "America/New_York",
        "cancellation_policy": "24 hours notice required for cancellation"
    }
]

# Sample data for business_hours
# Will be populated after businesses are created

# Sample data for service_categories
service_categories_templates = [
    {
        "name": "Haircuts",
        "description": "All types of haircuts and styling services"
    },
    {
        "name": "Nail Services",
        "description": "Manicures, pedicures, and nail art"
    },
    {
        "name": "Massage Therapy",
        "description": "Various massage techniques for relaxation and therapy"
    },
    {
        "name": "Dental Procedures",
        "description": "Regular check-ups and dental treatments"
    },
    {
        "name": "Fitness Training",
        "description": "Personal and group fitness sessions"
    },
    {
        "name": "Spa Treatments",
        "description": "Facials, body wraps, and other spa services"
    },
    {
        "name": "Tech Services",
        "description": "Phone, computer, and other device repairs"
    },
    {
        "name": "Auto Detailing",
        "description": "Interior and exterior car cleaning services"
    },
    {
        "name": "Pet Services",
        "description": "Grooming, bathing, and styling for pets"
    },
    {
        "name": "Tutoring Sessions",
        "description": "Academic help for various subjects and levels"
    }
]

# Sample data for services
services_templates = [
    {
        "name": "Men's Haircut",
        "description": "Classic haircut with clippers and scissors",
        "duration": 30,
        "buffer_time": 5,
        "max_clients": 1,
        "price": 25.00,
        "is_active": True
    },
    {
        "name": "Women's Haircut",
        "description": "Haircut and style for women",
        "duration": 45,
        "buffer_time": 5,
        "max_clients": 1,
        "price": 40.00,
        "is_active": True
    },
    {
        "name": "Basic Manicure",
        "description": "Nail shaping, cuticle care, and polish",
        "duration": 30,
        "buffer_time": 5,
        "max_clients": 1,
        "price": 25.00,
        "is_active": True
    },
    {
        "name": "Swedish Massage",
        "description": "Relaxing full-body massage",
        "duration": 60,
        "buffer_time": 10,
        "max_clients": 1,
        "price": 80.00,
        "is_active": True
    },
    {
        "name": "Dental Cleaning",
        "description": "Professional teeth cleaning",
        "duration": 45,
        "buffer_time": 15,
        "max_clients": 1,
        "price": 120.00,
        "is_active": True
    },
    {
        "name": "Personal Training Session",
        "description": "One-on-one fitness training",
        "duration": 60,
        "buffer_time": 10,
        "max_clients": 1,
        "price": 70.00,
        "is_active": True
    },
    {
        "name": "Facial Treatment",
        "description": "Deep cleansing facial with massage",
        "duration": 60,
        "buffer_time": 10,
        "max_clients": 1,
        "price": 90.00,
        "is_active": True
    },
    {
        "name": "Phone Screen Repair",
        "description": "Replacement of cracked or damaged screens",
        "duration": 45,
        "buffer_time": 5,
        "max_clients": 1,
        "price": 80.00,
        "is_active": True
    },
    {
        "name": "Full Car Detailing",
        "description": "Complete interior and exterior cleaning",
        "duration": 120,
        "buffer_time": 15,
        "max_clients": 1,
        "price": 150.00,
        "is_active": True
    },
    {
        "name": "Dog Grooming",
        "description": "Bath, haircut, and nail trimming for dogs",
        "duration": 60,
        "buffer_time": 10,
        "max_clients": 1,
        "price": 65.00,
        "is_active": True
    }
]

# Sample data for staff
staff_templates = [
    {
        "first_name": "John",
        "last_name": "Smith",
        "email": "john.smith@example.com",
        "phone": "555-111-2222",
        "position": "Senior Stylist",
        "is_active": True
    },
    {
        "first_name": "Emily",
        "last_name": "Johnson",
        "email": "emily.johnson@example.com",
        "phone": "555-222-3333",
        "position": "Nail Technician",
        "is_active": True
    },
    {
        "first_name": "Michael",
        "last_name": "Williams",
        "email": "michael.williams@example.com",
        "phone": "555-333-4444",
        "position": "Massage Therapist",
        "is_active": True
    },
    {
        "first_name": "Sarah",
        "last_name": "Brown",
        "email": "sarah.brown@example.com",
        "phone": "555-444-5555",
        "position": "Dental Hygienist",
        "is_active": True
    },
    {
        "first_name": "David",
        "last_name": "Jones",
        "email": "david.jones@example.com",
        "phone": "555-555-6666",
        "position": "Personal Trainer",
        "is_active": True
    },
    {
        "first_name": "Jennifer",
        "last_name": "Garcia",
        "email": "jennifer.garcia@example.com",
        "phone": "555-666-7777",
        "position": "Esthetician",
        "is_active": True
    },
    {
        "first_name": "Robert",
        "last_name": "Miller",
        "email": "robert.miller@example.com",
        "phone": "555-777-8888",
        "position": "Tech Specialist",
        "is_active": True
    },
    {
        "first_name": "Lisa",
        "last_name": "Davis",
        "email": "lisa.davis@example.com",
        "phone": "555-888-9999",
        "position": "Auto Detailer",
        "is_active": True
    },
    {
        "first_name": "James",
        "last_name": "Rodriguez",
        "email": "james.rodriguez@example.com",
        "phone": "555-999-0000",
        "position": "Pet Groomer",
        "is_active": True
    },
    {
        "first_name": "Michelle",
        "last_name": "Wilson",
        "email": "michelle.wilson@example.com",
        "phone": "555-000-1111",
        "position": "Tutor",
        "is_active": True
    }
]

# Sample data for clients
clients_templates = [
    {
        "first_name": "Alex",
        "last_name": "Taylor",
        "email": "alex.taylor@example.com",
        "phone": "555-123-9876",
        "date_of_birth": "1985-06-15",
        "notes": "Prefers afternoon appointments"
    },
    {
        "first_name": "Jessica",
        "last_name": "Martinez",
        "email": "jessica.martinez@example.com",
        "phone": "555-234-8765",
        "date_of_birth": "1990-03-22",
        "notes": "Allergic to certain hair products"
    },
    {
        "first_name": "Daniel",
        "last_name": "Anderson",
        "email": "daniel.anderson@example.com",
        "phone": "555-345-7654",
        "date_of_birth": "1978-11-30",
        "notes": "Prefers quiet environment"
    },
    {
        "first_name": "Sophia",
        "last_name": "Thomas",
        "email": "sophia.thomas@example.com",
        "phone": "555-456-6543",
        "date_of_birth": "1995-08-10",
        "notes": "New client"
    },
    {
        "first_name": "William",
        "last_name": "Jackson",
        "email": "william.jackson@example.com",
        "phone": "555-567-5432",
        "date_of_birth": "1982-04-05",
        "notes": "Prefers early morning appointments"
    },
    {
        "first_name": "Olivia",
        "last_name": "White",
        "email": "olivia.white@example.com",
        "phone": "555-678-4321",
        "date_of_birth": "1988-09-18",
        "notes": "Has back issues"
    },
    {
        "first_name": "Ethan",
        "last_name": "Harris",
        "email": "ethan.harris@example.com",
        "phone": "555-789-3210",
        "date_of_birth": "1975-12-03",
        "notes": "Regular client"
    },
    {
        "first_name": "Ava",
        "last_name": "Clark",
        "email": "ava.clark@example.com",
        "phone": "555-890-2109",
        "date_of_birth": "1992-07-25",
        "notes": "Prefers female staff"
    },
    {
        "first_name": "Noah",
        "last_name": "Lewis",
        "email": "noah.lewis@example.com",
        "phone": "555-901-1098",
        "date_of_birth": "1980-02-14",
        "notes": "Has a service dog"
    },
    {
        "first_name": "Emma",
        "last_name": "Walker",
        "email": "emma.walker@example.com",
        "phone": "555-012-0987",
        "date_of_birth": "1993-05-20",
        "notes": "Prefers text message reminders"
    }
]

# Other sample data will be populated after the related tables are created

# Insert businesses
def seed_businesses():
    print("Seeding businesses...")
    for business in businesses:
        try:
            response = supabase.table("businesses").insert(business).execute()
            print(f"Added business: {business['name']}")
        except Exception as e:
            print(f"Error adding business {business['name']}: {e}")

# Insert business_hours
def seed_business_hours():
    print("Seeding business hours...")
    # First get business IDs
    response = supabase.table("businesses").select("id, name").execute()
    business_data = response.data

    for business in business_data:
        # Create business hours for each day of the week
        for day in range(7):  # 0 = Monday, 6 = Sunday
            is_closed = day == 6  # Closed on Sundays

            business_hour = {
                "business_id": business["id"],
                "day_of_week": day,
                "open_time": "09:00:00" if not is_closed else None,
                "close_time": "17:00:00" if not is_closed else None,
                "is_closed": is_closed
            }

            try:
                supabase.table("business_hours").insert(business_hour).execute()
                status = "Closed" if is_closed else "Open 9:00-17:00"
                print(f"Added business hours for {business['name']}, Day {day}: {status}")
            except Exception as e:
                print(f"Error adding business hours for {business['name']}, Day {day}: {e}")

# Insert service categories
def seed_service_categories():
    print("Seeding service categories...")
    # First get business IDs
    response = supabase.table("businesses").select("id, name").execute()
    business_data = response.data

    for business in business_data:
        # Assign a relevant category based on business index
        business_index = business_data.index(business) % len(service_categories_templates)
        category = service_categories_templates[business_index].copy()
        category["business_id"] = business["id"]

        try:
            supabase.table("service_categories").insert(category).execute()
            print(f"Added service category: {category['name']} for {business['name']}")
        except Exception as e:
            print(f"Error adding service category {category['name']}: {e}")

# Insert services
def seed_services():
    print("Seeding services...")
    # First get business IDs and categories
    business_response = supabase.table("businesses").select("id, name").execute()
    business_data = business_response.data

    category_response = supabase.table("service_categories").select("id, business_id, name").execute()
    category_data = category_response.data

    for business in business_data:
        # Find categories for this business
        business_categories = [cat for cat in category_data if cat["business_id"] == business["id"]]
        category_id = business_categories[0]["id"] if business_categories else None

        # Add services for this business
        for i in range(10):  # 10 services per business
            service_index = i % len(services_templates)
            service = services_templates[service_index].copy()
            service["business_id"] = business["id"]
            service["category_id"] = category_id
            # Slightly modify the name to make it unique
            service["name"] = f"{service['name']} - {i+1}"

            try:
                supabase.table("services").insert(service).execute()
                print(f"Added service: {service['name']} for {business['name']}")
            except Exception as e:
                print(f"Error adding service {service['name']}: {e}")

# Insert staff
def seed_staff():
    print("Seeding staff...")
    # First get business IDs
    response = supabase.table("businesses").select("id, name").execute()
    business_data = response.data

    for business in business_data:
        # Add staff for this business
        for i in range(10):  # 10 staff per business
            staff_index = i % len(staff_templates)
            staff = staff_templates[staff_index].copy()
            staff["business_id"] = business["id"]
            # Modify email to make it unique
            staff["email"] = f"{i+1}.{staff['email']}"

            try:
                supabase.table("staff").insert(staff).execute()
                print(f"Added staff: {staff['first_name']} {staff['last_name']} for {business['name']}")
            except Exception as e:
                print(f"Error adding staff {staff['first_name']} {staff['last_name']}: {e}")

# Insert clients
def seed_clients():
    print("Seeding clients...")
    # First get business IDs
    response = supabase.table("businesses").select("id, name").execute()
    business_data = response.data

    for business in business_data:
        # Add clients for this business
        for i in range(10):  # 10 clients per business
            client_index = i % len(clients_templates)
            client = clients_templates[client_index].copy()
            client["business_id"] = business["id"]
            # Modify email to make it unique
            client["email"] = f"{i+1}.{client['email']}"

            try:
                supabase.table("clients").insert(client).execute()
                print(f"Added client: {client['first_name']} {client['last_name']} for {business['name']}")
            except Exception as e:
                print(f"Error adding client {client['first_name']} {client['last_name']}: {e}")

# Insert staff_services
def seed_staff_services():
    print("Seeding staff services...")
    # Get staff and services
    staff_response = supabase.table("staff").select("id, business_id, first_name, last_name").execute()
    staff_data = staff_response.data

    services_response = supabase.table("services").select("id, business_id, name").execute()
    services_data = services_response.data

    for staff in staff_data:
        # Find services for this staff's business
        business_services = [service for service in services_data if service["business_id"] == staff["business_id"]]

        # Assign 3 random services to each staff member
        if business_services:
            selected_services = random.sample(business_services, min(3, len(business_services)))

            for service in selected_services:
                staff_service = {
                    "staff_id": staff["id"],
                    "service_id": service["id"]
                }

                try:
                    supabase.table("staff_services").insert(staff_service).execute()
                    print(f"Added service: {service['name']} for staff {staff['first_name']} {staff['last_name']}")
                except Exception as e:
                    print(f"Error adding service {service['name']} for staff {staff['first_name']} {staff['last_name']}: {e}")

# Insert staff_schedules
def seed_staff_schedules():
    print("Seeding staff schedules...")
    # Get staff
    staff_response = supabase.table("staff").select("id, business_id, first_name, last_name").execute()
    staff_data = staff_response.data

    for staff in staff_data:
        # Create schedules for each day of the week
        for day in range(7):  # 0 = Monday, 6 = Sunday
            is_working = day < 6  # Not working on Sundays

            if is_working:
                schedule = {
                    "staff_id": staff["id"],
                    "day_of_week": day,
                    "start_time": "09:00:00",
                    "end_time": "17:00:00",
                    "is_working": True
                }

                try:
                    supabase.table("staff_schedules").insert(schedule).execute()
                    print(f"Added schedule for staff {staff['first_name']} {staff['last_name']}, Day {day}: Working 9:00-17:00")
                except Exception as e:
                    print(f"Error adding schedule for staff {staff['first_name']} {staff['last_name']}, Day {day}: {e}")

# Insert appointments
def seed_appointments():
    print("Seeding appointments...")
    # Get clients, services, and staff
    clients_response = supabase.table("clients").select("id, business_id, first_name, last_name").execute()
    clients_data = clients_response.data

    services_response = supabase.table("services").select("id, business_id, name, duration").execute()
    services_data = services_response.data

    staff_response = supabase.table("staff").select("id, business_id, first_name, last_name").execute()
    staff_data = staff_response.data

    # Group by business
    businesses_response = supabase.table("businesses").select("id, name").execute()
    businesses_data = businesses_response.data

    for business in businesses_data:
        # Get clients, services, and staff for this business
        business_clients = [client for client in clients_data if client["business_id"] == business["id"]]
        business_services = [service for service in services_data if service["business_id"] == business["id"]]
        business_staff = [staff for staff in staff_data if staff["business_id"] == business["id"]]

        if not business_clients or not business_services or not business_staff:
            continue

        # Create 10 appointments for this business
        for i in range(10):
            # Randomly select client, service, and staff
            client = random.choice(business_clients)
            service = random.choice(business_services)
            staff = random.choice(business_staff)

            # Create appointment in the next 30 days
            days_ahead = random.randint(1, 30)
            hour = random.randint(9, 16)  # 9 AM to 4 PM

            start_time = datetime.now() + timedelta(days=days_ahead)
            start_time = start_time.replace(hour=hour, minute=0, second=0, microsecond=0)

            # Calculate end time based on service duration
            end_time = start_time + timedelta(minutes=service["duration"])

            # Random status weighted towards "scheduled"
            status_options = ["scheduled", "confirmed", "completed", "cancelled", "no-show"]
            status_weights = [0.5, 0.2, 0.1, 0.1, 0.1]
            status = random.choices(status_options, status_weights)[0]

            appointment = {
                "business_id": business["id"],
                "client_id": client["id"],
                "service_id": service["id"],
                "staff_id": staff["id"],
                "start_time": start_time.isoformat(),
                "end_time": end_time.isoformat(),
                "status": status,
                "notes": "Automatically generated appointment"
            }

            try:
                response = supabase.table("appointments").insert(appointment).execute()
                print(f"Added appointment for client {client['first_name']} {client['last_name']} with {staff['first_name']} {staff['last_name']}")

                # Store the appointment ID for reminders and payments
                if response.data:
                    appointment_id = response.data[0]["id"]

                    # Create a reminder
                    reminder = {
                        "appointment_id": appointment_id,
                        "reminder_type": random.choice(["email", "sms"]),
                        "scheduled_time": (start_time - timedelta(days=1)).isoformat(),
                        "status": "pending"
                    }

                    try:
                        supabase.table("appointment_reminders").insert(reminder).execute()
                        print(f"Added reminder for appointment {appointment_id}")
                    except Exception as e:
                        print(f"Error adding reminder for appointment {appointment_id}: {e}")

                    # Create a payment if appointment is completed
                    if status == "completed":
                        payment = {
                            "appointment_id": appointment_id,
                            "amount": service["price"],
                            "payment_method": random.choice(["credit_card", "cash", "debit_card"]),
                            "payment_status": "completed",
                            "transaction_id": f"TXN-{random.randint(10000, 99999)}",
                            "payment_date": end_time.isoformat()
                        }

                        try:
                            supabase.table("payments").insert(payment).execute()
                            print(f"Added payment for appointment {appointment_id}")
                        except Exception as e:
                            print(f"Error adding payment for appointment {appointment_id}: {e}")
            except Exception as e:
                print(f"Error adding appointment: {e}")

# Insert appointment_reminders
# (Created in the appointments function)

# Insert special_business_hours
def seed_special_business_hours():
    print("Seeding special business hours...")
    # Get businesses
    businesses_response = supabase.table("businesses").select("id, name").execute()
    businesses_data = businesses_response.data

    for business in businesses_data:
        # Create 10 special business hours entries
        for i in range(10):
            # Random date in the next 90 days
            days_ahead = random.randint(1, 90)
            special_date = (datetime.now() + timedelta(days=days_ahead)).date()

            # 20% chance of being closed
            is_closed = random.random() < 0.2

            special_hours = {
                "business_id": business["id"],
                "date": special_date.isoformat(),
                "is_closed": is_closed
            }

            if not is_closed:
                # Special hours for open days
                special_hours["open_time"] = "10:00:00"
                special_hours["close_time"] = "16:00:00"
                special_hours["description"] = "Special hours for holiday season"
            else:
                special_hours["description"] = "Closed for holiday"

            try:
                supabase.table("special_business_hours").insert(special_hours).execute()
                status = "Closed" if is_closed else "Open 10:00-16:00"
                print(f"Added special hours for {business['name']} on {special_date}: {status}")
            except Exception as e:
                print(f"Error adding special hours for {business['name']} on {special_date}: {e}")

# Insert payments
# (Created in the appointments function)

# Insert client_notes
def seed_client_notes():
    print("Seeding client notes...")
    # Get clients and staff
    clients_response = supabase.table("clients").select("id, business_id, first_name, last_name").execute()
    clients_data = clients_response.data

    staff_response = supabase.table("staff").select("id, business_id, first_name, last_name").execute()
    staff_data = staff_response.data

    # Create 10 notes for random clients
    for i in range(10):
        # Randomly select a client
        client = random.choice(clients_data)

        # Find staff from the same business
        business_staff = [staff for staff in staff_data if staff["business_id"] == client["business_id"]]
        staff = random.choice(business_staff) if business_staff else None

        note_texts = [
            "Client arrived on time and was very satisfied with the service.",
            "Client requested a different stylist for next appointment.",
            "Client has allergies to certain products - check notes before service.",
            "Client prefers appointments in the morning.",
            "Client is a regular and has been coming for over a year.",
            "Client requested information about additional services.",
            "Client was 15 minutes late for appointment.",
            "Client referred by another customer.",
            "Client requested a specific product to be used.",
            "Client mentioned they might bring a friend next time."
        ]

        note = {
            "client_id": client["id"],
            "staff_id": staff["id"] if staff else None,
            "note_text": note_texts[i % len(note_texts)]
        }

        try:
            supabase.table("client_notes").insert(note).execute()
            print(f"Added note for client {client['first_name']} {client['last_name']}")
        except Exception as e:
            print(f"Error adding note for client {client['first_name']} {client['last_name']}: {e}")

# Main function to run all seeding functions
if __name__ == "__main__":
    # Seed in order of dependencies
    seed_businesses()
    seed_business_hours()
    seed_service_categories()
    seed_services()
    seed_staff()
    seed_clients()
    seed_staff_services()
    seed_staff_schedules()
    seed_appointments()  # This also seeds appointment_reminders and payments
    seed_special_business_hours()
    seed_client_notes()

    print("Database seeding completed!")
