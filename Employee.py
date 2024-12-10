"""Employé de base"""

class Employee:
    """Employé de base"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self) -> str:
        """email du pey"""
        return f"{self.first}.{self.last}@mymail.com"
    
    @property
    def fullname(self) -> str:
        """nom du gars"""
        return f"{self.first} {self.last}"
    
    def __repr__(self) -> str:
        return f"Employee : {self.fullname}, {self.pay}"