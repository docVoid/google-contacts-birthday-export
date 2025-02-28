# Google Contacts Birthday Exporter

This Python script extracts birthdays from a Google Contacts CSV export and converts them into an ICS calendar file. The resulting ICS file can easily be imported into Google Calendar for automatic event creation.

## Features
- Extracts birthdays from a CSV file exported from Google Contacts.
- Converts the birthdays into an ICS calendar file.
- Simplifies the process of adding multiple birthdays to Google Calendar.

## Requirements
- Python 3.x
- `icalendar` library (install with `pip install icalendar`)

## How to Export Google Contacts
To export your Google Contacts to a CSV file with birthdays, follow these steps:

1. Open [Google Contacts](https://contacts.google.com).
2. On the left sidebar, click on **Export**.
3. Choose **Google CSV** as the export format. This will include your contacts details such as name, email, and birthday.
4. Click **Export**, and the CSV file will be downloaded to your computer.

## How to Run the Script
1. Clone or download this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install icalendar
3. Place your downloaded Google Contacts CSV file (e.g., contacts.csv) in the same directory as the script.

4. Run the script:
    ```bash
    python csv_to_ics.py
5. The script will generate a file named birthdays.ics containing the birthday events.


## How to Import the ICS File into Google Calendar
1. Open [Google Calendar](https://calendar.google.com).
2. On the left sidebar, click the + next to **Other calendars** and select **Import**.
3. Click **Select file from your computer** and choose the `birthdays.ics` file generated by the script.
4. Select the calendar to which you'd like to add the birthdays.
5. Click **Import**, and all the birthdays will be added as recurring events in your Google Calendar.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 