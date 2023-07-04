from dataclasses import dataclass, field
from typing import List, Optional
from .Good import Good

@dataclass
class BaseUser:
    aopsid: str=''
    city: str=''



@dataclass
class GoodsRecUser(BaseUser):
    cart: Optional[List[str]] = field(default_factory=list)



@dataclass
class MyOrderCenterRecUser(BaseUser):
    history_goods: Optional[List[str]] = field(default_factory=list)


