import uuid
import hashlib

# def generate_api_key():
#     u1 = uuid.uuid4()
#     u2 = uuid.uuid4()
#     u3 = str(u1) + str(u2)
#     u3 = u3.lower()
#     api_key = u3.replace("-","")
#     return str(api_key)


# def generate_vendor_id():
#     u1 = uuid.uuid4()
#     u2 = str(u1)
#     vendor_id = u2.upper()
#     vendor_id = vendor_id.replace("-","")
#     return str(vendor_id)


# def generate_sub_vendor_id():
#     sub_vendor_id = str(uuid.uuid4())
#     sub_vendor_id = sub_vendor_id.upper()
#     sub_vendor_id = sub_vendor_id.replace("-","")
#     return sub_vendor_id


# def generate_lead_id():
#     return str(uuid.uuid4())

# def compute_security_hash(hashing_security):
#     hashed_security = hashlib.sha512(bytes(hashing_security, "utf8"))
#     return hashed_security.hexdigest()