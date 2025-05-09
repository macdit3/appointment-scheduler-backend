## 1. Tables and Fields

### businesses
```sql
CREATE TABLE businesses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    website VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_businesses_name ON businesses(name);
```

### business_hours
```sql
CREATE TABLE business_hours (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    business_id UUID NOT NULL REFERENCES businesses(id) ON DELETE CASCADE,
    day_of_week SMALLINT NOT NULL CHECK (day_of_week BETWEEN 0 AND 6), -- 0 = Sunday, 6 = Saturday
    open_time TIME NOT NULL,
    close_time TIME NOT NULL,
    is_closed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE (business_id, day_of_week)
);

CREATE INDEX idx_business_hours_business_id ON business_hours(business_id);
```

### service_categories
```sql
CREATE TABLE service_categories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    business_id UUID NOT NULL REFERENCES businesses(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE (business_id, name)
);

CREATE INDEX idx_service_categories_business_id ON service_categories(business_id);
```

### services
```sql
CREATE TABLE services (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    business_id UUID NOT NULL REFERENCES businesses(id) ON DELETE CASCADE,
    category_id UUID REFERENCES service_categories(id) ON DELETE SET NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration INTEGER NOT NULL, -- in minutes
    price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE (business_id, name)
);

CREATE INDEX idx_services_business_id ON services(business_id);
CREATE INDEX idx_services_category_id ON services(category_id);
```

### clients
```sql
CREATE TABLE clients (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    business_id UUID NOT NULL REFERENCES businesses(id) ON DELETE CASCADE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_clients_business_id ON clients(business_id);
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_clients_name ON clients(last_name, first_name);
```

### staff
```sql
CREATE TABLE staff (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    business_id UUID NOT NULL REFERENCES businesses(id) ON DELETE CASCADE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    position VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_staff_business_id ON staff(business_id);
```

### staff_services
```sql
CREATE TABLE staff_services (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    staff_id UUID NOT NULL REFERENCES staff(id) ON DELETE CASCADE,
    service_id UUID NOT NULL REFERENCES services(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE (staff_id, service_id)
);

CREATE INDEX idx_staff_services_staff_id ON staff_services(staff_id);
CREATE INDEX idx_staff_services_service_id ON staff_services(service_id);
```

### staff_schedules
```sql
CREATE TABLE staff_schedules (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    staff_id UUID NOT NULL REFERENCES staff(id) ON DELETE CASCADE,
    day_of_week SMALLINT NOT NULL CHECK (day_of_week BETWEEN 0 AND 6),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    is_working BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE (staff_id, day_of_week)
);

CREATE INDEX idx_staff_schedules_staff_id ON staff_schedules(staff_id);
```

### appointments
```sql
CREATE TABLE appointments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    business_id UUID NOT NULL REFERENCES businesses(id) ON DELETE CASCADE,
    client_id UUID NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    service_id UUID NOT NULL REFERENCES services(id) ON DELETE RESTRICT,
    staff_id UUID REFERENCES staff(id) ON DELETE SET NULL,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'scheduled' 
        CHECK (status IN ('scheduled', 'confirmed', 'completed', 'cancelled', 'no-show')),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_appointments_business_id ON appointments(business_id);
CREATE INDEX idx_appointments_client_id ON appointments(client_id);
CREATE INDEX idx_appointments_service_id ON appointments(service_id);
CREATE INDEX idx_appointments_staff_id ON appointments(staff_id);
CREATE INDEX idx_appointments_start_time ON appointments(start_time);
CREATE INDEX idx_appointments_status ON appointments(status);
```

### appointment_reminders
```sql
CREATE TABLE appointment_reminders (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    appointment_id UUID NOT NULL REFERENCES appointments(id) ON DELETE CASCADE,
    reminder_type VARCHAR(20) NOT NULL CHECK (reminder_type IN ('email', 'sms')),
    scheduled_time TIMESTAMP WITH TIME ZONE NOT NULL,
    sent_at TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) NOT NULL DEFAULT 'pending' 
        CHECK (status IN ('pending', 'sent', 'failed')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_appointment_reminders_appointment_id ON appointment_reminders(appointment_id);
CREATE INDEX idx_appointment_reminders_scheduled_time ON appointment_reminders(scheduled_time);

-- Special Business Hours 
CREATE TABLE special_business_hours (
                                       id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                                       business_id UUID NOT NULL REFERENCES businesses(id) ON DELETE CASCADE,
                                       date DATE NOT NULL,
                                       is_closed BOOLEAN DEFAULT FALSE,
                                       open_time TIME,
                                       close_time TIME,
                                       description VARCHAR(255),
                                       created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                                       updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                                       UNIQUE (business_id, date)
);


--Payment Information 
CREATE TABLE payments (
                         id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                         appointment_id UUID NOT NULL REFERENCES appointments(id) ON DELETE CASCADE,
                         amount DECIMAL(10, 2) NOT NULL,
                         payment_method VARCHAR(50) NOT NULL,
                         payment_status VARCHAR(20) NOT NULL DEFAULT 'pending',
                         transaction_id VARCHAR(100),
                         payment_date TIMESTAMP WITH TIME ZONE,
                         created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                         updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);


-- Client Notes or History
CREATE TABLE client_notes (
                             id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                             client_id UUID NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
                             staff_id UUID REFERENCES staff(id) ON DELETE SET NULL,
                             note_text TEXT NOT NULL,
                             created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

```