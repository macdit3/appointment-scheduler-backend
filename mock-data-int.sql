-- Inserting into businesses
INSERT INTO public.businesses (name, address, phone, email, website, timezone, cancellation_policy)
VALUES
    ('Harmony Wellness Spa', '123 Relaxation Ave, Suite 200, Portland, OR 97205', '(503) 555-7890', 'info@harmonywellness.com', 'www.harmonywellness.com', 'America/Los_Angeles', 'Cancellations must be made 24 hours in advance for a full refund. Less than 24 hours will result in a 50% charge.'),
    ('Urban Cuts Barbershop', '456 Main Street, Chicago, IL 60611', '(312) 555-4321', 'appointments@urbancuts.com', 'www.urbancuts.com', 'America/Chicago', 'Please provide at least 4 hours notice for cancellations. No-shows will be charged full price.'),
    ('Serene Dental Care', '789 Healthcare Blvd, Miami, FL 33130', '(305) 555-9876', 'reception@serenedental.com', 'www.serenedental.com', 'America/New_York', 'A 48-hour notice is required for cancellation. Late cancellations may incur a $50 fee.'),
    ('Blissful Yoga Studio', '101 Zen Way, Austin, TX 78701', '(512) 555-1234', 'namaste@blissfulyoga.com', 'www.blissfulyoga.com', 'America/Chicago', 'Classes can be cancelled up to 2 hours before start time through our app or website.'),
    ('Prestige Auto Detailing', '567 Vehicle Lane, Seattle, WA 98101', '(206) 555-8765', 'service@prestigeauto.com', 'www.prestigeauto.com', 'America/Los_Angeles', 'Please cancel 24 hours in advance. Rescheduling is available at no extra cost with sufficient notice.');

-- Inserting into business_hours
INSERT INTO public.business_hours (business_id, day_of_week, open_time, close_time, is_closed)
VALUES
    (1, 1, '09:00:00', '18:00:00', false), -- Harmony Wellness Monday
    (1, 0, '10:00:00', '16:00:00', false), -- Harmony Wellness Sunday
    (2, 1, '08:00:00', '20:00:00', false), -- Urban Cuts Monday
    (2, 6, '09:00:00', '17:00:00', false), -- Urban Cuts Saturday
    (3, 2, '08:30:00', '17:30:00', false); -- Serene Dental Tuesday

-- Inserting into service_categories
INSERT INTO public.service_categories (business_id, name, description)
VALUES
    (1, 'Massage Therapy', 'Relax and rejuvenate with our range of massage treatments designed to reduce stress and tension.'),
    (1, 'Facial Treatments', 'Revitalize your skin with our signature facial treatments using premium skincare products.'),
    (2, 'Haircuts', 'Professional haircuts for all styles and preferences.'),
    (3, 'Preventive Care', 'Regular check-ups and cleanings to maintain your dental health.'),
    (4, 'Group Classes', 'Join our community in instructor-led group yoga sessions for all experience levels.');

-- Inserting into services
INSERT INTO public.services (business_id, category_id, name, description, duration, buffer_time, max_clients, price, is_active)
VALUES
    (1, 1, 'Swedish Massage', '60-minute full body massage using gentle pressure and long strokes to promote relaxation.', 60, 15, 1, 85.00, true),
    (1, 2, 'Deep Cleansing Facial', 'A thorough facial treatment to cleanse pores and refresh skin.', 45, 10, 1, 65.00, true),
    (2, 3, 'Men''s Haircut & Style', 'Classic men''s haircut with styling.', 30, 5, 1, 35.00, true),
    (3, 4, 'Dental Cleaning', 'Professional dental cleaning and examination.', 45, 10, 1, 120.00, true),
    (4, 5, 'Vinyasa Flow Class', 'Energetic yoga class linking breath with movement.', 60, 15, 12, 18.00, true);

-- Inserting into staff
INSERT INTO public.staff (business_id, first_name, last_name, email, phone, position, is_active)
VALUES
    (1, 'Sarah', 'Johnson', 'sarah.j@harmonywellness.com', '(503) 555-7891', 'Lead Massage Therapist', true),
    (1, 'Michael', 'Chen', 'michael.c@harmonywellness.com', '(503) 555-7892', 'Esthetician', true),
    (2, 'James', 'Rodriguez', 'james.r@urbancuts.com', '(312) 555-4322', 'Senior Barber', true),
    (3, 'Lisa', 'Wong', 'dr.wong@serenedental.com', '(305) 555-9877', 'Dentist', true),
    (4, 'Emma', 'Garcia', 'emma.g@blissfulyoga.com', '(512) 555-1235', 'Yoga Instructor', true);

-- Inserting into clients
INSERT INTO public.clients (business_id, first_name, last_name, email, phone, date_of_birth, preferred_staff_id, notes)
VALUES
    (1, 'Robert', 'Smith', 'robert.smith@email.com', '(503) 555-1001', '1985-07-15', 1, 'Prefers firm pressure during massages.'),
    (1, 'Jennifer', 'Lopez', 'jlopez@email.com', '(503) 555-1002', '1979-03-22', 2, 'Sensitive skin, use hypoallergenic products only.'),
    (2, 'David', 'Wilson', 'dwilson@email.com', '(312) 555-2001', '1992-11-30', 3, 'Prefers classic tapered cut.'),
    (3, 'Maria', 'Gonzalez', 'mgonzalez@email.com', '(305) 555-3001', '1988-05-12', 4, 'Anxious about dental procedures, needs extra time.'),
    (4, 'Thomas', 'Brown', 'tbrown@email.com', '(512) 555-4001', '1990-09-05', 5, 'Intermediate yoga practitioner, has minor knee issues.');

