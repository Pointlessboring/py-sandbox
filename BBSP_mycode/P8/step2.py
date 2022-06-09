# Step 0: Dabbling with datetime basics
# https://docs.python.org/3/library/datetime.html
# Define the DOW and MOY variables

# Step 1: Added structure and user inputs.
# Step 2: Write calendar drawing function

from calendar import weekday
from datetime import date, datetime, timedelta
# Build string of weekdays starting Sunday
DOW = [date.strftime((date.today() + timedelta(d - date.isoweekday(date.today()))) ,"%A") for d in range (7)]

# Build string of months
MOY = [date.strftime( date(1,m+1,1) ,"%B") for m in range (12)]

def main():


    while True:  # Input a year from the user.
        print('Enter the year for the calendar:')
        response = input('> ')
        if response.isdecimal() and int(response) > 0:
            year = int(response)
            break
        else: 
            print('Please enter a numeric year, like 2023.')

    while True:  # Input a month from the user.
        print('Enter the month for the calendar: (1 to 12)')
        response = input('> ')
    
        if response.isdecimal() and int(response) > 0:
            month = int(response)
            break
        else: 
            print('Please enter a numeric month, like 6 for June.')

    # Compute the calendar the month
    caltext = ''
    caltext = drawCalendar(year, month)

    # Display the calendar
    print(caltext)

    # Save the calendar to a file
    filename = f"calendar_{year}_{month}.txt"

    with open(filename, 'w') as f:
        f.write(caltext)
    
    print(f"\nCalendar was saved to {filename}")

def drawCalendar(year, month):
    text = ''
    text += (' ' * 34) + MOY[month - 1] + ' ' + str(year) + '\n'
    
    text += ''.join([ (f'{day :{"."}^{11}}') for day in DOW]) + '\n'
    
    weekRow = "+----------" * 7 + '+\n'
    blankRow = ('|          ' * 7) + '|\n'

    # Calculate the date of the top left square.
    leftdate = date(year, month, 1) - timedelta(date(year, month, 1).isoweekday())
    
    while True: # Loop for every week in the month

        # Add top border for the week
        text += weekRow
        
        for d in range(7): # Add each day of the week for the date row.
            text += '|' + str( (leftdate+timedelta(d)).day).rjust(10)  

        # Add the carriage return for the date row and add 3 blank rows.  
        text += '|\n' + blankRow * 3
        
        # Move to the following week and check if we have completed the month
        leftdate += timedelta(7) 

        if leftdate.month != month:
            text += weekRow  # If so, add bottom border and return the calendar
            return text

# If this program was run (instead of imported), run main():
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('=- Insert name of program -=, by @PointlessBoring')
