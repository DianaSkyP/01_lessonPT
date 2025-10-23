import pytest
from models import DatabaseManager, get_db_connection_string, Employee


@pytest.fixture(scope="session")
def db_manager():
    connection_string = get_db_connection_string()
    manager = DatabaseManager(connection_string)

    yield manager


@pytest.fixture
def db_session(db_manager):
    session = db_manager.get_session()

    yield session

    session.query(Employee).filter(
        Employee.email.like('%test_automation%')
    ).delete(synchronize_session=False)
    session.commit()
    session.close()


@pytest.fixture
def sample_employee_data():
    return {
        "first_name": "Иван",
        "last_name": "Иванов",
        "middle_name": "Иванович",
        "phone": "+79001234567",
        "email": "ivan.ivanov@test_automation.com",
        "company_id": 1
    }
