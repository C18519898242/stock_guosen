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

    # pb, pe
    result_sets = result["ResultSets"][6]
    result_items = result_sets["Content"]
    last_item = result_items[0]
    pe = last_item[0]
    pb = last_item[2]

    # 行业
    result_sets = result["ResultSets"][1]
    result_items = result_sets["Content"]
    last_item = result_items[0]
    industry1 = last_item[1]
    industry2 = last_item[2]

    p_item = {
        "pe": pe,
        "pb": pb,
        "industry1": industry1,
        "industry2": industry2
    }
    return p_item


if __name__ == "__main__":
    item = get_overview_data("601169")
    print(item)
    pass
