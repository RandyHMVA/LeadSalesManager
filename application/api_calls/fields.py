import json
import datetime
from application import json_errors


def get_required_fields(database,post_data,vendor_id_type):
    field_data = database.get_required_fields(post_data["vertical_id"])

    fields = []
    for field in field_data:
        field_d = {"field_id": field["field_id"], "field": field["field"], "multiple_answers": field["multiple_answers"], "no_key": field["no_key"]}
        fields.append(field_d)

    json_template = {"required_fields": fields}
    return json.dumps(json_template)

def get_answer_key(database,post_data,vendor_id_type):
    answer_data = database.get_answer_key(post_data["field_id"])

    answers = []
    for answer in answer_data:
        answer_d = {"answer_id": answer["answer_id"], "answer": answer["answer"]}
        answers.append(answer_d)

    json_template = {"answer_key": answers}
    return json.dumps(json_template)
