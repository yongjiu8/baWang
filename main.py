import base64
import datetime
import hashlib
import json
import os
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote, unquote

from curl_cffi import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import execjs
from tqdm import tqdm


def printf(text):
    ti = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(f'[{ti}]: {text}')
    sys.stdout.flush()


def getFileContent(path):
    if os.path.exists(path) and os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    else:
        raise Exception(f'无法找到文件：{path}')


def generate_random_str(randomlength=16):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def md5(content):
    md = hashlib.md5()
    md.update(content.encode())
    return md.hexdigest()

def getNowTimeStr():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def getTimestamp():
    return str(round(time.time() * 1000))

def compareTime(startTime, endTime):
    time_format = "%Y-%m-%d %H:%M:%S"
    datetime1 = datetime.datetime.strptime(startTime, time_format).timestamp()
    datetime2 = datetime.datetime.strptime(endTime, time_format).timestamp()
    if datetime2 >= datetime1:
        return True
    return False

def compareTimeSub(startTime, endTime):
    time_format = "%Y-%m-%d %H:%M:%S"
    datetime1 = datetime.datetime.strptime(startTime, time_format)
    datetime2 = datetime.datetime.strptime(endTime, time_format)
    return round(datetime1.timestamp()) - round(datetime2.timestamp())

def aes_encrypt(content, key='', iv=''):
    key = key.encode('utf-8')
    iv = iv.encode('utf-8')
    content = pad(content.encode('utf-8'), AES.block_size)
    cipher = AES.new(key=key, iv=iv, mode=AES.MODE_CBC)
    res = cipher.encrypt(content)
    return base64.b64encode(res).decode('utf-8')

def aes_decrypt(content, key='', iv=''):
    key = key.encode('utf-8')
    iv = iv.encode('utf-8')
    content = base64.b64decode(content)
    cipher = AES.new(key=key, iv=iv, mode=AES.MODE_CBC)
    res = cipher.decrypt(content)
    res = unpad(res, AES.block_size)
    return res.decode('utf-8')


def run(userId, userToken, userKey, userIv, userVersion, storeId, activityId, keyWords):
    ip_address = '123.123.' + str(random.randint(1, 254))+'.' + str(random.randint(1, 254))
    head = {
        "qm-user-token": userToken,
        "store-id": storeId,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11275",
        "content-type": "application/json",
        "qm-from": "wechat",
        "accept": "v=1.0",
        "qm-trace-store-id": storeId,
        "xweb_xhr": "1",
        "qm-from-type": "catering",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://servicewechat.com/wxafec6f8422cb357b/201/page-frame.html",
        'X-Forwarded-For': ip_address,
        'X-Real-IP': ip_address
    }
    timestamp = getTimestamp()
    signature = md5(
        f'activityId={activityId}&sellerId={storeId}&timestamp={timestamp}&userId={userId}&key={"".join(reversed(activityId))}')
    enData = {"activityId": activityId, "keyWords": keyWords, "qzGtd": "", "gdtVid": "",
              "appid": "wxafec6f8422cb357b", "timestamp": timestamp,
              "signature": signature.upper()}
    enDataStr = json.dumps(enData, ensure_ascii=False, separators=(",", ":"))
    dataEnCode = aes_encrypt(enDataStr, userKey, userIv)
    requestData = {"activityId": activityId, "keyWords": keyWords, "qzGtd": "", "gdtVid": "",
                   "appid": "wxafec6f8422cb357b", "timestamp": timestamp,
                   "signature": signature.upper(),
                   "data": dataEnCode,
                   "version": int(userVersion)}
    requestData = json.dumps(requestData, separators=(",", ":"))
    callJs = execjs.compile(getFileContent('./type.js'))
    type1475 = callJs.call('postRequest', requestData)
    res = requests.post("https://miniapp.qmai.cn/web/cmk-center/receive/takePartInReceive?type__1475="+type1475,
                  headers=head, data=requestData)
    printf(res.text)

def main(storeId, activityId, keywords):
    for userInfo in users:
        if userInfo == '':
            printf(f'用户信息为空 跳过...')
            continue
        try:
            userArry = userInfo.split('----')
            if len(userArry) != 5:
                printf(f'用户信息填写错误 跳过...')
                continue
            userId = userArry[0]
            userToken = userArry[1]
            userKey = userArry[2]
            userIv = userArry[3]
            userVersion = userArry[4]
            printf(f'开始用户：'+userId)
            for i in range(maxCount):
                for keyword in keywords:
                    pool.submit(run, userId, userToken, userKey, userIv, userVersion, storeId, activityId, keyword)
                    time.sleep(intervalTime)
        except Exception as e:
            printf(f'运行异常：{e}')


if __name__ == '__main__':
    config = {}
    try:
        config = json.loads(getFileContent('./config.json'))
    except Exception as e:
        printf(f'加载配置文件异常：{str(e)}')
        os.system('pause')
    usersInfo = getFileContent('./users.txt')
    users = usersInfo.split("\n")
    storeId = config['storeId']
    activityId = config['activityId']
    keywords = config['keywords']
    maxCount = config['maxCount']
    intervalTime = config['intervalTime']
    startTime = config['startTime']
    pool = ThreadPoolExecutor(max_workers=20)
    printf(f'开始时间：{startTime}')

    sends = compareTimeSub(startTime, getNowTimeStr())
    for i in tqdm(range(sends + 10), colour="green", desc="等待开始时间"):
        if compareTime(startTime, getNowTimeStr()):
            main(storeId, activityId, keywords)
            break
        time.sleep(1)

    if sends < 0:
        main(storeId, activityId, keywords)
    #防止退出
    while True:
        time.sleep(1)
