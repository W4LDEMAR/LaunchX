from datetime import *
from dateutil.relativedelta import *
ahora = datetime.now()
print(ahora)

ahora = ahora + relativedelta(months=1, weeks=1, hour=10)

print(ahora)