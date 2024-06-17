from domain import Car, Personal, NativeWorld, Film, BiologicalSpecies

cars = {
    1: Car(id=1, name="Машина 1"),
    2: Car(id=2, name="Машина 2"),
    3: Car(id=3, name="Машина 3"),

}



nativeworlds = {
    1: NativeWorld(id=1, name="Земля"),
}



films = {
    1: Film(id=1, name="Приключения кота Леопольда"),
}


biologicalspeciess = {
    1: BiologicalSpecies(id=1, name="Кот"),
}



personals = {
    1: Personal(id=1, name="Леопольд", age=38, height=164, hair_color="Оранжевые", eyes_color="Черные",
                year_of_birth=1937, gender="Мужской", car=cars[1], nativeworld=nativeworlds[1], film=films[1],
                biologicalspecies=biologicalspeciess[1]),
}

