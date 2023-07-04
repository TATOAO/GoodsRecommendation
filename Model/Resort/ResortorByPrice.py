
from typing import List
from Schema import Good
from BaseResort import BaseResort

class ResortorByPrice(BaseResort):
    def resort_by_price(self, goods_list: List[Good]):
        return self.sortting(goods_list, 'price')


