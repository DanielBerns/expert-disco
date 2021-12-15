from typing import Dict, Optional
from collections import DefaultDict

class Node:
    def __init__(self, name: str):
        self._name: str = name
        self._attributes: Dict[str, Dict] = DefaultDict(lambda: None)
        
    @property
    def name(self) -> str:
        return self._name

    @property
    def attributes(self) -> Dict[str, Dict]:
        return self._attributes
    
    def assign_attribute(self, key: str, value: Dict[str, str]):
        self.attributes[key]: Dict[str, str] = value
       

class Agent(Node):
    def __init__(self, name: str):
        super.__init__(name)
        self._bag_of_things: Dict[str, Node] = {}
        



class Place(Node):
    def __init__(self, name: str):
        super.__init__(name)
        self._agents: Dict[str, Agent] = {}
        self._neighbours: Dict[str, 'Room'] = {}

    @property
    def neighbours(self) -> Dict[str, 'Room']:
        return self._neighbours

    
class Game:
    def __init__(self):
        pass
