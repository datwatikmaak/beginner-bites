cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    string_of_jeeps = ", "
    jeep_models = cars['Jeep']
    return string_of_jeeps.join(jeep_models)


get_all_jeeps(cars)


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_models = []
    for key, value in cars.items():
        first_models.append(value[0])

    return first_models


get_first_model_each_manufacturer(cars)


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    delimiter = ","
    models = cars["Ford"] + cars["Holden"] + cars["Nissan"] + cars["Honda"] + cars["Jeep"]

    # turn all models in one long string of models
    string_of_models = delimiter.join(models)

    # turn all models from the string into a list of all models
    list_of_models = string_of_models.split(",")

    # loop over list to check of a modelname contains grep
    models_grep = []
    for model in list_of_models:
        if grep.casefold() in model.casefold():
            models_grep.append(model)

    sorted_models_grep = sorted(models_grep)

    return sorted_models_grep


get_all_matching_models(cars)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    sorted_cars = {x: sorted(cars[x]) for x in cars.keys()}
    return sorted_cars


sort_car_models(cars)
