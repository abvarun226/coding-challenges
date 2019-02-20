import calendar

if __name__ == "__main__":
    in1 = raw_input()
    mm, dd, yy = map(int, in1.split())
    weekday = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    print(weekday[calendar.weekday(yy, mm, dd)])
