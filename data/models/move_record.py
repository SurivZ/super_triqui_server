from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, orm

from ..connection import Base


class MoveRecord(Base):
    __tablename__ = "move_record"

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'))
    move_number = Column(Integer, nullable=False)
    player = Column(String(1), nullable=False)  # 'X' o 'O'
    board_index = Column(Integer, nullable=False)  # 0-8
    cell_index = Column(Integer, nullable=False)  # 0-8
    resulted_in_board_win = Column(Boolean, nullable=False)
    resulted_in_board_draw = Column(Boolean, nullable=False)

    game = orm.relationship("Game", backref="moves")

    def __repr__(self) -> str:
        return (f"MoveRecord(game_id={self.game_id}, move_number={self.move_number}, player={self.player}, board_index={self.board_index}, cell_index={self.cell_index}, resulted_in_board_win={self.resulted_in_board_win}, resulted_in_board_draw={self.resulted_in_board_draw})")
