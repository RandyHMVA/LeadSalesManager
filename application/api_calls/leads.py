import json

import datetime
from application import json_errors
from application import keys
from mailchimp3 import MailChimp
import requests

from application import json_errors

# add_lead logic
#   1. Check for valid intrinsic properties to leads
#   2. compute security hash and check for duplicate entry
#   3. check if vertical field is valid for lead.

#   3. validate all required fields
#   4. validate all answers to all questions

def add_lead(database,post_data,vendor_id_type):

    try:
        json_lead = json.loads(post_data["lead"])
    except:
        try:
            json_lead = post_data["lead"]
        except:
            return json_errors.no_lead()

    exisiting_lead = False

    valid_intrinsics, missing_instrinsics = valididate_intrinsics(json_lead)
    if valid_intrinsics:
        hashing_security = json_lead["first_name"].lower().replace(" ","") + json_lead["last_name"].lower().replace(" ","") + str(json_lead["phone"])
        hashed_digest = keys.compute_security_hash(hashing_security)

        try:
            lead_vertical = json_lead["vertical"]
        except KeyError:
            try:
                lead_vertical = json_lead["verticals"]
            except KeyError:
                return json_errors.no_vertical_data()

        if not validate_vertical(database,lead_vertical):
            return json_errors.bad_vertical_data(lead_vertical)

        if database.check_if_existing_lead(hashed_digest):
            lead_id = database.hashed_digest_lookup(hashed_digest)
            exisiting_lead = True
            if database.check_if_lead_vertical_exists(lead_id,lead_vertical):
                return json_errors.existing_lead()

        required_fields_list = generate_required_fields(database,lead_vertical)

        if validate_lead_fields(json_lead["fields"],required_fields_list):
            valid_answers, wrong_answers = validate_answers(database,json_lead["fields"])
            if valid_answers:
                if not exisiting_lead:
                    lead_id = keys.generate_lead_id()

                if vendor_id_type == "sub_vendor_id":
                    sub_vendor_id = post_data["vendor_id"]
                    vendor_id = database.get_vendor_from_sub_vendor(sub_vendor_id)["vendor_id"]
                else:
                    vendor_id = post_data["vendor_id"]
                    sub_vendor_id = ""



                rep_id = ""
                rep_name = ""
                if lead_vertical == 1 or lead_vertical[0] == 1 or lead_vertical == "1":

                    if sub_vendor_id == "CAEFFF7079F14E5D9C5D75C29635E2BB":
                        rep_id = "flex"
                        rep_name = "flex"
                    else:
                        total_auto_leads = database.get_total_auto_leads()
                        if total_auto_leads % 2 == 0:
                            rep_id = "lh661"
                            rep_name = "Laurie"
                        else:
                            rep_id = "mh778"
                            rep_name = "Melissa"
                        subscribe_mail_chimp(database, lead_id, json_lead, lead_vertical, rep_id, rep_name) #subscribes to mailchimp list based on which vertical

                database.add_lead(lead_id,json_lead,hashed_digest,vendor_id,sub_vendor_id, exisiting_lead, lead_vertical, rep_id)



                return json.dumps({'success': lead_id})
            else:
                return json_errors.invalid_answers(wrong_answers)
        else:
            return json_errors.missing_required_fields()

    else:
        return json_errors.missing_intrinsics(missing_instrinsics)

def subscribe_mail_chimp(database, lead_id, json_lead, lead_vertical, rep_id, rep_name):
    ####AUTO WARRANTIES####
    if lead_vertical == 1 or lead_vertical[0] == 1 or lead_vertical == "1":
        try:
            client = MailChimp(mc_api='edc69c97625c830eef2fee09da524e47-us19', mc_user='Apex Marketing')
            data = client.lists.members.create('cacd930943', {
                'email_address': json_lead["email"],
                'status': 'subscribed',
                'merge_fields': {
                    'FNAME': json_lead["first_name"],
                    'LNAME': json_lead["last_name"],
                    'PHONE': json_lead["phone"],
                    'REP_ID': rep_id,
                    'REP_NAME': rep_name,
                },
            })
            database.update_mailchimp_id(lead_id, data["id"])
        except Exception as e:
            pass


