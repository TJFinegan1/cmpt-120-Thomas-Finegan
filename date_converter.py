def convert(date):
    '''
    Enter date as Month Day, Year
    '''

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "Novmember",
        "December"

    ]

    month, day, year = date.split()
    
    day_number = day[:2]
    if not day.isdigit() or int(day) < 1 or int(day) > 31:
        raise Exception("Invalid date, please enter number 1-31")

    print(month)
    print(day)
    print(year)
    
    formatted_month = month.capitalize()
    
    index = -1
    for i in range(len(months)):
        if months[i].startswith(formatted_month):
            index = i + 1
            break
        
    if index == -1:
        raise Exception("Invalid Month! Must be one of", months)
        
    month_number = index
    if index < 10:
        month_number = "0{0}".format(index)
    
    print("Formatted month:", month_number)
    
    if not year.isdigit():
        raise Exception("Invalid Year Format; must be digit!")
    
    print(month_number + "/" )

convert("May 24, 2022")