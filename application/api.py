from application import api_validator
from application import json_errors
from application import db

# api_call   --->   logic
#   0. connects to database
#   1. valiate the fields posted to the api call
#   2. set vendor_id_type to either a vendor_id or a sub_vendor_id
#   3. deny use of api on calls to functions with no_sub_api flag set when vendor_id_type = sub_vendor_id
#   4. validate the api key to be a valid api key for the given vendor or sub vendor id
#   5. on valid key make the api call
#   6. else return error message

# def api_call(api_function,required_fields,no_sub_api,post_data):
#     database = db.database()
#     if database.is_connected:
#         if api_validator.validate_fields(required_fields, post_data):

#             if database.check_if_existing_vendor_id(post_data["vendor_id"]):
#                 vendor_id_type = "vendor_id"
#             else:
#                 if database.check_if_existing_sub_vendor_id(post_data["vendor_id"]):
#                     vendor_id_type = "sub_vendor_id"
#                 else:
#                     return json_errors.invalid_vendor_id()

#             if vendor_id_type == "sub_vendor_id" and no_sub_api:
#                 database.insert_api_event(post_data["vendor_id"],post_data["api_key"],str(api_function), "FAILED")
#                 return json_errors.invalid_permission()
#             else:
#                 if vendor_id_type == "vendor_id":
#                     valid_key, error_response = api_validator.validate_api(database,post_data["vendor_id"], post_data["api_key"])
#                     if valid_key:
#                         json_data = api_function(database,post_data,vendor_id_type)
#                         database.insert_api_event(post_data["vendor_id"], post_data["api_key"], api_function.__name__, str(json_data))
#                         return json_data
#                     else:
#                         database.insert_api_event(post_data["vendor_id"], post_data["api_key"], api_function.__name__, error_response)
#                         return error_response

#                 else:
#                     valid_key, error_response = api_validator.validate_sub_api(database,post_data["vendor_id"], post_data["api_key"])
#                     if valid_key:
#                         json_data = api_function(database,post_data,vendor_id_type)
#                         database.insert_api_event(post_data["vendor_id"], post_data["api_key"], api_function.__name__, str(json_data))
#                         return json_data
#                     else:
#                         database.insert_api_event(post_data["vendor_id"], post_data["api_key"], api_function.__name__, error_response)
#                         return error_response

#         else:
#             return json_errors.missing_required_posts()
#     else:
#         return json_errors.api_offline()