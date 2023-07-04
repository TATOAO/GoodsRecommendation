from typing import List
from Schema import Good


class BaseResort():
    def __init__(self):
        pass

    def sortting(self, goods_list: List[Good], key):
        if len(goods_list) == 0:
            return goods_list

        return sorted(goods_list, key=lambda x: x.get(key, 0.0))
