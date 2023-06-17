from flask import *
from database import db_session
from datetime import date
import models

app = Flask(__name__)

### MAIN ROUTING ###


# Получение списка всех отелей. Ответ должен включать название, адрес, цену за ночь и оценку отеля.
@app.route("/hotels")
def get_hotels():
    hotels = [h.base_serialize for h in models.Hotel.query.all()]
    return hotels

# Получение информации о конкретном отеле, включая подробное описание и список доступных удобств.
@app.route("/hotels/<int:hotel_id>")
def get_hotel(hotel_id):
    res = models.Hotel.query.filter_by(id = hotel_id).first()
    if res == None:
        return {'error': 'Id not found', 'code': 404}, 404
    return res.serialize

# Бронирование отеля. Запрос должен включать ID отеля, дату заезда и дату отъезда.
# Была добавлена возможность посмотреть все бронирования для удобства
@app.route("/bookings", methods=['GET', 'POST'])
def make_booking():
    if (request.method == 'GET'):
        bookings = [i.serialize for i in models.Booking.query.all()]
        return bookings
    hotel_id = request.form.get('hotel_id', None)
    in_date = request.form.get('in_date', None)
    out_date = request.form.get('out_date', None)
    if hotel_id == None or in_date == None or out_date == None:
        return {'error': 'Fields are empty or incorrect', 'code': 403}, 403
    try:
        hotel_id_ = int(hotel_id)
        in_date_ = float(in_date)
        out_date_ = float(out_date)
    except Exception as e:
        return {'error': 'Fields are empty or incorrect', 'code': 403}, 403
    booking = models.Booking(hotel_id_, date.fromtimestamp(in_date_), date.fromtimestamp(out_date_))
    db_session.add(booking)
    db_session.commit()
    return {'code': 200}, 200

# Получение отзывов о конкретном отеле.
@app.route("/reviews/<int:hotel_id>")
def get_reviews(hotel_id):
    reviews = [h.serialize for h in models.Review.query.filter_by(hotel_id = hotel_id).all()]
    return reviews

# Оставление отзыва о отеле. Запрос должен включать ID отеля, оценку и текст отзыва.
@app.route("/reviews", methods=['POST'])
def make_review():
    hotel_id = request.form.get('hotel_id', None)
    rating = request.form.get('rating', None)
    text = request.form.get('text', None)
    if hotel_id == None or rating == None or text == None:
        return {'error': 'Fields are empty or incorrect', 'code': 403}, 403
    try:
        hotel_id_ = int(hotel_id)
        rating_ = float(rating)
    except Exception as e:
        return {'error': 'Fields are empty or incorrect', 'code': 403}, 403
    if rating_ < 0 or rating > 5:
        return {'error': 'Rating is incorrect', 'code': 403}, 403
    review = models.Review(hotel_id_, rating_, text)
    db_session.add(review)
    db_session.commit()
    return {'code': 200}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)