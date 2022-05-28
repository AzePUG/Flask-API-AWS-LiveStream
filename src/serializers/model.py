import json
from typing import Any


class PDFJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        try:
            return {"code": str(o.code), "dest_path": o.dest_path, "extension": o.extension}
        except AttributeError:
            return super().default(o)
        
class JPGJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        try:
            return {"code": str(o.code), "src_path": o.src_path, "extensions": f"{list(o.extensions)}"}
        except AttributeError:
            return super().default(o) 
        

class ConvertedJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        try:
            return {
                "converted_from": json.dumps(o.converted_from, cls=JPGJsonEncoder),
                "converted_to": json.dumps(o.converted_to, cls=PDFJsonEncoder),
                "converted_at": str(o.converted_at)
            }
        except AttributeError:
            return super().default(o)