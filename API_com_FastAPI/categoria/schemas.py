from typing import Annotated
from pydantic import Field
from API_com_FastAPI.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome do categoria', example='Scale', max_length=10)]
    