from pydantic import BaseModel, Field
from uuid import UUID


class OrmModel(BaseModel):
    class Config:
        orm_mode = True


class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username between 6 and 20 chars")


class AssetAdd(BaseModel):
    ticker: str = Field(
        description="unique combination of letters that identifies a financial"
        " asset, such as a stock, bond, or mutual fund "
    )


class AssetInfoBase(BaseModel):
    ticker: str = Field(description="The stock symbol.")
    name: str = Field(description="The company's name.")
    country: str = Field(description="The company's headquarters country")
    sector: str = Field(description="The company's main field of operations. ")


class AssetInfoUser(AssetInfoBase):
    units: float


class AssetInfoPrice(AssetInfoBase):
    current_price: float = Field(description="The stock's current price")
    currency: str = Field(description="The symbol for currency.")
    today_low_price: float = Field(
        description="The stock's lowest registered price today."
    )
    today_high_price: float = Field(
        description="The stock's highest registered price today."
    )
    open_price: float = Field(
        description="The stock's latest registered opening price."
    )
    closed_price: float = Field(
        description="The stock's latest registered closing price."
    )
    fifty_day_price: float = Field(
        description="The stock's average price over the last fifty days. "
    )
    price_evolution: str = Field(
        description="The stock's price evolution over the last 24 hours."
    )


class UserInfo(OrmModel):
    id: UUID = Field(description="Unique user ID")
    username: str = Field(
        description="Alphanumeric username between 6 and 20 characters."
    )
    stocks: list[AssetInfoBase] = Field(
        description="A list of stocks associated to the user."
    )
