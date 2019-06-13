import pymysql

from application import json_errors


def validate_api(database,vendor_id,api_key):

    stored_key = database.get_api_key(vendor_id)["api_key"]
    valid = True if str(stored_key) == str(api_key) else False

    if valid:
        return True, None
    else:
        return False, json_errors.invalid_api_key()


def validate_sub_api(database,sub_vendor_id,sub_api_key):

    stored_key = database.get_sub_api_key(sub_vendor_id)["sub_api_key"]
    valid = True if str(stored_key) == str(sub_api_key) else False

    if valid:
        return True, None
    else:
        return False, json_errors.invalid_api_key()


def validate_fields(field_list,fields):
    for field in field_list:
        if field not in fields:
            return False
    return True
