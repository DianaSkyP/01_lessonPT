from models import Employee
from datetime import datetime


def test_create_employee(db_session, sample_employee_data):

    new_employee = Employee(
        first_name=sample_employee_data["first_name"],
        last_name=sample_employee_data["last_name"],
        middle_name=sample_employee_data["middle_name"],
        phone=sample_employee_data["phone"],
        email=sample_employee_data["email"],
        company_id=sample_employee_data["company_id"]
    )

    db_session.add(new_employee)
    db_session.commit()

    assert new_employee.id is not None
    assert new_employee.first_name == sample_employee_data["first_name"]
    assert new_employee.last_name == sample_employee_data["last_name"]
    assert new_employee.email == sample_employee_data["email"]
    assert new_employee.is_active is True
    assert isinstance(new_employee.create_timestamp, datetime)

    employee_from_db = db_session.query(Employee).filter_by(
        email=sample_employee_data["email"]
    ).first()
    assert employee_from_db is not None
    assert employee_from_db.first_name == sample_employee_data["first_name"]


def test_update_employee(db_session, sample_employee_data):
    employee = Employee(
        first_name=sample_employee_data["first_name"],
        last_name=sample_employee_data["last_name"],
        middle_name=sample_employee_data["middle_name"],
        phone=sample_employee_data["phone"],
        email=sample_employee_data["email"],
        company_id=sample_employee_data["company_id"]
    )
    db_session.add(employee)
    db_session.commit()

    original_create_timestamp = employee.create_timestamp
    employee_id = employee.id

    new_first_name = "Петр"
    new_phone = "+79007654321"
    employee.first_name = new_first_name
    employee.phone = new_phone
    db_session.commit()

    updated_employee = db_session.query(Employee).filter_by(
        id=employee_id
    ).first()
    assert updated_employee.first_name == new_first_name
    assert updated_employee.phone == new_phone
    assert updated_employee.last_name == sample_employee_data["last_name"]
    assert updated_employee.create_timestamp == original_create_timestamp
    assert updated_employee.change_timestamp >= original_create_timestamp


def test_delete_employee(db_session, sample_employee_data):
    employee = Employee(
        first_name=sample_employee_data["first_name"],
        last_name=sample_employee_data["last_name"],
        middle_name=sample_employee_data["middle_name"],
        phone=sample_employee_data["phone"],
        email=sample_employee_data["email"],
        company_id=sample_employee_data["company_id"]
    )
    db_session.add(employee)
    db_session.commit()

    employee_id = employee.id

    employee_from_db = db_session.query(Employee).filter_by(
        id=employee_id
    ).first()
    assert employee_from_db is not None

    db_session.delete(employee)
    db_session.commit()

    deleted_employee = db_session.query(Employee).filter_by(
        id=employee_id
    ).first()
    assert deleted_employee is None


def test_soft_delete_employee(db_session, sample_employee_data):
    employee = Employee(
        first_name=sample_employee_data["first_name"],
        last_name=sample_employee_data["last_name"],
        middle_name=sample_employee_data["middle_name"],
        phone=sample_employee_data["phone"],
        email=sample_employee_data["email"],
        company_id=sample_employee_data["company_id"]
    )
    db_session.add(employee)
    db_session.commit()

    employee_id = employee.id

    employee.soft_delete()
    db_session.commit()

    soft_deleted_employee = db_session.query(Employee).filter_by(
        id=employee_id
    ).first()
    assert soft_deleted_employee is not None
    assert soft_deleted_employee.is_active is False
    assert soft_deleted_employee.change_timestamp is not None
