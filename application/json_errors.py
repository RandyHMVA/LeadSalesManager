import json


def invalid_api_key():
    return json.dumps({'error': "invalid api key"})

def invalid_sub_api_key():
    return json.dumps({'error': "invalid sub api key"})

def invalid_vendor_id():
    return json.dumps({'error': "invalid vendor id"})

def invalid_sub_vendor_id():
    return json.dumps({'error': "invalid sub vendor id"})

def vendor_id_DNE():
    return json.dumps({'error': "vendor id does not exist"})

def sub_vendor_id_DNE():
    return json.dumps({'error': "sub vendor id soes not exist"})

def api_offline():
    return json.dumps({'error': "api server is offline, this could be either maintenance or catastrophic failure.."})

def missing_fields():
    return json.dumps({'error': "missing fields"})

def invalid_permission():
    return json.dumps({'error': "invalid permissions"})

def failed_creating_sub_vendor():
    return json.dumps({'error': "failed to create sub vendor"})

def failed_deleting_sub_vendor():
    return json.dumps({'error': "failed to delete sub vendor"})

def existing_lead():
    return json.dumps({'error': "lead duplicate"})

def missing_required_fields():
    return json.dumps({'error': "missing required fields"})

def missing_required_posts():
    return json.dumps({'error': "missing required posts"})

def invalid_answers(wrong_answers):
    return json.dumps({'error': "invalid answers for field ids: " + str(wrong_answers)})

def missing_intrinsics(missing_intrinsics):
    return json.dumps({'error': "missing instrinsics " + str(missing_intrinsics)})

def invalid_intrinsics(error_message):
    return json.dumps({'error': str(error_message)})

def bad_vertical_data(lead_vertical):
    return json.dumps({'error': str(lead_vertical) + " is badly formatted or does not exist as a vertical in the system"})

def no_vertical_data():
    return json.dumps({'error': "no vertical data"})

def multi_vertical_verse():
    return json.dumps({'errors': "multiple verticals exist"})

def no_lead():
    return json.dumps({'error': "no lead in post"})