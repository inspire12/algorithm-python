from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class User:
    id: int
    name: str
    email: str

u = User(1, "Neo", "neo@matrix.io")
print(u)