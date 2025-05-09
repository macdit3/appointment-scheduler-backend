Based on the DDL below generate real-to-life mock data.
I want real-to-life small-medium databset.

"""
create table public.businesses
(
    id                  integer generated always as identity
        primary key,
    name                varchar(100) not null,
    address             text,
    phone               varchar(20),
    email               varchar(100),
    website             varchar(255),
    timezone            varchar(50)              default 'UTC'::character varying,
    cancellation_policy text,
    created_at          timestamp with time zone default now(),
    updated_at          timestamp with time zone default now()
);

create table public.business_hours
(
    id          integer generated always as identity
        primary key,
    business_id integer  not null
        references public.businesses
            on delete cascade,
    day_of_week smallint not null
        constraint business_hours_day_of_week_check
            check ((day_of_week >= 0) AND (day_of_week <= 6)),
    open_time   time     not null,
    close_time  time     not null,
    is_closed   boolean                  default false,
    created_at  timestamp with time zone default now(),
    updated_at  timestamp with time zone default now(),
    unique (business_id, day_of_week),
    constraint business_hours_time_check
        check ((is_closed = true) OR ((is_closed = false) AND (close_time > open_time)))
);


create table public.service_categories
(
    id          integer generated always as identity
        primary key,
    business_id integer      not null
        references public.businesses
            on delete cascade,
    name        varchar(100) not null,
    description text,
    created_at  timestamp with time zone default now(),
    updated_at  timestamp with time zone default now(),
    unique (business_id, name)
);

create table public.services
(
    id          integer generated always as identity
        primary key,
    business_id integer        not null
        references public.businesses
            on delete cascade,
    category_id integer
                               references public.service_categories
                                   on delete set null,
    name        varchar(100)   not null,
    description text,
    duration    integer        not null
        constraint services_duration_check
            check (duration > 0),
    buffer_time integer                  default 0
        constraint services_buffer_time_check
            check (buffer_time >= 0),
    max_clients integer                  default 1
        constraint services_max_clients_check
            check (max_clients >= 1),
    price       numeric(10, 2) not null,
    is_active   boolean                  default true,
    created_at  timestamp with time zone default now(),
    updated_at  timestamp with time zone default now(),
    unique (business_id, name)
);

create table public.staff
(
    id          integer generated always as identity
        primary key,
    business_id integer     not null
        references public.businesses
            on delete cascade,
    first_name  varchar(50) not null,
    last_name   varchar(50) not null,
    email       varchar(100),
    phone       varchar(20),
    position    varchar(100),
    is_active   boolean                  default true,
    created_at  timestamp with time zone default now(),
    updated_at  timestamp with time zone default now()
);


create table public.clients
(
    id                 integer generated always as identity
        primary key,
    business_id        integer     not null
        references public.businesses
            on delete cascade,
    first_name         varchar(50) not null,
    last_name          varchar(50) not null,
    email              varchar(100),
    phone              varchar(20),
    date_of_birth      date,
    preferred_staff_id integer
                                   references public.staff
                                       on delete set null,
    notes              text,
    created_at         timestamp with time zone default now(),
    updated_at         timestamp with time zone default now()
);


create table public.staff_services
(
    id         integer generated always as identity
        primary key,
    staff_id   integer not null
        references public.staff
            on delete cascade,
    service_id integer not null
        references public.services
            on delete cascade,
    created_at timestamp with time zone default now(),
    unique (staff_id, service_id)
);

create table public.staff_schedules
(
    id          integer generated always as identity
        primary key,
    staff_id    integer  not null
        references public.staff
            on delete cascade,
    day_of_week smallint not null
        constraint staff_schedules_day_of_week_check
            check ((day_of_week >= 0) AND (day_of_week <= 6)),
    start_time  time     not null,
    end_time    time     not null,
    is_working  boolean                  default true,
    created_at  timestamp with time zone default now(),
    updated_at  timestamp with time zone default now(),
    unique (staff_id, day_of_week),
    constraint staff_schedules_time_check
        check (end_time > start_time)
);


create table public.appointments
(
    id          integer generated always as identity
        primary key,
    business_id integer                                                         not null
        references public.businesses
            on delete cascade,
    client_id   integer                                                         not null
        references public.clients
            on delete cascade,
    service_id  integer                                                         not null
        references public.services
            on delete restrict,
    staff_id    integer
                                                                                references public.staff
                                                                                    on delete set null,
    start_time  timestamp with time zone                                        not null,
    end_time    timestamp with time zone                                        not null,
    status      varchar(20)              default 'scheduled'::character varying not null
        constraint appointments_status_check
            check ((status)::text = ANY
                   ((ARRAY ['scheduled'::character varying, 'confirmed'::character varying, 'completed'::character varying, 'cancelled'::character varying, 'no-show'::character varying])::text[])),
    notes       text,
    created_at  timestamp with time zone default now(),
    updated_at  timestamp with time zone default now(),
    constraint appointments_time_check
        check (end_time > start_time)
);


create table public.appointment_reminders
(
    id             integer generated always as identity
        primary key,
    appointment_id integer                                                       not null
        references public.appointments
            on delete cascade,
    reminder_type  varchar(20)                                                   not null
        constraint appointment_reminders_reminder_type_check
            check ((reminder_type)::text = ANY
                   ((ARRAY ['email'::character varying, 'sms'::character varying])::text[])),
    scheduled_time timestamp with time zone                                      not null,
    sent_at        timestamp with time zone,
    status         varchar(20)              default 'pending'::character varying not null
        constraint appointment_reminders_status_check
            check ((status)::text = ANY
                   ((ARRAY ['pending'::character varying, 'sent'::character varying, 'failed'::character varying])::text[])),
    created_at     timestamp with time zone default now(),
    updated_at     timestamp with time zone default now()
);


create table public.special_business_hours
(
    id          integer generated always as identity
        primary key,
    business_id integer not null
        references public.businesses
            on delete cascade,
    date        date    not null,
    is_closed   boolean                  default false,
    open_time   time,
    close_time  time,
    description varchar(255),
    created_at  timestamp with time zone default now(),
    updated_at  timestamp with time zone default now(),
    unique (business_id, date),
    constraint check_hours_consistency
        check (((is_closed = true) AND (open_time IS NULL) AND (close_time IS NULL)) OR
               ((is_closed = false) AND (open_time IS NOT NULL) AND (close_time IS NOT NULL) AND
                (close_time > open_time)))
);

create table public.payments
(
    id             integer generated always as identity
        primary key,
    appointment_id integer                                                       not null
        references public.appointments
            on delete cascade,
    amount         numeric(10, 2)                                                not null,
    payment_method varchar(50)                                                   not null,
    payment_status varchar(20)              default 'pending'::character varying not null
        constraint payments_status_check
            check ((payment_status)::text = ANY
                   ((ARRAY ['pending'::character varying, 'completed'::character varying, 'failed'::character varying, 'refunded'::character varying, 'partially_refunded'::character varying])::text[])),
    transaction_id varchar(100),
    payment_date   timestamp with time zone,
    created_at     timestamp with time zone default now(),
    updated_at     timestamp with time zone default now()
);

create table public.client_notes
(
    id         integer generated always as identity
        primary key,
    client_id  integer not null
        references public.clients
            on delete cascade,
    staff_id   integer
                       references public.staff
                           on delete set null,
    note_text  text    not null,
    created_at timestamp with time zone default now()
);

"""

Do not write in a notebook, write in raw SQL.