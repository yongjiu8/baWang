# baWang1.0
# 八碗茶鸡猜口令脚本多用户版（原创脚本，仅供学习交流使用，关注忒星不迷路）

# 运行效果
```json
[2024-11-18 17:36:13.905772]: 开始时间：2024-11-18 17:20:00
等待开始时间: 0it [00:00, ?it/s]
[2024-11-18 17:36:13.924648]: 开始用户：1234567890
[2024-11-18 17:36:14.509246]: {"code":1003101,"message":"口令错误,再试一次!","status":false,"trace_id":"1"}
[2024-11-18 17:36:14.583498]: {"code":1003104,"message":"您来晚了，今日奖品已领完","status":false,"trace_id":"2"}
[2024-11-18 17:36:14.914507]: {"code":1003101,"message":"口令错误,再试一次!","status":false,"trace_id":"3"}
[2024-11-18 17:36:15.057375]: {"code":1003104,"message":"您来晚了，今日奖品已领完","status":false,"trace_id":"4"}
[2024-11-18 17:36:15.235423]: {"code":1003101,"message":"口令错误,再试一次!","status":false,"trace_id":"5"}
[2024-11-18 17:36:15.313360]: {"code":1003104,"message":"您来晚了，今日奖品已领完","status":false,"trace_id":"6"}
[2024-11-18 17:36:15.543121]: {"code":1003101,"message":"口令错误,再试一次!","status":false,"trace_id":"7"}
[2024-11-18 17:36:15.739369]: {"code":1003104,"message":"您来晚了，今日奖品已领完","status":false,"trace_id":"8"}
[2024-11-18 17:36:15.963215]: {"code":1003101,"message":"口令错误,再试一次!","status":false,"trace_id":"9"}
[2024-11-18 17:36:16.115454]: {"code":1003104,"message":"您来晚了，今日奖品已领完","status":false,"trace_id":"10"}
[2024-11-18 17:36:16.355730]: {"code":1003101,"message":"口令错误,再试一次!","status":false,"trace_id":"11"}
[2024-11-18 17:36:16.576419]: {"code":1003104,"message":"您来晚了，今日奖品已领完","status":false,"trace_id":"12"}
[2024-11-18 17:36:16.708429]: {"code":1003101,"message":"口令错误,再试一次!","status":false,"trace_id":"13"}
[2024-11-18 17:36:17.005857]: {"code":1003104,"message":"您来晚了，今日奖品已领完","status":false,"trace_id":"14"}
```

# 更新日志
```text
2024-11-18
创建项目 init1.0
```
# 说明
1.安装Python3.8+

2.安装模块命令（cmd执行）

```json
pip install requests curl_cffi pyexecjs tqdm pycryptodome -i https://pypi.doubanio.com/simple/
```

3.设置账号
```text
1.管理员运行账号.exe 点击搜索 电脑打开小程序 进到口令页面 输入口令领取 在点搜索即可获取账号信息
如：
"data":"{"data":"{"encrypt_key":"这里是你的用户key填到users.txt","version":这里是你的用户key版本填到users.txt,"expire_in":2182,"iv":"这里是你的用户iv填到users.txt","create_time":1731921075}","err_no":0}","desc":"","err_msg":"ok","err_no":0,"errorCode":0,"isSuccess":true,"operateCode":0,"scope":"","task_id":282}

{"id":"这里是你的用户id填到users.txt","nickname":"微信用户","username":"微信用户","mobile":"","avatar":null,"unionid":"","openid":"","userNickname":"","requireDefaultNickname":false,"requireDefaultUsername":false,"isSupportLogoff":false,"isAgreeLogoffProtocol":false,"is_open_webank":0,"open_webank_time":0,"entity_card_qty":0,"personal_recommend_setting":1},"storeInfo":{"id":49006,"name":"","logo":"https://images.qmai.cn/s49006/2022/03/07/8dfcb82447277fdffe.png","store_type":66,"service_tel":"400 8788 359","contact_number":"","contact_person":""},"shopInfo":{"id":"","name":""},"userToken":"这里是你的用户token填到users.txt","networkInfo":{"isWeakNet":null},"clientTime":1,"version":"5.41.40","logType":"common","name":"领取动作发生错误之未知code","level":"info","error":{"code":1003101,"message":"口令错误,再试一次!","status":false,"trace_id":"1"}}
users.txt 支持多个号 一行一个 格式为
用户id----用户token----用户key----用户iv----用户key版本
```
4.配置
```json
修改config.json
{
  "activityId": "1063505589269471233", 活动id一般不变
  "storeId": "49006", 任务id一般不变
  "keywords": ["口令1", "好状态随春醒"], 口令可以设置多个按顺序执行
  "maxCount": 20, 一个账号最多执行多少次
  "intervalTime": 0.2, 每次执行间隔0.2秒
  "startTime": "2024-11-18 17:20:00" 开始执行时间 请按此格式填写
}
```
# 启动 (在cmd中执行命令)
```text
python main.py
```

# wx交流群：
![image](https://ma.suv.run/uploads/picture/QRcode/17_d0e8944d9af4dabf92232bb55368394a.png?t=1733124963)
