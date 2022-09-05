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
    geo_obj = {
        "type": "FeatureCollection",
        "features":[]
    }
    for i in jobj:
        coordinates = []
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": []
            },
            "properties":{}
        }
        # パラメータが1つ以上存在する場合
        if len(params) > 1:
            for p in params:
                if i[p] is not None:
                    print("OK")
                    break
                else:
                    print("NG")
        # パラメータが1つの場合
        else:
            param = params[0]
            coordinates = get_coordinates(i.get(param))
            print(coordinates)
            feature["geometry"]["coordinates"] = coordinates
        feature["properties"] = i
        geo_obj["features"].append(feature)
    return geo_obj


"""
    座標を取得する
    経度、緯度の順番にし数値の配列に変換する
"""


def get_coordinates(items):
    try:
        str_coordinates = items.split(",")
        coordinates = [float(i) for i in str_coordinates]
        # 降順にソートする(経度が先頭に来る)
        sorted_list = sorted(coordinates, reverse=True)
        return sorted_list
    except ValueError as e:
        print(e)
        return False


def output_json(geo_obj):
    filename = input("Save filename:")
    with open("./" + filename, encoding="UTF-8"):
        pass


if __name__ == "__main__":
    path = input("filepath:")
    params = input("座標パラメータ名(スペース区切り):").split()
    jobj = open_json(path)
    geojson = create_geojson(jobj, params)

    print(j)
