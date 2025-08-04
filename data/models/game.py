from sqlalchemy import Column, Integer, String, Boolean, BigInteger

from ..connection import Base


class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)
    mode = Column(String(50), nullable=False)
    vs_ai = Column(Boolean, nullable=False)
    ai_level = Column(String(50), nullable=True)
    result = Column(String(10), nullable=False)
    duration_ms = Column(Integer, nullable=False)
    timestamp = Column(BigInteger, nullable=False)
    move_count = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Game(mode={self.mode}, vs_ai={self.vs_ai}, ai_level={self.ai_level}, result={self.result}, duration_ms={self.duration_ms}, timestamp={self.timestamp}, move_count={self.move_count})"
