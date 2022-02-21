from xml.dom import NotFoundErr
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

@bp_series.patch('/seriado/:serie_id')
def update(id):
    try:
        data = request.get_json()

        serie = SerieModel.query.get(id)

        if data['released_date']:
            series = datetime.strptime(data['released_date'],'%d/%m/%Y').date()
            data['released_date'] = series

        for key, value in data.items():
            setattr(serie, key, value)

        current_app.db.session.add(serie)
        current_app.db.session.commit()

        return jsonify(serie),200
    except AttributeError:
        return jsonify({'msg':'Serie not found'}), 404


@bp_series.delete('/seriado/:serie_id')
def deletando(serie_id):
    try:
        query = SerieModel.query.filter_by(id=serie_id).first_or_404()
        current_app.db.session.delete(query)
        current_app.db.session.commit()
        return '', 204
    except NotFoundErr:
        return {"Error": "Serie not Found"}, 404






       
       
