import json
import datetime
import pymysql
from application import json_errors
from application import keys


def get_sub_vendors(database,post_data,vendor_id_type):
    data_list = database.get_sub_vendors(post_data["vendor_id"])

    json_template = {}
    sub_vendors = []
    for sub_vendor in data_list:
        sub_vendor_d = { "sub_vendor_id": sub_vendor["sub_vendor_id"], "sub_vendor_name": sub_vendor["sub_vendor_name"], "sub_api_key": sub_vendor["sub_api_key"], "creation_date": str(sub_vendor["creation_date"])}
        sub_vendors.append(sub_vendor_d)

    json_template["sub_vendors"] = sub_vendors

    return json.dumps(json_template)


def add_sub_vendor(database,post_data,vendor_id_type):
    try:
        sub_vendor_id = keys.generate_vendor_id()
        sub_vendor_api_key = keys.generate_api_key()
        inserted = database.add_sub_vendor(post_data["vendor_id"],post_data["api_key"],post_data["sub_vendor"],sub_vendor_id,sub_vendor_api_key)
    except:
        return json_errors.failed_creating_sub_vendor()

    if inserted:
        json_template = {"sub_vendor_id": sub_vendor_id, "sub_vendor_api_key": sub_vendor_api_key, "sub_vendor": post_data["sub_vendor"]}
        return json.dumps(json_template)
    else:
        return json_errors.failed_creating_sub_vendor()


def delete_sub_vendor(database,post_data,vendor_id_type):
    delete_attempt = database.delete_sub_vendor(post_data["vendor_id"],post_data["sub_vendor_id"])
    return json.dumps({'sub_vendor_id': post_data["sub_vendor_id"]}) if delete_attempt else json_errors.failed_deleting_sub_vendor()