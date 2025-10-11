# SOME ADVANCE DATATYPES which we can import and use as required

# DATETIME, TIME, CALENDAR, TIMEDELTA, ARROW, DATEUTIL, COLLECTIONSS

# import arrow

# brewing_time = arrow.utcnow()
# brewing_time.to("Europe/Rome")

from collections import namedtuple

chaiProfile = namedtuple("chaiProfile", ["flavour","aroma","color"])