def validate_vertical(database, lead_vertical):
    if type(lead_vertical) is int:
            if lead_vertical <= 27:
                return True
    elif type(lead_vertical) is list:
        if len(lead_vertical) == 1:
            return True
        else:
            return False
    else:
        try:
            if int(lead_vertical) <= 27:
                return True
            else:
                return False
        except:
            return False
    return False


def generate_required_fields(database,lead_vertical):
    required_fields_list = []
    required_fields = database.get_required_fields(lead_vertical)
    for field in required_fields:
        if field["field_id"] not in required_fields_list:
            required_fields_list.append(field["field_id"])

    return required_fields_list


def generate_answers(database,field_id):
    answer_key = database.get_answer_key(field_id)
    answers = []
    for answer in answer_key:
        answers.append(answer["answer_id"])
    return answers


def valididate_intrinsics(lead):
    missing_intrinsics = []
    valid = True

    if "mode" not in lead:
        valid = False
        missing_intrinsics.append("mode")
    else:
        pass

    if "first_name" not in lead:
        valid = False
        missing_intrinsics.append("first_name")
    else:
        pass

    if "last_name" not in lead:
        valid = False
        missing_intrinsics.append("last_name")
    else:
        pass

    if "ip_address" not in lead:
        valid = False
        missing_intrinsics.append("ip_address")
    else:
        pass

    if "email" not in lead:
        valid = False
        missing_intrinsics.append("email")
    else:
        pass

    if "phone" not in lead:
        valid = False
        missing_intrinsics.append("phone")
    else:
        pass

    if "phone2" not in lead:
        valid = False
        missing_intrinsics.append("phone2")
    else:
        pass

    if "address" not in lead:
        valid = False
        missing_intrinsics.append("address")
    else:
        pass

    if "city" not in lead:
        valid = False
        missing_intrinsics.append("city")
    else:
        pass

    if "state" not in lead:
        valid = False
        missing_intrinsics.append("state")
    else:
        pass

    if "zip" not in lead:
        valid = False
        missing_intrinsics.append("zip")
    else:
        pass

    if "dob" not in lead:
        valid = False
        missing_intrinsics.append("dob")
    else:
        pass

    if "source" not in lead:
        valid = False
        missing_intrinsics.append("source")
    else:
        pass

    if "vertical" not in lead and "verticals" not in lead:
        valid = False
        missing_intrinsics.append("vertical or verticals")
    else:
        pass

    if "fields" not in lead:
        valid = False
        missing_intrinsics.append("fields")
    else:
        pass

    return valid, missing_intrinsics


def validate_lead_fields(lead_fields,required_fields_list):

    for field in lead_fields:
        field_id = int(field["field_id"])

        try:
            if field_id in required_fields_list:
                required_fields_list.remove(field_id)
        except:
            return False

    if len(required_fields_list) > 0:
        return False
    else:
        return True


def validate_answers(database,lead_fields):
    wrong_answers = []
    for field in lead_fields:
        field_id = field["field_id"]

        is_keyed = database.is_keyed(field_id)
        if is_keyed:
            answer_id = field["answer_id"]

            answer_key = database.get_answer_key(field_id)
            #print(answer_key)
            multi_answer_capable = database.is_multi_answer_field(field_id)

            if type(answer_id) is list:
                if multi_answer_capable:
                    for answer in answer_id:
                        if not answer_lookup_passes(answer, answer_key):
                            wrong_answers.append(field_id)
                            break
                else:
                    wrong_answers.append(field_id)
            else: #int answer_id
                if not answer_lookup_passes(answer_id,answer_key):
                    wrong_answers.append(field_id)
        else:
            try:
                answer = field["answer"]
            except:
                wrong_answers.append(field_id)
                break

    if len(wrong_answers) > 0:
        return False, wrong_answers
    else:
        return True, wrong_answers


def answer_lookup_passes(answer_id,answer_key):
    for answer in answer_key:
        try:
            if int(answer_id) == answer["answer_id"]:
                return True
        except:
            return False
    return False