import json


'''
    Jsonファイルを開く
'''


def open_json(path):
    with open(path, encoding="UTF-8") as f:
        j = json.load(f)
        return j

"""
    geojsonにオブジェクトを作成する
"""


def create_geojson(jobj, params):

    for i in jobj:
        if len(params) > 1:
            for p in params:
                if i[p] is not None:
                    print("OK")
                    break
                else:
                    print("NG")
        else:
            param = params[0]
            print(i.get(param))
    return None


"""
    座標を取得する
    経度、緯度の順番にし数値の配列に変換する
"""


def get_coordinate(item):
    str_coordinates = item.split(",")

    return []


if __name__ == "__main__":
    path = input("filepath:")
    params = input("座標パラメータ名(スペース区切り):").split()
    jobj = open_json(path)
    geojson = create_geojson(jobj, params)

    print(j)
