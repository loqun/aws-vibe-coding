from typing import List
from ...domain.events.base_event import BaseEvent
from .event_store import EventStore

class EventPublisher:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store
    
    def publish_events(self, events: List[BaseEvent]) -> None:
        # Mock SQS publishing - just store events
        self.event_store.save_events(events)
        print(f"Published {len(events)} events to SQS")