from myproject.hospital.users import Patient
from myproject.hospital.apikey import ApiKey


def auth(obj):
    username = obj.session.get('username')
    api_key = obj.session.get('api_key')
    is_auth = True
    context = {}
    try:
        puser = Patient.objects.get(user__username = username)
        apk = ApiKey.objects.get(user=puser, api_key=api_key)
    except ApiKey.DoesNotExist:
        is_auth = False
        context = {'error': "User not  found with given username"}
    except ApiKey.DoesNotExist:
        is_auth = False
        context ={"error": "Apikey does not match"}
    else:
        context = {
            "name": "{} {}".format(puser.user.first_name, puser.user.last_name)
        }
    return is_auth, context