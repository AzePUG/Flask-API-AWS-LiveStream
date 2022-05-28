import uuid
from dataclasses import dataclass, field, asdict
from src.domain.validators import is_jpeg, is_pdf

@dataclass
class JPG:
    code: uuid.UUID
    src_path: str
    extensions: tuple[str, str] = field(init=False, default=(".jpeg", ".jpg"))
    
    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)
    
    def to_dict(self):
        return asdict(self)

@dataclass
class PDF:
    code: uuid.UUID
    dest_path: str
    extension: str = field(init=False, default=(".pdf"))
    
    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)
    
    def to_dict(self):
        return asdict(self)

@is_jpeg
def allocate_jpeg(code: uuid.UUID, src_path: str) -> JPG:
    return JPG(code=code, src_path=src_path)

@is_pdf
def allocate_pdf(code: uuid.UUID, dest_path: str) -> PDF:
    return PDF(code=code, dest_path=dest_path)