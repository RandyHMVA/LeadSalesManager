import json

def get_makes(database,post_data,vendor_id_type):
    makes = database.get_vehicle_makes()
    make_list = []
    for make in makes:
        make_list.append(make["make"])
    return json.dumps({'makes': make_list})

def get_models(database,post_data,vendor_id_type):
    models = database.get_vehicle_models(post_data["make"])
    model_list = []
    for model in models:
        model_list.append(model["model"])
    return json.dumps({'models': model_list})