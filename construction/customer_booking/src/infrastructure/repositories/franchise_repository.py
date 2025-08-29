from typing import Dict, List, Optional
from ...domain.entities.franchise import Franchise

class FranchiseRepository:
    def __init__(self):
        self._franchises: Dict[str, Franchise] = {}
    
    def save(self, franchise: Franchise) -> None:
        self._franchises[franchise.id] = franchise
    
    def get_by_id(self, franchise_id: str) -> Optional[Franchise]:
        return self._franchises.get(franchise_id)
    
    def get_all_active(self) -> List[Franchise]:
        return [f for f in self._franchises.values() if f.is_active]