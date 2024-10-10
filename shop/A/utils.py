from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('536772766D6E504B4C6834356C4F615A32346E314F7A594E415545544F4C5568706A595642306A476158303D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'کد تایید شما {code}'
        }
        response = api.sms.send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)



#limit access of user 
class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin