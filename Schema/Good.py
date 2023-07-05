from pydantic import BaseModel, ConfigDict


class Good(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str = ""
    title: str = ""
    price: float = -1.0
    inventory: int = -1
    city: str = ""
    cat4: str = ""
    cat3: str = ""
    label: str = ""
    brand: str = ""
    channel: str = ""
    short_name: str = ""
    jigou: str = ""

    def get(self, key, default_value):
        try:
            return getattr(self, key)
        except AttributeError:
            return default_value

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
