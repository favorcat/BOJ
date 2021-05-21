from datetime import datetime
now = datetime.utcnow()
print(now.strftime('%Y'))
print(now.strftime('%m'))
print(now.strftime('%d'))