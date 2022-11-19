import jwt

from db.db_helpers import get_id_of_user, user_present
KEY="abiraj"

def genToken(data):
    token = jwt.encode(
        payload=data,
        key=KEY
    )
    return token

def extractPayload(token):
    data = jwt.decode(jwt=token,key=KEY,algorithms=['HS256'])
    return data

def verifyToken(token):
    try:
        data = extractPayload(token)
        if user_present('doctor',(data['email'],data['password'])) :
            return True,get_id_of_user('doctor',(data['email'],data['password']))
        if user_present('patient',(data['email'],data['password'])) :
            return True,get_id_of_user('patient',(data['email'],data['password']))
    except Exception as e:
        return False,-1

# token = (genToken({"name":"abiraj"}))
# print(extractPayload('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYWJpcmFqIn0.L20g9849zJMXT_RJRBWmfrBVSuW5C1P4XXWBwXc2wnY'))