from datetime import datetime

now = datetime.now()
timestamp = datetime.timestamp(now)

date: dict = {
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute
}

def formated_date(date) -> datetime:
        year = date["year"] 
        month = datetime.strptime(str(date["month"]), "%m").strftime("%B")
        day = date["day"]
        hour = date["hour"]
        minute = date["minute"]
        return f"Today is {month} {day}, {year}. It's {hour} hours with {minute} minutes."

f_date = formated_date(date)
print(f_date)

print("\n====================================================================\n")

sqrts = [i * i for i in range(40 + 1)] 
print(sqrts)
if 1024 in sqrts:
        print(1024 // 32)
        
print("\n====================================================================\n")
