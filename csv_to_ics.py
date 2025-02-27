import csv
from datetime import datetime
from icalendar import Calendar, Event

def csv_to_ics(csv_file, ics_file):
    cal = Calendar()
    
    with open(csv_file, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row.get('First Name', '').strip() + ' ' + row.get('Last Name', '').strip()
            birthday = row.get('Birthday', '').strip()
            
            if birthday:
                try:
                    date = datetime.strptime(birthday, '%Y-%m-%d').date()
                    event = Event()
                    event.add('summary', f'Geburtstag: {name.strip()}')
                    event.add('dtstart', date)
                    event.add('rrule', {'freq': 'yearly'})
                    cal.add_component(event)
                except ValueError:
                    print(f'Ungültiges Datum für {name}: {birthday}')
    
    with open(ics_file, 'wb') as f:
        f.write(cal.to_ical())
    
    print(f'ICS-Datei gespeichert als {ics_file}')

if __name__ == "__main__":
    csv_to_ics('contacts.csv', 'geburtstage.ics') # Change to your filepath
