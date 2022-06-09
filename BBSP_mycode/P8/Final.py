# Step 0: Dabbling with datetime basics
#         https://docs.python.org/3/library/datetime.html
#         Defined the DOW and MOY variables
# Step 1: Added structure and user inputs.
# Step 2: Write calendar drawing function
# Step 3: Clean up
# Final : More clean-up, plus final touches.

from datetime import date, datetime, timedelta

# Build string of weekdays starting Sunday
# Given that these are constants, they (perhaps) should be in extension
#  but it was an opportunity to test date functions

DOW = [date.strftime((date.today() + 
       timedelta(d - date.isoweekday(date.today()))) ,"%A") 
            for d in range (7)]

MOY = [date.strftime( date(1,m+1,1) ,"%B") for m in range (12)]

def main():
    """This function create a printable calendar for a given month."""

    while True:  # Input a year from the user.
        print('Enter the year for the calendar:')
        response = input('> ')
        if response.isdecimal() and int(response) > 0:
            year = int(response)
            break
        else: 
            print('Please enter a year, like 2022.')

    while True:  # Input a month from the user.
        print('Enter the month for the calendar: (1 to 12)')
        response = input('> ')
    
        if response.isdecimal() and int(response) > 0:
            month = int(response)
            break
        else: 
            print('Please enter a numeric month, like 6 for June.')

    # Compute the calendar the month
    caltext = drawCalendar(year, month)

    # Display the calendar
    print(caltext)

    # Save the calendar to a file
    filename = f"{year}_{month}_calendar.txt"
    with open(filename, 'w') as f:
        f.write(caltext)
    print(f"\nCalendar was saved to {filename}")

def drawCalendar(year, month):
    """This function 'draws' the calendar and returns it."""

    # Create the empty text string and add the month and year as a title.
    text = ''
    text += (' ' * 34) + MOY[month - 1] + ' ' + str(year) + '\n'

    # Add the days of week padded with '.'. Change DOW code abbreviated days.
    text += ''.join([ (f'{day :{"."}^{11}}') for day in DOW]) + '\n'
    
    # These are filler rows that will be used to draw the calendar.
    weekRow = "+----------" * 7 + '+\n'
    blankRow = ('|          ' * 7) + '|\n'

    # Calculate the date of the top left square.
    ldate = date(year, month, 1) - timedelta(date(year, month, 1).isoweekday())
    
    while True: # Loop for every week in the month
        # Add top border when starting a week.
        text += weekRow
        
        for d in range(7): # Add each day of the week for the date row.
            text += '|' + str( (ldate+timedelta(d)).day).rjust(10)  

        # Add the carriage return for the date row and add 3 blank rows.  
        text += '|\n' + blankRow * 3
        
        # Move to the following week and check if we have completed the month
        ldate += timedelta(7) 

        if ldate.month != month:
            text += weekRow  # If so, add bottom border and return calendar
            return text

# If this program was run (instead of imported), run main():
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('=- Insert name of program -=, by @PointlessBoring')
