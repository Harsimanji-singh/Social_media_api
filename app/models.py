from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
import datetime
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    type_annotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True)
    }


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    detail: Mapped[str] = mapped_column(nullable=False)
    published: Mapped[bool] = mapped_column(server_default='True')
    created_At: Mapped[datetime.datetime] = mapped_column(
        nullable=False, server_default=text('now()'))
    user_id: Mapped[int] = mapped_column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    created_At: Mapped[datetime.datetime] = mapped_column(
        nullable=False, server_default=text('now()'))


class Vote(Base):
    __tablename__ = "votes"
    user_id: Mapped[int] = mapped_column(ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)
