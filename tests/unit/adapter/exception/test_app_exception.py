"""
Test the AlchidanticException class

:author: Alex Traveylan
:date: 2024
"""

from alchidantic.adapter.exception.app_exception import AlchidanticException


def test_app_exception():
    """Test the AppException class."""

    message = "Test exception message"
    exception = AlchidanticException(message)

    assert str(exception) == message
