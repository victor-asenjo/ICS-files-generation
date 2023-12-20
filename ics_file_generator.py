import icalendar
from datetime import datetime
from icalendar import Calendar, Event

def generate_ics_file(subject, location, description, start_time, end_time):
    # Create a new calendar
    cal = Calendar()

    # Create an event
    event = Event()

    # Set event details
    event.add('summary', subject)
    event.add('location', location)
    event.add('description', description)

    # Convert string datetime to datetime object
    start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

    # Set event time
    event.add('dtstart', start_time)
    event.add('dtend', end_time)

    # Add the event to the calendar
    cal.add_component(event)

    # Save the calendar to a file
    with open('event.ics', 'wb') as f:
        f.write(cal.to_ical())

    print('ICS file generated successfully.')


def main():
    # Example usage
    subject = 'Meeting with Team'
    location = 'Conference Room 101'
    description = 'Discuss project updates and future plans.'
    start_time = '2023-01-01 09:00:00'
    end_time = '2023-01-01 10:30:00'

    # Get event details from the user
    subject = input('Enter the event subject: ')
    location = input('Enter the event location: ')
    description = input('Enter the event description: ')
    start_time = input('Enter the event start time (YYYY-MM-DD HH:MM:SS): ')
    end_time = input('Enter the event end time (YYYY-MM-DD HH:MM:SS): ')

    # Generate ICS file
    generate_ics_file(subject, location, description, start_time, end_time)

if __name__ == "__main__":
    main()
