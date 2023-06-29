import sys
from tabulate import tabulate

# format * * * * *
# minute hour day_of_month month day_of_week

if len(sys.argv) < 2:
    print("Usage: python script.py <cron_string>")
    sys.exit(1)

cron_string = sys.argv[1]

def expand(field, start, end):
    expanded = set()

    if field == '*':
        expanded.update(range(start, end + 1))
    elif ',' in field:
        elements = field.split(',')
        for element in elements:
            expanded.update(expand_subfield(element, start, end))
    elif '-' in field or '/' in field:
        expanded.update(expand_subfield(field, start, end))
    else:
        expanded.add(int(field))

    expanded = {value for value in expanded if start <= value <= end}

    return expanded
    # empty input > ALL RANGE
    # if field == '*':
    #     expanded.update(range(start, end + 1))
    # elif '*,' in field:
    #     initialize = int(field[2:])
    #     expanded.update(initialize)
    # # Handle incrementing values
    # elif '*/' in field:
    #     increment = int(field[2:])                      # after */ character
    #     expanded.update(range(start, end + 1, increment))
    # else:
    #     # Parse individual values and ranges
    #     elements = field.split(',')
    #     for element in elements:
    #         if '-' in element:
    #             range_start, range_end = element.split('-')
    #             range_start = int(range_start)
    #             range_end = int(range_end)
    #             expanded.update(range(range_start, range_end + 1))
    #         else:
    #             expanded.add(int(element))
    #
    # # Filter values outside the valid range
    # expanded = {value for value in expanded if start <= value <= end}
    #
    # return expanded

def is_valid_field(field, start, end):
    if field == '*':
        return True

    elements = field.split(',')

    for element in elements:
        if '-' in element:
            range_start, range_end = element.split('-')
            if not range_start.isdigit() or not range_end.isdigit():
                return False
            if int(range_start) < start or int(range_end) > end:
                return False
        elif '/' in element:
            increment = element.split('/')[1]
            if not increment.isdigit() or int(increment) <= 0:
                return False
        elif not element.isdigit() or int(element) < start or int(element) > end:
            return False

    return True

def expand_subfield(subfield, start, end):
    subfield_expanded = set()
    #  TODO CASE 0   2,16-20/2    *   *   *
    if '-' in subfield and '/' in subfield:
        range_part, increment_part = subfield.split('/')
        range_start, range_end = range_part.split('-')
        range_start = int(range_start)
        range_end = int(range_end)
        increment = int(increment_part)
        for value in range(range_start, range_end + 1, increment):
            subfield_expanded.add(value)
    elif '-' in subfield:
        range_start, range_end = subfield.split('-')
        range_start = int(range_start)
        range_end = int(range_end)
        subfield_expanded.update(range(range_start, range_end + 1))
    elif '/' in subfield:
        increment = int(subfield.split('/')[1])
        subfield_expanded.update(range(start, end + 1, increment))
    else:
        subfield_expanded.add(int(subfield))

    return subfield_expanded

def print_table(minutes,hours,days_of_month, months, days_of_week, command):
    table_data = []
    table_header = ['Field', 'Expanded Times']
    table_data.append(['Minutes', ' ',minutes])
    table_data.append(['Hours', ' ', hours])
    table_data.append(['Days of Month', ' ' , days_of_month])
    table_data.append(['Months', ' ',months])
    table_data.append(['Days of Week', ' ', days_of_week])
    table_data.append(["Command" ,' ', command])

    print(tabulate(table_data, headers=table_header))

def pasrse_input_string(cron_string):
    fields = cron_string.split(' ') #cron string time values seperated by space

    output = []
    if not is_valid_field(fields[0], 0, 59) or not is_valid_field(fields[1], 0, 23) or not is_valid_field(fields[2], 1, 31) \
            or not is_valid_field(fields[3], 1, 12) or not is_valid_field(fields[4], 1, 7):
        print("Invalid Cron format. Check and Try Again")
        sys.exit(0)
    else:
        minutes = sorted(expand(fields[0],0,59))
        hours = sorted(expand(fields[1],0,23))
        days_of_month = sorted(expand(fields[2], 1,31))
        months = sorted(expand(fields[3],1,12))
        days_of_week = sorted(expand(fields[4],1,7))
        command = fields[5]

    print_table(minutes,hours,days_of_month, months, days_of_week, command)

    # return output

# cron_string = '*/15 0 1,15 * 1-5'
schedule = pasrse_input_string(cron_string)
