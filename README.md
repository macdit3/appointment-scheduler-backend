# Appointment Scheduler Backend

A FastAPI backend for a small business appointment scheduling system using Supabase (PostgreSQL) as the database.

## Features

- Complete database schema for appointment scheduling
- RESTful API for managing businesses, services, clients, and appointments
- Integration with Supabase for PostgreSQL database and authentication
- Comprehensive data validation and error handling

## Database Schema

The database is designed with the following tables:

- **businesses**: Store business information (name, address, contact info)
- **business_hours**: Business operating hours for each day of the week
- **service_categories**: Categories for organizing services
- **services**: Services offered by the business (name, duration, price, description)
- **clients**: Client information (name, contact info, notes)
- **staff**: Staff members who provide services
- **staff_services**: Junction table for staff-service relationships
- **staff_schedules**: Staff working hours
- **appointments**: Appointment bookings (date, time, service, client, status)
- **appointment_reminders**: Reminders for upcoming appointments

For the complete schema, see [database-design.md](database-design.md) and [schema.sql](schema.sql).

## Setup

### Prerequisites

- Python 3.12 or higher
- Supabase account

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/appointment-scheduler-backend.git
   cd appointment-scheduler-backend
   ```

2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```
   export SUPABASE_URL=your_supabase_url
   export SUPABASE_KEY=your_supabase_key
   ```
   On Windows:
   ```
   set SUPABASE_URL=your_supabase_url
   set SUPABASE_KEY=your_supabase_key
   ```

4. Set up the database:
   - Create a new Supabase project
   - Execute the SQL in `schema.sql` in the Supabase SQL Editor

5. Run the application:
   ```
   # Using the run.py script (recommended)
   python run.py

   # Or directly with uvicorn
   uvicorn main:app --reload
   ```

6. Access the API documentation at http://localhost:8000/docs

## API Endpoints

### Root
- `GET /`: Welcome message to the API

### Businesses
- `GET /businesses/`: List all businesses
- `GET /businesses/{business_id}`: Get business details
- `POST /businesses/`: Create a new business
- `PUT /businesses/{business_id}`: Update a business
- `DELETE /businesses/{business_id}`: Delete a business

### Business Hours
- `GET /business-hours/`: List all business hours (can filter by business_id)
- `GET /business-hours/{hours_id}`: Get specific business hours
- `POST /business-hours/`: Create new business hours
- `PUT /business-hours/{hours_id}`: Update business hours
- `DELETE /business-hours/{hours_id}`: Delete business hours

### Service Categories
- `GET /service-categories/`: List all service categories (can filter by business_id)
- `GET /service-categories/{category_id}`: Get specific service category
- `POST /service-categories/`: Create a new service category
- `PUT /service-categories/{category_id}`: Update a service category
- `DELETE /service-categories/{category_id}`: Delete a service category

### Services
- `GET /services/`: List all services (can filter by business_id and category_id)
- `GET /services/{service_id}`: Get specific service details
- `POST /services/`: Create a new service
- `PUT /services/{service_id}`: Update a service
- `DELETE /services/{service_id}`: Delete a service

### Staff
- `GET /staff/`: List all staff members (can filter by business_id)
- `GET /staff/{staff_id}`: Get specific staff member details
- `POST /staff/`: Create a new staff member
- `PUT /staff/{staff_id}`: Update a staff member
- `DELETE /staff/{staff_id}`: Delete a staff member

### Clients
- `GET /clients/`: List all clients (can filter by business_id)
- `GET /clients/{client_id}`: Get specific client details
- `POST /clients/`: Create a new client
- `PUT /clients/{client_id}`: Update a client
- `DELETE /clients/{client_id}`: Delete a client

### Staff Services
- `GET /staff-services/`: List all staff-service assignments (can filter by staff_id and service_id)
- `POST /staff-services/`: Assign a service to a staff member
- `DELETE /staff-services/`: Remove a service from a staff member

### Staff Schedules
- `GET /staff-schedules/`: List all staff schedules (can filter by staff_id and day_of_week)
- `GET /staff-schedules/{schedule_id}`: Get specific staff schedule
- `POST /staff-schedules/`: Create a new staff schedule
- `PUT /staff-schedules/{schedule_id}`: Update a staff schedule
- `DELETE /staff-schedules/{schedule_id}`: Delete a staff schedule

### Appointments
- `GET /appointments/`: List all appointments (can filter by business_id, client_id, staff_id, status, start_date, end_date)
- `GET /appointments/{appointment_id}`: Get specific appointment details
- `POST /appointments/`: Create a new appointment
- `PUT /appointments/{appointment_id}`: Update an appointment
- `DELETE /appointments/{appointment_id}`: Delete an appointment

### Appointment Reminders
- `GET /appointment-reminders/`: List all appointment reminders (can filter by appointment_id and status)
- `GET /appointment-reminders/{reminder_id}`: Get specific appointment reminder
- `POST /appointment-reminders/`: Create a new appointment reminder
- `PUT /appointment-reminders/{reminder_id}`: Update an appointment reminder
- `DELETE /appointment-reminders/{reminder_id}`: Delete an appointment reminder

### Special Business Hours
- `GET /special-business-hours/`: List all special business hours (can filter by business_id, date_from, date_to)
- `GET /special-business-hours/{hours_id}`: Get specific special business hours
- `POST /special-business-hours/`: Create new special business hours
- `PUT /special-business-hours/{hours_id}`: Update special business hours
- `DELETE /special-business-hours/{hours_id}`: Delete special business hours

### Payments
- `GET /payments/`: List all payments (can filter by appointment_id and payment_status)
- `GET /payments/{payment_id}`: Get specific payment details
- `POST /payments/`: Create a new payment
- `PUT /payments/{payment_id}`: Update a payment
- `DELETE /payments/{payment_id}`: Delete a payment

### Client Notes
- `GET /client-notes/`: List all client notes (can filter by client_id and staff_id)
- `GET /client-notes/{note_id}`: Get specific client note
- `POST /client-notes/`: Create a new client note
- `DELETE /client-notes/{note_id}`: Delete a client note

## Authentication

The application uses Supabase authentication. In a production environment, you would:

1. Implement proper JWT token validation
2. Use Row Level Security (RLS) in Supabase to restrict data access
3. Extract the business_id from the authenticated user's JWT token

## Future Enhancements

- Staff management endpoints
- Business hours management
- Service category management
- Advanced appointment filtering and searching
- Payment processing integration
- Email and SMS notifications

## License

[MIT](LICENSE)
