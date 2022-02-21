from flask import Blueprint,jsonify,request,current_app
from app.models.serieModel import SerieModel
from datetime import datetime, date


bp_series = Blueprint('bp_series', __name__)


@bp_series.get('/seriado')
def get_all():
 
    series = SerieModel.query.all()
    
    
    return jsonify(series),200

@bp_series.post('/seriado')
def create():
    serie = request.get_json()

    series = datetime.strptime(serie['released_date'],'%d/%m/%Y').date()
    
    serie['released_date'] = series

    new_series = SerieModel(**serie)
    current_app.db.session.add(new_series)
    current_app.db.session.commit()

    return jsonify(serie),201







       
       
