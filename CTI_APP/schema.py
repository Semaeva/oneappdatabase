from ninja import Schema
from typing import Optional
from pydantic import Field, constr
import datetime


class BlackListURLOut(Schema):
    id: int
    url_source: Optional[str]
    attack_date: int = Field(..., title="Год появления атаки", ge=1900, le=datetime.datetime.now().year)


class BlackListURLPost(Schema):
    url_source: str = None
    attack_date: int = Field(..., title="Год появления атаки", ge=1900, le=datetime.datetime.now().year)


class BlackListIPOut(Schema):
    id: int
    ip_source: str
    attack_date: int = Field(..., title="Год появления атаки", ge=1900, le=datetime.datetime.now().year)
    country_source: str


class BlackListIPIn(Schema):
    ip_source: str
    attack_date: int = Field(..., title="Год появления атаки", ge=1900, le=datetime.datetime.now().year)
    country_source: constr(max_length=50)


class CtiPostSchema(Schema):
    cve: Optional[str]
    signature: str
    description: str
    response_measures: str


class CtiOutSchema(CtiPostSchema):
    id: int