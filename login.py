import time
import requests


def time_milli():
    return int(time.time() * 1000)


headers = {
    "Host": "172.16.16.16:8090",
    "Connection": "keep-alive",
    "Content-Length": "83",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.56 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "*/*",
    "Origin": "http://172.16.16.16:8090",
    "Referer": "http://172.16.16.16:8090/httpclient.html?u=http://www.gstatic.com/generate_204",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-IN,en-US;q=0.9,en;q=0.8"
}

login_url = "http://172.16.16.16:8090/login.xml"
logout_url = "http://172.16.16.16:8090/logout.xml"


def req_login(username, password, producttype=0):
    payload = {
        'username': username,
        "password": password,
        "a": time_milli(),
        "mode": 191,
        "producttype": producttype
    }
    return requests.post(login_url, data=payload, headers=headers)


def login(username, password, producttype=0):
    try:
        res = req_login(username, password, producttype)
    except requests.exceptions.ConnectionError as ex:
        print("[ConnectionError] Cannot connect to {lurl}.".format(lurl=login_url))
    else:
        pass

def req_logout(username, producttype=0):
    payload = {
        'username': username,
        "a": time_milli(),
        "mode": 191,
        "producttype": producttype
    }
    return requests.post(logout_url, data=payload, headers=headers)




if __name__ == '__main__':
    roll_no = input("Enetr the Username: ")
    password = input("Enter the password: ")
    print(req_login(roll_no, password))


    
