import asyncio

from BaseRecall import BaseRecall

from Schema.Good import Good
from typing import List


class RecallerByCategories(BaseRecall):

    async def recall_by_cat4(self, good_list: List[Good], cat4):
        return [good for good in good_list if good.cat4 == cat4]

    async def recall_by_cat3(self, good_list: List[Good], cat3):
        return [good for good in good_list if good.cat3 == cat3]





