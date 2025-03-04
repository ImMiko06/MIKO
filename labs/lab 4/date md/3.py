from datetime import datetime

now = datetime.now()
now_without_microseconds = now.replace(microsecond=0)

print("Original datetime:", now)
print("Datetime without microseconds:", now_without_microseconds)
