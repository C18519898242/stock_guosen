import json
import requests


def get_payout(symbol):
    url = "http://zxtp.guosen.com.cn:7615/TQLEX?Entry=CWServ.tdxf10_gg_fhrz"

    payload = json.dumps({
        "Params": [
            symbol,
            "fh"
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    text = response.text
    result = json.loads(text)
    result_sets = result["ResultSets"][0]
    result_items = result_sets["Content"]

    p_item_list = []
    for result_item in result_items:
        date_str = result_item[0]
        p_value = result_item[2]
        p_item = {
            "date": date_str,
            "col": "S" + date_str.replace("-", "").strip(),
            "value": p_value
        }
        p_item_list.append(p_item)
    return p_item_list


if __name__ == "__main__":
    item = get_payout("601169")
    print(item)
    pass
