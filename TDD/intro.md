# Test-Driven Development (TDD) in Python: A Comprehensive Guide

## Table of Contents
1. [Introduction to TDD](#introduction)
2. [The TDD Cycle](#tdd-cycle)
3. [Python Testing Frameworks](#frameworks)
4. [Writing Effective Tests](#writing-tests)
5. [Test Types](#test-types)
6. [Best Practices](#best-practices)
7. [Common Patterns](#patterns)
8. [Advanced Topics](#advanced)

## 1. Introduction to TDD <a name="introduction"></a>

Test-Driven Development is a software development methodology where you write tests before writing the actual code. The main benefits of TDD include:
- Improved code quality
- Better code design
- Built-in documentation
- Confidence in code changes
- Faster debugging

## 2. The TDD Cycle <a name="tdd-cycle"></a>

The TDD cycle, often called "Red-Green-Refactor," consists of:

1. **Red**: Write a failing test
2. **Green**: Write the minimum code to make the test pass
3. **Refactor**: Improve the code while keeping tests passing

Example:
```python
# 1. Red - Write a failing test
def test_add():
    assert add(2, 3) == 5  # This fails because 'add' doesn't exist

# 2. Green - Write minimal code to pass
def add(a, b):
    return a + b

# 3. Refactor (if needed)
# In this simple case, no refactoring is necessary
```

## 3. Python Testing Frameworks <a name="frameworks"></a>

### unittest
Python's built-in testing framework:
```python
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```

### pytest
A more modern and powerful testing framework:
```python
def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0
```

Key differences:
- pytest uses plain assert statements
- More concise syntax
- Powerful fixtures and parameterization

## 4. Writing Effective Tests <a name="writing-tests"></a>

### Test Structure: AAA Pattern
- **Arrange**: Set up the test conditions
- **Act**: Perform the action being tested
- **Assert**: Verify the results

```python
def test_user_creation():
    # Arrange
    username = "testuser"
    email = "test@example.com"
    
    # Act
    user = User(username, email)
    
    # Assert
    assert user.username == username
    assert user.email == email
```

### Naming Conventions
- Test files should start with `test_`
- Test functions should start with `test_`
- Names should be descriptive: `test_user_creation_with_valid_email`

## 5. Test Types <a name="test-types"></a>

1. **Unit Tests**
   - Test individual components in isolation
   ```python
   def test_calculate_tax():
       assert calculate_tax(100) == 10
   ```

2. **Integration Tests**
   - Test multiple components together
   ```python
   def test_order_processing():
       order = create_order(items=["book", "pen"])
       process_payment(order)
       assert order.status == "paid"
   ```

3. **Functional Tests**
   - Test complete features
   ```python
   def test_user_registration_flow():
       user = register_new_user("test@example.com", "password123")
       assert user.is_registered
       assert send_welcome_email(user)
   ```

## 6. Best Practices <a name="best-practices"></a>

1. **Test One Thing per Test**
```python
# Good
def test_user_creation_success():
    user = User("test", "test@example.com")
    assert user.is_valid()

def test_user_creation_invalid_email():
    user = User("test", "invalid_email")
    assert not user.is_valid()

# Bad
def test_user_creation():
    user1 = User("test", "test@example.com")
    assert user1.is_valid()
    
    user2 = User("test", "invalid_email")
    assert not user2.is_valid()
```

2. **Use Descriptive Test Names**
```python
# Good
def test_order_total_with_multiple_items():
    pass

# Bad
def test_order():
    pass
```

3. **Don't Test Implementation Details**
```python
# Good
def test_user_registration():
    user = register_user("test@example.com", "password123")
    assert user.is_registered

# Bad
def test_user_registration_implementation():
    user = register_user("test@example.com", "password123")
    assert user._password_hash.startswith("$2b$")
```

## 7. Common Patterns <a name="patterns"></a>

### Fixtures (pytest)
```python
import pytest

@pytest.fixture
def sample_user():
    return User("testuser", "test@example.com")

def test_user_email(sample_user):
    assert sample_user.email == "test@example.com"
```

### Parameterized Tests
```python
@pytest.mark.parametrize("input,expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True)
])
def test_is_prime(input, expected):
    assert is_prime(input) == expected
```

### Mocking
```python
from unittest.mock import Mock, patch

def test_user_notification():
    with patch('myapp.email.send_email') as mock_send_email:
        notify_user("test@example.com", "Hello")
        mock_send_email.assert_called_once_with(
            "test@example.com", "Hello"
        )
```

## 8. Advanced Topics <a name="advanced"></a>

### Test Coverage
Use coverage.py to measure test coverage:
```bash
coverage run -m pytest
coverage report
```

### Continuous Integration
Example GitHub Actions workflow:
```yaml
name: Python Tests
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: pytest
```

### Property-Based Testing
Using hypothesis:
```python
from hypothesis import given
from hypothesis.strategies import lists, integers

@given(lists(integers()))
def test_sort_idempotent(lst):
    sorted_once = sorted(lst)
    sorted_twice = sorted(sorted_once)
    assert sorted_once == sorted_twice
```

### Tips for Testing Different Types of Code

1. **Testing Exceptions**
```python
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
```

2. **Testing Async Code**
```python
@pytest.mark.asyncio
async def test_async_function():
    result = await fetch_data()
    assert result is not None
```

3. **Testing Classes**
```python
class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()
    
    def test_add(self):
        assert self.calc.add(2, 3) == 5
```

Remember: The key to successful TDD is practice and gradually building up your testing skills. Start simple and progressively tackle more complex scenarios as you become comfortable with the basics.