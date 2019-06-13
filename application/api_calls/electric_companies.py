import json
import datetime
from application import json_errors

def get_states(database,post_data,vendor_id_type):
    states = database.get_states()
    state_list = []

    for state in states:
        state_list.append(state["state"])

    json_template = {"states": state_list}
    return json.dumps(json_template)


def get_electric_companies(database,post_data,vendor_id_type):
    companies = database.get_electric_companies(post_data["state"])
    companies_list = []
    for company in companies:
        companies_list.append(company["company"])
    return json.dumps({'companies': companies_list})