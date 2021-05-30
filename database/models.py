from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class Affiliation(str, Enum):
    rebel_alliance = "Rebel Alliance"
    empire = "Imperial Empire"


class Character(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    affiliation: Affiliation


if __name__ == "__main__":
    data = {
        "id": uuid4(),
        "first_name": "Erik",
        "last_name": "Kvale",
        "affiliation": "Rebel Allianc"
    }
    print(Character(**data))

