import simplejson as json
import uuid
import psycopg2
import requests

from datetime import date

# Example bulk import script to import users from an existing table into FusionAuth using the bulk import API
#
# Setup
# 1. Create a FusionAuth application, make note of the application Id.
#
# 2. Add the following roles to the application
#    - user
#
# 3. Add an API key if you don't already have one - FusionAuth --> Settings --> API Keys
#    - It must at least have [POST] permission to /api/user/import
#
# 4. Update the configurable parameters below.

# Start - Configurable parameters
db_name = "application"
db_user = "dev"
db_table = "users"

api_uri = "http://localhost:9011/api/user/import"
api_headers = {
    'Authorization': 'api-key',
    'Content-Type': 'application/json'
}
application_id = "1141e0b8-95e6-402a-ac6f-0a0449485b3c"
# End - Configurable parameters

# Connect to db
conn = psycopg2.connect("dbname=%s user=%s" % (db_name, db_user))
cur = conn.cursor()

# Retrieve all  and assign them to 'result'
cur.execute("SELECT * from %s" % db_table)
result = cur.fetchall()


# Example Table definition, modify to match yours
# --------------------
# 0  id
# 1  password   [ scheme | factor | salt | hash ]
# 2  last_login
# 3  username
# 4  first_name
# 5  last_name
# 6  email
# 7  active
# 8  created
# 9  last_modified
# 10  date_of_birth
# 11  parent_id

# Build JSON Body
request = {'users': []}
for index, row in enumerate(result):
    schema = row[1].split("$")
    encryption_scheme = "salted-pbkdf2-hmac-sha256" if schema[0] == "pbkdf2_sha256" else schema[0]

    user = {
        'id': uuid.UUID(int=row[0]),
        'active': row[7],
        'encryptionScheme': encryption_scheme,
        'factor': schema[1],
        'salt': schema[2],
        'password': schema[3],
        'email': row[6],
        'username': row[3],
        'firstName': row[4],
        'lastName': row[5],
        'birthDate': row[10],
        'registrations': [{
            'applicationId': application_id,
            'roles': ['user']
        }],
    }

    # prune empty properties
    user = dict((k, v) for k, v in user.iteritems() if v is not None and v != "")
    request['users'].append(user)


# Custom Encoder to handle UUID and date
def custom_encoder(obj):
    if isinstance(obj, uuid.UUID):
        return str(obj)
    if isinstance(obj, date):
        return str(obj)


# Build Json Request
json_data = json.dumps(request, default=custom_encoder)

# Make the API call to bulk import
response = requests.post(api_uri, data=json_data, headers=api_headers)
print "API Response [%d]" % response.status_code

if response.status_code == 400:
    print 'Error Response: '
    print response.json()
