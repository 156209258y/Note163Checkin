import requests
import time
import json

# 配置cookie和headers
cookies = {
    'YNOTE_LOGIN':'5||1729044419809	',
    'YNOTE_PERS':'v2|cqq||YNOTE||web||-1||1729044126238||220.197.11.93||qq37A745476BB00B6ED27C8E998C0E8786||qKhHYm0LquRYGOMpFh4lERey6MT40MPB0qLnHk50HPS0puPMPyRHYERJK6MPFkLzY0Tuh4Ylh4Om0Jyn4zMkMkf0',
    'YNOTE_CSTK': 'M8NMe4NT',  # 从抓包中获取的CSTK字段
    'YNOTE_SESS': 'v2|-WUBN5I0fBPLhHPSOMYMRpBRMPLRfzGRJFnfOfPMqZ0JFhHwz0HeK0TFRHwunL64RPy0MeBOfgL0lG0LlWnfll0py0HkW6LPyR',  # 从抓包中获取的Session Cookie
}

headers = {
    'User-Agent': 'YouDaoNote/7.0.6 (iPhone; iOS 14.3; Scale/2.00)',
    'Content-Type': 'application/x-www-form-urlencoded',
}

# 签到URL
sign_in_url = 'https://note.youdao.com/yws/mapi/user?method=checkin'

def sign_in():
    # 发送签到请求
    response = requests.post(sign_in_url, headers=headers, cookies=cookies, verify=False)
    if response.status_code == 200:
        result = json.loads(response.text)
        total_space = result['total'] / 1048576  # 总获得空间，单位MB
        gained_space = result['space'] / 1048576  # 本次签到获得空间，单位MB
        sign_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(result['time'] / 1000))

        print(f"[+] 签到成功！当前时间：{sign_time}")
        print(f"[+] 本次签到获得空间：{gained_space} MB")
        print(f"[+] 总共获得空间：{total_space} MB")
    else:
        print(f"[!] 签到失败，状态码：{response.status_code}")
        print(response.text)

if __name__ == '__main__':
    sign_in()
