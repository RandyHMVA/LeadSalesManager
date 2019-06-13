import json
import datetime
from application import json_errors


def get_verticals(database,post_data,vendor_id_type):

    vertical_data = database.get_verticals()

    json_template = {}
    verticals = []
    for vertical in vertical_data:
        vertical_d = {"vertical_id": vertical["vertical_id"], "vertical": vertical["vertical"]}
        verticals.append(vertical_d)

    json_template = {"verticals": verticals}
    return json.dumps(json_template)