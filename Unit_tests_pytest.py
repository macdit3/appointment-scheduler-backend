import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from datetime import datetime, date, timedelta

from main import app

client = TestClient(app)

# Mock response objects
class MockResponse:
    def __init__(self, data):
        self.data = data

# Root endpoint test
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Appointment Scheduler API"}

# Business endpoint tests
@patch("main.supabase")
def test_get_businesses(mock_supabase):
    # Mock data
    mock_businesses = [
        {"id": 1, "name": "Business 1", "email": "business1@example.com"},
        {"id": 2, "name": "Business 2", "email": "business2@example.com"}
    ]

    # Setup the mock
    mock_select = MagicMock()
    mock_execute = MagicMock(return_value=MockResponse(mock_businesses))
    mock_select.select.return_value = mock_select
    mock_select.execute.return_value = mock_execute.return_value
    mock_supabase.table.return_value = mock_select

    # Make the request
    response = client.get("/businesses/")

    # Check the response
    assert response.status_code == 200
    assert response.json() == mock_businesses

    # Check that the correct table was queried
    mock_supabase.table.assert_called_with("businesses")

@patch("main.supabase")
def test_get_business(mock_supabase):
    # Mock data
    mock_business = {"id": 1, "name": "Business 1", "email": "business1@example.com"}

    # Setup the mock
    mock_select = MagicMock()
    mock_eq = MagicMock()
    mock_execute = MagicMock(return_value=MockResponse([mock_business]))

    mock_select.select.return_value = mock_select
    mock_select.eq.return_value = mock_eq
    mock_eq.execute.return_value = mock_execute.return_value
    mock_supabase.table.return_value = mock_select

    # Make the request
    response = client.get("/businesses/1")

    # Check the response
    assert response.status_code == 200
    assert response.json() == mock_business

    # Check that the correct table and ID was queried
    mock_supabase.table.assert_called_with("businesses")
    mock_select.eq.assert_called_with("id", 1)

@patch("main.supabase")
def test_get_business_not_found(mock_supabase):
    # Setup the mock for not found
    mock_select = MagicMock()
    mock_eq = MagicMock()
    mock_execute = MagicMock(return_value=MockResponse([]))

    mock_select.select.return_value = mock_select
    mock_select.eq.return_value = mock_eq
    mock_eq.execute.return_value = mock_execute.return_value
    mock_supabase.table.return_value = mock_select

    # Make the request
    response = client.get("/businesses/999")

    # Check the response
    assert response.status_code == 404
    assert response.json() == {"detail": "Business not found"}

@patch("main.supabase")
def test_create_business(mock_supabase):
    # Mock data
    mock_business_data = {"name": "New Business", "email": "new@example.com", "phone": "1234567890"}
    mock_business_response = {"id": 3, "name": "New Business", "email": "new@example.com", "phone": "1234567890"}

    # Setup the mock
    mock_insert = MagicMock()
    mock_execute = MagicMock(return_value=MockResponse([mock_business_response]))

    mock_insert.execute.return_value = mock_execute.return_value
    mock_supabase.table.return_value.insert.return_value = mock_insert

    # Make the request
    response = client.post("/businesses/", json=mock_business_data)

    # Check the response
    assert response.status_code == 200
    assert response.json() == mock_business_response

    # Check that the correct table was used and data was inserted
    mock_supabase.table.assert_called_with("businesses")
    mock_supabase.table.return_value.insert.assert_called_once()

@patch("main.supabase")
def test_update_business(mock_supabase):
    # Mock data
    mock_update_data = {"name": "Updated Business"}
    mock_updated_business = {"id": 1, "name": "Updated Business", "email": "business1@example.com"}

    # Setup the mock
    mock_update = MagicMock()
    mock_eq = MagicMock()
    mock_execute = MagicMock(return_value=MockResponse([mock_updated_business]))

    mock_update.eq.return_value = mock_eq
    mock_eq.execute.return_value = mock_execute.return_value
    mock_supabase.table.return_value.update.return_value = mock_update

    # Make the request
    response = client.put("/businesses/1", json=mock_update_data)

    # Check the response
    assert response.status_code == 200
    assert response.json() == mock_updated_business

    # Check that the correct table was used and data was updated
    mock_supabase.table.assert_called_with("businesses")
    mock_supabase.table.return_value.update.assert_called_once()
    mock_update.eq.assert_called_with("id", 1)

