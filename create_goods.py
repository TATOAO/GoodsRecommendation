goods = [
    {
        "id": "91",
        "name": "Sennheiser Momentum 真无线耳机",
        "first_category": "电子产品",
        "second_category": "音频设备",
        "brand": "Sennheiser",
    },
    {
        "id": "92",
        "name": "Herman Miller Aeron 办公椅",
        "first_category": "家居家装",
        "second_category": "家具",
        "brand": "Herman Miller",
    },
    {
        "id": "93",
        "name": "Adidas Ultra Boost 跑步鞋",
        "first_category": "运动户外",
        "second_category": "运动鞋",
        "brand": "Adidas",
    },
    {
        "id": "94",
        "name": "LAMY 万宝龙钢笔",
        "first_category": "文具",
        "second_category": "书写工具",
        "brand": "LAMY",
    },
    {
        "id": "95",
        "name": "Swatch 手表",
        "first_category": "珠宝首饰",
        "second_category": "手表",
        "brand": "Swatch",
    },
    {
        "id": "96",
        "name": "七匹狼男士皮带",
        "first_category": "服装",
        "second_category": "配饰",
        "brand": "七匹狼",
    },
    {
        "id": "97",
        "name": "Roku 流媒体播放器",
        "first_category": "电子产品",
        "second_category": "家庭娱乐设备",
        "brand": "Roku",
    },
    {
        "id": "98",
        "name": "Lancome 粉底液",
        "first_category": "美妆个护",
        "second_category": "化妆品",
        "brand": "Lancome",
    },
    {
        "id": "99",
        "name": "Gucci 女士香水",
        "first_category": "美妆个护",
        "second_category": "香水",
        "brand": "Gucci",
    },
    {
        "id": "100",
        "name": "Haagen-Dazs 冰淇淋",
        "first_category": "食品",
        "second_category": "冷冻食品",
        "brand": "Haagen-Dazs",
    },
]

from Data.GoodCollections import GoodCollections
from Schema.Good import Good

gc = GoodCollections()

for good in goods:
    g1 = Good(
        id=good["id"],
        title=good["name"],
        cat4=good["second_category"],
        cat3=good["first_category"],
    )

    gc.update_good(g1)

print(gc["100"])
