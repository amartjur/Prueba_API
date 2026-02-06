#!/usr/bin/env python3
"""
Tests para verificar la funcionalidad del script de saludo
"""

from unittest.mock import patch
from datetime import datetime
import main


def test_greeting_times():
    """
    Prueba el script con diferentes horas del día
    """
    print('Testing greeting script with different times...')
    print()
    
    # Test cases: (hour, minute, expected_greeting)
    test_cases = [
        (6, 1, 'Buenos días'),      # Start of Buenos días
        (9, 30, 'Buenos días'),      # Middle of Buenos días
        (12, 0, 'Buenos días'),      # End of Buenos días
        (12, 1, 'Buenas tardes'),    # Start of Buenas tardes
        (15, 30, 'Buenas tardes'),   # Middle of Buenas tardes
        (20, 0, 'Buenas tardes'),    # End of Buenas tardes
        (20, 1, 'Buenas noches'),    # Start of Buenas noches
        (23, 30, 'Buenas noches'),   # Night time
        (0, 0, 'Buenas noches'),     # Midnight
        (3, 30, 'Buenas noches'),    # Early morning
        (6, 0, 'Buenas noches'),     # Just before Buenos días
    ]
    
    all_passed = True
    for hour, minute, expected in test_cases:
        # Create a mock datetime
        mock_time = datetime(2024, 1, 1, hour, minute)
        
        with patch('main.datetime') as mock_datetime:
            mock_datetime.now.return_value = mock_time
            result = main.obtener_saludo()
        
        status = '✓' if result == expected else '✗'
        
        if result != expected:
            all_passed = False
            
        print(f'{status} {hour:02d}:{minute:02d} -> {result} (expected: {expected})')
    
    print()
    if all_passed:
        print('✓ All tests passed!')
        return True
    else:
        print('✗ Some tests failed!')
        return False


if __name__ == "__main__":
    success = test_greeting_times()
    exit(0 if success else 1)
