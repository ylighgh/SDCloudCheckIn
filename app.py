#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from happy_python import HappyLog
from config import UserList, login_url, headers, check_in_url

hlog = HappyLog.get_instance()


def check_in(username: str, passwd: str) -> None:
    session = requests.session()
    session.post(login_url, headers=headers, data={'email': username, 'passwd': passwd})
    resp = session.post(check_in_url)
    if resp.status_code == 200:
        hlog.info(f"用户{username}签到成功！")


def main():
    for username, passwd in UserList.items():
        check_in(username, passwd)


if __name__ == '__main__':
    main()
