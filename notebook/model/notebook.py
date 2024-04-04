from dataclasses import dataclass, field
from datetime import datetime
from random import random


@dataclass
class Note:
     code:int
     title:str
     text:str
     importance:str

     creation_date: datetime = field(default_factory=datetime.now)
     tags: list[str] = field(default_factory=list)

     HIGH: str = "HIGH"
     MEDIUM: str = "MEDIUM"
     LOW: str = "LOW"


    def __str__(self) -> str:
        return f"Code: {self.code}\nCreation date: {self.creation_date}\n{self.title}: {self.text}"

    def add_tag (self, tag:str):
        if tag not in self.tags:
            self.tags.append(tag)

@dataclass
class Notebook:
    notas = dict()

    def add_note (self, title:str, text:str, importance:str):
        nota = Note(title, text, importance)
        codigo = random.randint(1000,9999)
        self.notas[codigo] = nota
        return codigo

    def important_notes (self) -> list[Note]:
        result = []
        for codigo in self.notas:
            if self.notas[codigo].importance == "HIGH" or self.notas[codigo].importance == "MEDIUM":
                result.append(self.notas[codigo])
        return result


    def tags_notes_count (self) -> dict[str, int]:
        tags = {}
        for codigo in self.notas:
            for tag in self.notas[codigo].tags:
                tags[tag] += 1
        return tags


