from pydantic import BaseModel, Field
from uuid import UUID


# TODO add the field with description, approx half
class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username between 6 and 20 chars")


class AssetAdd(BaseModel):
    ticker: str


class AssetInfoBase(BaseModel):
    ticker: str
    name: str
    country: str

    class Config:
        orm_mode = True


class AssetInfoUser(AssetInfoBase):
    units: float


class AssetInfoPrice(AssetInfoBase):
    current_price: float
    currency: str
    today_low_price: float
    today_high_price: float
    open_price: float
    closed_price: float
    fifty_day_price: float
    price_evolution: str


class UserInfo(BaseModel):
    id: UUID
    username: str
    stocks: list[AssetInfoBase]

    class Config:
        orm_mode = True
