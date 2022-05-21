from dataclasses import dataclass, field
import sre_compile

@dataclass
class JPG:
    src_path: str
    extensions: tuple[str, str] = field(init=False, default=(".jpeg", ".jpg"))

@dataclass
class PDF:
    dest_path: str
    extension: str = field(init=False, default=(".pdf"))
    
def allocate_jpeg(src_path: str) -> JPG:
    return JPG(src_path=src_path)

def allocate_pdf(dest_path: str) -> PDF:
    return PDF(dest_path=dest_path)