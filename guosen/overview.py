import json
import requests


def get_overview_data(symbol):
    url = "http://zxtp.guosen.com.cn:7615/TQLEX?Entry=CWServ.tdxf10_gg_zxts"
    payload = json.dumps({
        "Params": [
            symbol,
            "gsgy",
            ""
        ]
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    text = response.text
    result = json.loads(text)

    # roe
    result_sets = result["ResultSets"][0]
    result_items = result_sets["Content"]

    if len(result_items) == 0:
        return None
    last_item = result_items[0]
    roe = last_item[1]

    # 行业
    result_sets = result["ResultSets"][1]
    result_items = result_sets["Content"]

    if len(result_items) == 0:
        return None
    last_item = result_items[0]
    industry1 = last_item[1]
    industry2 = last_item[2]

    # revenue (营收), revenue_growth (营收同比), profit_growth (归母净利润同比), gross_profit (毛利率), eps (每股收益)
    result_sets = result["ResultSets"][4]
    result_items = result_sets["Content"]

    if len(result_items) == 0:
        return None
    last_item = result_items[0]
    eps = last_item[0]
    revenue = last_item[2]
    gross_profit = last_item[4]
    revenue_growth = last_item[7]
    profit_growth = last_item[8]

    # pb, pe
    result_sets = result["ResultSets"][6]
    result_items = result_sets["Content"]

    if len(result_items) == 0:
        return None
    last_item = result_items[0]
    pe = last_item[0]
    pb = last_item[2]

    p_item = {
        "eps": eps,
        "roe": roe,
        "pe": pe,
        "pb": pb,
        "revenue": revenue,
        "gross_profit": gross_profit,
        "revenue_growth": revenue_growth,
        "profit_growth": profit_growth,
        "industry1": industry1,
        "industry2": industry2
    }
    return p_item


if __name__ == "__main__":
    # item = get_overview_data("000991")
    item = get_overview_data("300073")
    print(item)
    pass
