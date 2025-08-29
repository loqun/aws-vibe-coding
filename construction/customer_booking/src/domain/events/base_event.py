from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

@dataclass
class BaseEvent:
    event_id: str = None
    timestamp: datetime = None
    
    def __post_init__(self):
        if not self.event_id:
            object.__setattr__(self, 'event_id', str(uuid4()))
        if not self.timestamp:
            object.__setattr__(self, 'timestamp', datetime.utcnow())