from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserEdit(BaseCase):
    def test_edit_just_crated_user(self):
        # Registration
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post('/user/', data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.asset_json_has_key(response1, 'id')

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        # Login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post('/user/login', data=login_data)

        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # Edit
        new_name = 'dimis143'
        response3 = MyRequests.put(
            f'/user/{user_id}',
            cookies={'auth_sid': auth_sid},
            headers={'x-csrf-token': token},
            data={'firstName': new_name}
        )

        Assertions.assert_status_code(response3, 200)

        # GET
        response4 = MyRequests.get(
            f'/user/{user_id}',
            cookies={'auth_sid': auth_sid},
            headers={'x-csrf-token': token}
        )

        Assertions.assert_json_value_by_name(response4, 'firstName', new_name,
                                             "Wrong user name after edit")
