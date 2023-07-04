from typing import List, Optional

from pydantic import BaseModel

from .Good import Good


class BaseUser(BaseModel):
    aopsid: str = ""
    city: str = ""


class GoodsRecUser(BaseUser):
    cart: Optional[List[str]] = []


class MyOrderCenterRecUser(BaseUser):
    history_goods: Optional[List[str]] = []
