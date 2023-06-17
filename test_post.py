import requests
from datetime import date

url_booking = 'http://127.0.0.1:5000/bookings'
url_reviews = 'http://127.0.0.1:5000/reviews'

# Make post request to add new booking
r = requests.post(url_booking, data = {'hotel_id': 1, 'in_date': datetime.now().timestamp(), 'out_date': datetime.now().timestamp()})
print(r.json())
# Make post request to add new review
r = requests.post(url_reviews, data = {'hotel_id': 1, 'rating': 3.4, 'text': 'Norm'})
print(r.json())
