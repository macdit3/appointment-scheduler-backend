# Prompts to Generate functions and their testing script:

Context:
I am building a small business appointment scheduler full-stack application. I want to create a python script to interact with my database which consists of 13 tables.  Follow the provide example of pre-defined functions to create additional functions of each other’s named tables.
Do not output the response on notebook, output the response as a Python file called
appointments.py script.

Tasks:
-	Based on the provided appointments.py file <>, I want you to create additional function to test the rest of my database tables contents. Use the provided  DDL  of my database to generate additional testing functions similar to the one on appointment file.
-	In short, I want to generated functions to be use later for testing my 13 tables contents. I should be able to perform the similar operations specified on appointments.py file.
-	I am expecting a new file called appointment.py with functions to interact with my database content like the following functions:
•	Function to send appointment reminders 
•	Functions to make an appointment 
•	Function to view the current appointment
•	Function to show the current business hours
•	Function to allow client sent a note to business
•	Function to allow clients make payment
•	Function to show all the clients
•	Function to interact with staff table contents
•	Function to allow staff making schedules
•	Function to show allow interact with staff services.
-	You can add additional function that are common used by small businesses.

Examples or format:

'''

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
    
    def get_business(business_id):
        """Get a business by ID"""
        response = supabase.table("businesses").select("*").eq("id", business_id).execute()
        return response.data[0] if response.data else None
    
    def get_services(business_id):
        """Get all services for a business"""
        response = supabase.table("services").select("*").eq("business_id", business_id).execute()
        return response.data
    
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
    
    def create_appointment(service_id, client_id, date, start_time):
        """Create a new appointment"""
        appointment_data = {
            "service_id": service_id,
            "client_id": client_id,
            "date": date,
            "start_time": start_time,
            "status": "scheduled"
        }
    
        response = supabase.table("appointments").insert(appointment_data).execute()
        return response.data[0] if response.data else None
    
    # Add more functions as needed

'''

