from database import db_session
from models import Hotel
import hashlib
hotels = [
{'name': 'Hotel #1', 'addr': '1st Street', 'price': 100, 'rating': 3.5, 'description': 'description', 'services': 'services'},
{'name': 'Hotel #2', 'addr': '2st Street', 'price': 10, 'rating': 1.5, 'description': 'description', 'services': 'services'},
{'name': 'Hotel #3', 'addr': '3st Street', 'price': 75, 'rating': 5.0, 'description': 'description', 'services': 'services'},
{'name': 'Hotel #4', 'addr': '4st Street', 'price': 80, 'rating': 4.5, 'description': 'description', 'services': 'services'},
{'name': 'Hotel #5', 'addr': '5st Street', 'price': 30, 'rating': 4.3, 'description': 'description', 'services': 'services'}
]


for hotel in hotels:
	s = Hotel(hotel['name'], hotel['addr'], hotel['price'],hotel['rating'],hotel['description'],hotel['services'])
	db_session.add(s)
	db_session.commit()