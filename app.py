from database import cars, personals, nativeworlds, biologicalspeciess, films
from flask import Flask, request, abort, json, jsonify
from domain import Car, BiologicalSpecies, Film, Personal, NativeWorld

app = Flask(__name__)

@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)



@app.route('/cars', methods=['POST'])
def update_cars():
    new_one = request.json
    cars.append(new_one)
    return jsonify(cars)


@app.route('/cars/<int:car_id>', methods=['PUT'])
def put_car(car_id):
    item = next((x for x in cars if x ["id"] == car_id), None)
    params = request.json
    if not item:
        return {"message": "Нет машин с этим id"}, 400
    item.update(params)
    return item


@app.route('/cars/<int:car_id>', methods=['PATCH'])
def patch_car(car_id):
    item = next((x for x in cars if x ["id"] == car_id), None)
    params = request.json
    if not item:
        return {"message": "Нет машин с этим id"}, 400
    item.update(params)
    return item


@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    idx, _ = next((x for x in enumerate(cars)
                   if x[1]['id'] == car_id), (None, None))
    cars.pop(idx)
    return " ", 204


@app.route('/personals', methods=['GET'])
def get_personal():
    return jsonify(personals)



@app.route('/personals', methods=['POST'])
def update_personal():
    new_one = request.json
    personals.append(new_one)
    return jsonify(personals)



@app.route('/personals/<int:personal_id>', methods=['PUT'])
def put_personal(personal_id):
    item = next((x for x in personals if x ["id"] == personal_id), None)
    params = request.json
    if not item:
        return {"message": "Нет персонажей с этим id"}, 400
    item.update(params)
    return item




@app.route('/personals/<int:personal_id>', methods=['PATCH'])
def patch_personal(personal_id):
    item = next((x for x in personals if x ["id"] == personal_id), None)
    params = request.json
    if not item:
        return {"message": "Нет персонажей с этим id"}, 400
    item.update(params)
    return item





@app.route('/personals/<int:personal_id>', methods=['DELETE'])
def delete_personal(personal_id):
    idx, _ = next((x for x in enumerate(personals)
                   if x[1]['id'] == personal_id), (None, None))
    personals.pop(idx)
    return " ", 204



@app.route('/nativeworlds', methods=['GET'])
def get_nativeworld():
    return jsonify(nativeworlds)




@app.route('/nativeworlds', methods=['POST'])
def update_nativeworld():
    new_one = request.json
    nativeworlds.append(new_one)
    return jsonify(nativeworlds)




@app.route('/nativeworlds/<int:nativeworld_id>', methods=['PUT'])
def put_nativeworld(nativeworld_id):
    item = next((x for x in nativeworlds if x ["id"] == nativeworld_id), None)
    params = request.json
    if not item:
        return {"message": "Нет родных миров с этим id"}, 400
    item.update(params)
    return item





@app.route('/nativeworlds/<int:nativeworld_id>', methods=['PATCH'])
def patch_nativeworld(nativeworld_id):
    item = next((x for x in nativeworlds if x ["id"] == nativeworld_id), None)
    params = request.json
    if not item:
        return {"message": "Нет родных миров с этим id"}, 400
    item.update(params)
    return item




@app.route('/nativeworlds/<int:nativeworld_id>', methods=['DELETE'])
def delete_nativeworld(nativeworld_id):
    idx, _ = next((x for x in enumerate(nativeworlds)
                   if x[1]['id'] == nativeworld_id), (None, None))
    nativeworlds.pop(idx)
    return " ", 204




@app.route('/biologicalspeciess', methods=['GET'])
def get_biologicalspecies():
    return jsonify(biologicalspeciess)




@app.route('/biologicalspeciess', methods=['POST'])
def update_biologicalspecies():
    new_one = request.json
    biologicalspeciess.append(new_one)
    return jsonify(biologicalspeciess)





@app.route('/biologicalspeciess/<int:biologicalspecies_id>', methods=['PUT'])
def put_biologicalspecies(biologicalspecies_id):
    item = next((x for x in biologicalspeciess if x ["id"] == biologicalspecies_id), None)
    params = request.json
    if not item:
        return {"message": "Нет биологических видов с этим id"}, 400
    item.update(params)
    return item




@app.route('/biologicalspeciess/<int:biologicalspecies_id>', methods=['PATCH'])
def patch_biologicalspecies(biologicalspecies_id):
    item = next((x for x in biologicalspeciess if x ["id"] == biologicalspecies_id), None)
    params = request.json
    if not item:
        return {"message": "Нет биологических видов с этим id"}, 400
    item.update(params)
    return item




@app.route('/biologicalspeciess/<int:biologicalspecies_id>', methods=['DELETE'])
def delete_biologicalspecies(biologicalspecies_id):
    idx, _ = next((x for x in enumerate(biologicalspeciess)
                   if x[1]['id'] == biologicalspecies_id), (None, None))
    biologicalspeciess.pop(idx)
    return " ", 204



@app.route('/films', methods=['GET'])
def get_film():
    return jsonify(films)





@app.route('/films', methods=['POST'])
def update_film():
    new_one = request.json
    films.append(new_one)
    return jsonify(films)




@app.route('/films/<int:film_id>', methods=['PUT'])
def put_film(film_id):
    item = next((x for x in films if x ["id"] == film_id), None)
    params = request.json
    if not item:
        return {"message": "Нет фильмов с этим id"}, 400
    item.update(params)
    return item




@app.route('/films/<int:film_id>', methods=['PATCH'])
def patcg_film(film_id):
    item = next((x for x in films if x ["id"] == film_id), None)
    params = request.json
    if not item:
        return {"message": "Нет фильмов с этим id"}, 400
    item.update(params)
    return item



@app.route('/films/<int:film_id>', methods=['DELETE'])
def delete_film(film_id):
    idx, _ = next((x for x in enumerate(films)
                   if x[1]['id'] == film_id), (None, None))
    films.pop(idx)
    return " ", 204





if __name__ == '__main__':
    app.run()