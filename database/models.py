from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, create_model


class Affiliation(str, Enum):
    rebel_alliance = "Rebel Alliance"
    empire = "Imperial Empire"


class Character(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    affiliation: Affiliation

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


if __name__ == "__main__":
    data = {
        "id": 123,
        "first_name": "Erik",
        "last_name": "Kvale",
        "affiliation": "Rebel Alliance"
    }
    erik = Character(**data)
    print(erik.id)
    # print(Character.schema_json(indent=2))