-- Inserting into staff_services
INSERT INTO public.staff_services (staff_id, service_id)
VALUES
    (1, 1), -- Sarah can perform Swedish Massage
    (2, 2), -- Michael can perform Deep Cleansing Facial
    (3, 3), -- James can perform Men's Haircut & Style
    (4, 4), -- Lisa can perform Dental Cleaning
    (5, 5); -- Emma can teach Vinyasa Flow Class

-- Inserting into staff_schedules
INSERT INTO public.staff_schedules (staff_id, day_of_week, start_time, end_time, is_working)
VALUES
    (1, 1, '09:00:00', '17:00:00', true), -- Sarah works Monday 9am-5pm
    (1, 2, '09:00:00', '17:00:00', true), -- Sarah works Tuesday 9am-5pm
    (2, 1, '10:00:00', '18:00:00', true), -- Michael works Monday 10am-6pm
    (3, 1, '08:00:00', '16:00:00', true), -- James works Monday 8am-4pm
    (4, 2, '08:30:00', '17:30:00', true); -- Lisa works Tuesday 8:30am-5:30pm

-- Inserting into appointments
INSERT INTO public.appointments (business_id, client_id, service_id, staff_id, start_time, end_time, status, notes)
VALUES
    (1, 1, 1, 1, '2024-06-10 10:00:00-07', '2024-06-10 11:00:00-07', 'confirmed', 'Returning client, prefers quiet environment.'),
    (1, 2, 2, 2, '2024-06-10 14:00:00-07', '2024-06-10 14:45:00-07', 'scheduled', 'First-time facial treatment.'),
    (2, 3, 3, 3, '2024-06-10 09:30:00-06', '2024-06-10 10:00:00-06', 'completed', 'Regular monthly haircut.'),
    (3, 4, 4, 4, '2024-06-11 13:00:00-04', '2024-06-11 13:45:00-04', 'scheduled', 'Six-month check-up and cleaning.'),
    (4, 5, 5, 5, '2024-06-10 18:00:00-05', '2024-06-10 19:00:00-05', 'confirmed', 'Regular attendee.');

-- Inserting into appointment_reminders
INSERT INTO public.appointment_reminders (appointment_id, reminder_type, scheduled_time, sent_at, status)
VALUES
    (1, 'email', '2024-06-09 10:00:00-07', '2024-06-09 10:00:00-07', 'sent'),
    (1, 'sms', '2024-06-09 10:00:00-07', '2024-06-09 10:00:01-07', 'sent'),
    (2, 'email', '2024-06-09 14:00:00-07', NULL, 'pending'),
    (3, 'sms', '2024-06-09 18:00:00-06', '2024-06-09 18:00:03-06', 'sent'),
    (4, 'email', '2024-06-10 13:00:00-04', NULL, 'pending');

-- Inserting into special_business_hours
INSERT INTO public.special_business_hours (business_id, date, is_closed, open_time, close_time, description)
VALUES
    (1, '2024-07-04', true, NULL, NULL, 'Closed for Independence Day'),
    (2, '2024-07-04', true, NULL, NULL, 'Closed for Independence Day'),
    (1, '2024-12-24', false, '09:00:00', '14:00:00', 'Christmas Eve - Reduced Hours'),
    (3, '2024-06-15', false, '10:00:00', '16:00:00', 'Staff Training Day - Limited Hours'),
    (4, '2024-05-27', true, NULL, NULL, 'Closed for Memorial Day');

-- Inserting into payments
INSERT INTO public.payments (appointment_id, amount, payment_method, payment_status, transaction_id, payment_date)
VALUES
    (3, 35.00, 'credit_card', 'completed', 'txn_1234567890', '2024-06-10 10:05:00-06'),
    (1, 85.00, 'credit_card', 'pending', NULL, NULL),
    (2, 65.00, 'gift_card', 'pending', NULL, NULL),
    (4, 120.00, 'insurance', 'pending', NULL, NULL),
    (5, 18.00, 'venmo', 'completed', 'venmo_1234567890', '2024-06-09 20:30:15-05');

-- Inserting into client_notes
INSERT INTO public.client_notes (client_id, staff_id, note_text)
VALUES
    (1, 1, 'Robert responded well to deep tissue techniques on lower back. Recommended stretching exercises for home care.'),
    (2, 2, 'Jennifer mentioned new sensitivity to lavender. Updated her profile to avoid lavender-based products.'),
    (3, 3, 'David is growing out his hair for a new style. Discussed maintenance tips for the transition period.'),
    (4, 4, 'Maria needs additional time for numbing to take effect. Very concerned about pain management.'),
    (5, 5, 'Thomas is progressing well in his practice. Suggested he try the intermediate flow class on Thursdays.');