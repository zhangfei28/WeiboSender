import re


def MBP():
    text = "abc🕯️🕯️🕯️123"
    # text = '''#疫情聚合##紧急寻人##呼和浩特#【呼和浩特市发布最详细协查通告！呼和浩特一确诊患者是的姐，急寻接触者！】
# 患者万某某， 女，系出租车（蒙AY1754）驾驶员，目前已被确诊为新型冠状病毒感染肺炎病例。以下是该患者（1月18日-30日）的行动轨迹：1月27日、29日在家休息，其余时间都在运营出租车。该出租车运营期间，现已梳理出利用微信支付138人、支付宝支付4人，共 142人，其余人员使用现金支付，乘客电子支付记录、现金支付人员轨迹及载客里程明细见附件。请广大市民认真核对相关信息，凡在上述时间段内乘坐蒙AY1754出租车的乘客，请务必向当地疾控中心登记，并在家进行居家隔离，自行测量体温。载客里程明细及乘客电子支付记录详细轨迹戳链接 。（人民日报微博） 【转自：https://m.weibo.cn/status/IsCSpnscE?jumpfrom=weibocom 】'''
    r = re.sub(u'[\U00010000-\U0010ffff]', '.', text)
    print(r)


if __name__ == '__main__':
    MBP()
