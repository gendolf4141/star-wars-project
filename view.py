from database import cars
from flask import Flask, request, abort, json
from domain import Car

app = Flask(__name__)

@app.route('/cars', methods=['GET', 'POST'])
def get_cars():
    if request.method == "GET":
        values = []
        for car in cars.values():
            values.append(car.model_dump_json())
        return {"cars": values}

    if request.method == "POST":
        #TODO:
        data = json.loads(request.data)
        car = Car(**data)
        cars[car.id] = car
        return car.model_dump_json()


@app.route('/cars/<int:cars_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def crud_car(id: int):
    if request.method == "GET":
        for key, car in cars.items():
            if car.id == id:
                return car.model_dump_json()
        return {"responce": f"Машина с id {id} не найдена"}

# Должны изменять полный обьект(должны получить от пользователя все поля)
# Проверить что id пользователя есть в базе данных
# Проверить что данные переданы правильно(name, id)
# Изменить значения в базе данных данными полученными от пользователя
    if request.method == "PUT":
        return {
            'id': id,
            'method': request.method,
        }


# Проверить что id пользователя есть в базе данных
# Удалить и дать понять пользователю что данные удалены
    if request.method == "DELETE":
        return {
            'id': id,
            'method': request.method,
        }
# Должны изменять полный обьект(должны получить от пользователя все поля)
# Проверить что id пользователя есть в базе данных
# Проверить что данные переданы правильно(name, id)
# Изменить значения в базе данных данными полученными от пользователя
    if request.method == "PATCH":
        return {
            'id': id,
            'method': request.method,
        }



if __name__ == '__main__':
    app.run()



