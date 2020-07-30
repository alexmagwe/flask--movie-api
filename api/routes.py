from flask import Blueprint,jsonify,request
api=Blueprint('api',__name__)
from .import db
from .models import Movies
@api.route('/add_movie',methods=['POST'])
def add_movie():
    movie_data=request.get_json()
    if movie_data['title'] and movie_data['rating']:
        movie=Movie(title=movie_data.get('title'),rating=movie_data.get('rating'))
        db.session.add(movie)
        db.session.commit()
    return 'done',301
@api.route('/movies')
def movies():
    allmovies=Movies.query.all()
    mvs=[]
    for mv in allmovies:
       mvs.append({'title':mv.title,'rating':mv.rating})
    print('movies:',mvs)
    return jsonify({'movies':mvs})




