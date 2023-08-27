from datetime import datetime
# from datetime import time
from datetime import date

today = datetime.now()
print(today.strftime('%Y'))

from datetime import datetime

today = datetime.now()

print(today.strftime('%c'))
print(today.strftime('%x'))
print(today.strftime('%X'))