@patch("main.supabase")
def test_delete_business(mock_supabase):
    # Mock data
    mock_deleted_business = {"id": 1, "name": "Business 1", "email": "business1@example.com"}

    # Setup the mock
    mock_delete = MagicMock()
    mock_eq = MagicMock()
    mock_execute = MagicMock(return_value=MockResponse([mock_deleted_business]))

    mock_delete.eq.return_value = mock_eq
    mock_eq.execute.return_value = mock_execute.return_value
    mock_supabase.table.return_value.delete.return_value = mock_delete

    # Make the request
    response = client.delete("/businesses/1")

    # Check the response
    assert response.status_code == 200
    assert response.json() == {"message": "Business deleted successfully"}

    # Check that the correct table was used and delete was called
    mock_supabase.table.assert_called_with("businesses")
    mock_supabase.table.return_value.delete.assert_called_once()
    mock_delete.eq.assert_called_with("id", 1)

# Business hours endpoint tests
@patch("main.supabase")
def test_get_all_business_hours(mock_supabase):
    # Mock data
    mock_hours = [
        {"id": 1, "business_id": 1, "day_of_week": 1, "open_time": "09:00", "close_time": "17:00"},
        {"id": 2, "business_id": 1, "day_of_week": 2, "open_time": "09:00", "close_time": "17:00"}
    ]

    # Setup the mock
    mock_select = MagicMock()
    mock_execute = MagicMock(return_value=MockResponse(mock_hours))

    mock_select.select.return_value = mock_select
    mock_select.execute.return_value = mock_execute.return_value
    mock_supabase.table.return_value = mock_select

    # Make the request
    response = client.get("/business-hours/")

    # Check the response
    assert response.status_code == 200
    assert response.json() == mock_hours

    # Check that the correct table was queried
    mock_supabase.table.assert_called_with("business_hours")

# Service category endpoint tests
@patch("main.supabase")
def test_get_service_categories(mock_supabase):
    # Mock data
    mock_categories = [
        {"id": 1, "business_id": 1, "name": "Category 1"},
        {"id": 2, "business_id": 1, "name": "Category 2"}
    ]

    # Setup the mock
    mock_select = MagicMock()
    mock_execute = MagicMock(return_value=MockResponse(mock_categories))

    mock_select.select.return_value = mock_select
    mock_select.execute.return_value = mock_execute.return_value
    mock_supabase.table.return_value = mock_select

    # Make the request
    response = client.get("/service-categories/")

    # Check the response
    assert response.status_code == 200
    assert response.json() == mock_categories

    # Check that the correct table was queried
    mock_supabase.table.assert_called_with("service_categories")

# Service endpoint tests
@patch("main.supabase")
def test_get_services(mock_supabase):
    # Mock data
    mock_services = [
        {"id": 1, "business_id": 1, "category_id": 1, "name": "Service 1", "duration": 60, "price": 100.00},
        {"id": 2, "business_id": 1, "category_id": 1, "name": "Service 2", "duration": 30, "price": 50.00}
    ]

    # Setup the mock
    mock_select = MagicMock()
    mock_execute = MagicMock(return_value=MockResponse(mock_services))

    mock_select.select.return_value = mock_select
    mock_select.execute.return_value = mock_execute.return_value
    mock_supabase.table.return_value = mock_select

    # Make the request
    response = client.get("/services/")

    # Check the response
    assert response.status_code == 200
    assert response.json() == mock_services

    # Check that the correct table was queried
    mock_supabase.table.assert_called_with("services")

# Staff endpoint tests
@patch("main.supabase")
def test_get_staff_members(mock_supabase):
    # Mock data
    mock_staff = [
        {"id": 1, "business_id": 1, "name": "Staff 1", "email": "staff1@example.com"},
        {"id": 2, "business_id": 1, "name": "Staff 2", "email": "staff2@example.com"}
    ]

    # Setup the mock
    mock_select = MagicMock()
    mock_execute = MagicMock(return_value=MockResponse(mock_staff))

    mock_select.select.return_value = mock_select
    mock_select.execute.return_value = mock_execute.return_value
    mock_supabase.table.return_value = mock_select

    # Make the request
    response = client.get("/staff/")

    # Check the response
    assert response.status_code == 200
    assert response.json() == mock_staff

    # Check that the correct table was queried
    mock_supabase.table.assert_called_with("staff")

# Client endpoint tests
@patch("main.supabase")
def test_get_clients(mock_supabase):
    # Mock data
    mock_clients = [
        {"id": 1, "business_id": 1, "name": "Client 1", "email": "client1@example.com", "phone": "1234567890"},
        {"id": 2, "business_id": 1, "name": "Client 2", "email": "client2@example.com", "phone": "0987654321"}
    ]

    # Setup the mock
    mock_select = MagicMock()
    mock_execute = MagicMock(return_value=MockResponse(mock_clients))

    mock_select.select.return_value = mock_select
    mock_select.execute.return_value = mock_execute.return_value
    mock_supabase.table.return_value = mock_select

    # Make the request
    response = client.get("/clients/")

    # Check the response
    assert response.status_code == 200
    assert response.json() == mock_clients

    # Check that the correct table was queried
    mock_supabase.table.assert_called_with("clients")