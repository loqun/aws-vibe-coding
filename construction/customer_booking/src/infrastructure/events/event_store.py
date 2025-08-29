from typing import List
from ...domain.events.base_event import BaseEvent

class EventStore:
    def __init__(self):
        self._events: List[BaseEvent] = []
    
    def save_events(self, events: List[BaseEvent]) -> None:
        self._events.extend(events)
    
    def get_all_events(self) -> List[BaseEvent]:
        return self._events.copy()