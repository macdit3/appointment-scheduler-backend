#!/usr/bin/env python3
"""
Test script for appointments.py functions
"""
from appointments import get_business, get_services, get_available_slots, create_appointment

def main():
    # Test getting a business
    business_id = 1  # Use an actual ID from your database
    business = get_business(business_id)
    print(f"Business: {business['name'] if business else 'Not found'}")

    # Test getting services
    services = get_services(business_id)  # Use an actual business ID
    print(f"Services for business {business_id}:")
    for service in services:
        print(f"Service: {service['name']} - ${service['price']}")

    # Test getting available slots
    if services:
        service_id = services[0]['id']  # Use the first service
        date = "2025-03-18"  # Use actual date
        slots = get_available_slots(service_id, date)
        print(f"Available slots for service {service_id} on {date}:")
        print(f"Available slots: {slots}")

    # Uncomment to test appointment creation
    # client_id = 1  # Use actual client ID
    # if slots:
    #     appointment = create_appointment(service_id, client_id, date, slots[0])
    #     print(f"Created appointment: {appointment}")

if __name__ == "__main__":
    main()