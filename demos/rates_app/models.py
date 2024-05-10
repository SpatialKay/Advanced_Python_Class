from sqlalchemy import Column, Integer, String, Float

from rates_app.database import Base


class ExchangeRate(Base):
    __tablename__ = "exchange_rates"

    id = Column(Integer, primary_key=True)
    market_date = Column(String, nullable=False)
    currency_symbol = Column(String, nullable=False)
    currency_rate = Column(Float, nullable=False)

    def __str__(self) -> str:
        return (
            f"<ExchangeRate Id={self.id}, "
            f"MarketDate={self.market_date}, "
            f"CurrencySymbol={self.currency_symbol}, "
            f"CurrencyRate={self.currency_rate}>"
        )
