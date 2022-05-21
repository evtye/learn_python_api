# #5
# import json
# json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
# obj = json.loads(json_text)
#
# print(obj["messages"][1]['message'])

#6
# import requests
#
# response = requests.get("https://playground.learnqa.ru/api/long_redirect")
# print(len(response.history))
# print(response.url)

# #7
# import requests
#
# params_list = ["GET", "POST", "PUT", "DELETE"]
# url1 = "https://playground.learnqa.ru/ajax/api/compare_query_type"
# payload = {"method": "POST"}
#
# for i in range(len(params_list)):
#     payload["method"] = params_list[i]
#     query_types = [
#         requests.get(url=url1, params=payload),
#         requests.post(url=url1, data=payload),
#         requests.put(url=url1, data=payload),
#         requests.delete(url=url1, data=payload)]
#     for j in range(len(query_types)):
#         response = query_types[j]
#         print(j+1, response.text, params_list[i])


# #8
# import requests
# from time import sleep
# url = "https://playground.learnqa.ru/ajax/api/longtime_job"
# response = requests.get(url)
#
# parsed_response = response.json()
# not_ready_response = requests.get(url, params={"token": parsed_response["token"]})
# print(not_ready_response.text)
#
# sleep(parsed_response["seconds"])
#
# ready_response = requests.get(url, params={"token": parsed_response["token"]})
# print(ready_response.text)

#9
# import requests
#
# payload = {"login": "super_admin", "password": "rer"}
# passwords_list = ['123456789', 'qwerty', 'password', '1234567', 'welcome', '12345678', '12345', 'iloveyou', '111111', '123123',
# 'abc123', 'qwerty123', '1q2w3e4r', 'admin', 'qwertyuiop', '654321', '555555', 'lovely', '7777777', '888888',
# 'princess', 'dragon', 'password1', '123qwe']
#
# for i in passwords_list:
#     payload["password"] = i
#     response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
#     cookie_values = response.cookies.get("auth_cookie")
#
#     cookie_payload = {"auth_cookie": cookie_values}
#     auth_result = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookie_payload)
#
#     if auth_result.text != "You are NOT authorized":
#         print(f'password: {i}\n{auth_result.text}')
#         break
