import unittest
from unittest.mock import patch, MagicMock
from io import StringIO

from csv_to_ics import csv_to_ics  

class TestCsvToIcs(unittest.TestCase):

    @patch("builtins.open", new_callable=MagicMock)
    @patch("icalendar.Calendar.add_component")
    def test_csv_to_ics(self, mock_add_component, mock_open):
       
        csv_data = """First Name,Last Name,Birthday
John,Doe,1990-05-15
Jane,Smith,1992-07-20
"""
        mock_open.return_value.__enter__.return_value = StringIO(csv_data)

        mock_ics_file = MagicMock()
        csv_to_ics('contacts.csv', 'geburtstage.ics')
        self.assertEqual(mock_add_component.call_count, 2)

        mock_ics_file.write.assert_called()

if __name__ == "__main__":
    unittest.main()
