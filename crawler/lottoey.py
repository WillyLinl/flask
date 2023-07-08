import requests
from bs4 import BeautifulSoup




# date=main.find('span').text.strip().replace('\xa0',' ')
def get_lottory():
    def get_ball(name):
        main=soup.find(id=f"contents_logo_0{lottory_group['大樂透']}").find_parent('div')
        date=main.find('span').text.strip().replace('\xa0',' ')
        balls=' '.join([ball.text.strip() for ball in main.find_all('div',class_="ball_tx")[6:]])
        ball_red = main.find('div',class_='ball_red')
        if ball_red:
            balls = balls + " 特別號:"+ ball_red.text.strip()
        return date ,balls
    
    lottory_group={
    '威力彩':2,
    '大樂透':4,
    '金彩539':6
    }

    url='https://www.taiwanlottery.com.tw/index_new.aspx'

    datas = {}
    try:

        resp=requests.get(url)
        soup=BeautifulSoup(resp.text,'lxml')
        dollars = {
            dollars.text.strip()

        }
        for name in lottory_group:
            datas[name] = get_ball(name)
    except Exception as e:
        print(e)
    return datas

print(get_lottory())