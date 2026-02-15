from sqlalchemy import Column, String, Numeric, BigInteger
from app.db.database import Base

class Coin(Base):
    __tablename__ = 'coins'
    
    id = Column(String, primary_key = True, index = True)
    name = Column(String, nullable = False)
    symbol = Column(String, nullable = False)
    price = Column(Numeric(precision = 18, scale = 8), nullable = False)
    market_cap = Column(BigInteger, nullable = False)
    
    def __repr__(self) -> str:
        return (
            f"(id={self.id}, "
            f"(name={self.name})"
            f"symbol={self.symbol}, "
            f"price={self.price}, "
            f"market_cap={self.market_cap})"
        )
    