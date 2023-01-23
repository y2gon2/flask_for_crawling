from urllib.request import urlopen
from bs4 import BeautifulSoup


def stock_crawling(code):
    root_url = "https://finance.naver.com/item/main.naver?code="
    url = root_url + code  # 삼성전자
    html = urlopen(url)
    bs_obj = BeautifulSoup(html, "html.parser", from_encoding="cp949")
    # print(bs_obj)

    date1 = bs_obj.find("em", {"class":"date"})
    # print(type(date1))
    # print(date1.text)
    # print(type(date1.text))

    try:
        date = date1.text.replace('.', '/').split()
        date = date[0]
        # print(date)

    except:
        print("해당 코드로 종목찾기에 실패하였습니다. 입력코드를 재확인 해주시기 바랍니다.")
        return {"code": "None"}

    table1 = bs_obj.find("div", {"class":"rate_info"})
    table1 = table1.text.split()
    # print(table1)

    corp_name = table1[0]
    cur_price = int(table1[2].replace(',', ''))

    try:
        prv_price = int(table1[23].replace(',', ''))
        highest_price = int(table1[26][0:len(table1[26])//2].replace(',', ''))
        lowest_price = int(table1[36][0:len(table1[36])//2].replace(',', ''))

    except:
        prv_price = int(table1[21].replace(',', ''))
        highest_price = int(table1[24][0:len(table1[24])//2].replace(',', ''))
        lowest_price = int(table1[34][0:len(table1[34])//2].replace(',', ''))

    # print(lowest_price)

    table2 = bs_obj.find("div", {"class":"aside_invest_info"}).text.split()
    # print(table2)

    try:
        total_stocks = int(table2[12].replace(',', ''))
        fgn_owned = int(table2[21].replace(',', ''))

    except:
        total_stocks = int(table2[11].replace(',', ''))
        fgn_owned = int(table2[20].replace(',', ''))

    # fgn_own_ratio = float(fgn_own) / float(total_stocks)
    # print("외국인 보유 비율: %.2f %%" % (fgn_own_ratio * 100 ))

    # print(per, pbr)

    total_info = {
        "code": code,
        "corp name": corp_name,
        "date": date,
        "privous price": prv_price,
        "current price": cur_price,
        "highest price": highest_price,
        "lowest price": lowest_price,
        "total stocks": total_stocks,
        "foreign owned": fgn_owned,
    }

    return total_info
