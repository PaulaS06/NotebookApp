from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Note:

     creation_time: datetime = field(default_factory=datetime.now())
     tags: list[str] = field(default_factory = [])

    def __str__(self) -> str:
        return f"Code: { }\nCreation Creation date: {self.creation_time}\nCreation Title: {}"

    def add_tag (self, tag):
        if tag not in self.tags:
            self.tags.append(tag)


class Notebook:
    def __init__(self):
    def add_note (self, nota):



