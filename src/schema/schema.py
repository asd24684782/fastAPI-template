from pydantic import BaseModel
from typing import List

class profileSchema(BaseModel):
    uuid                : str
    version             : str
    name                : str
    maxSafeCount        : int
    maxCount            : int
    cameras             : List[str]