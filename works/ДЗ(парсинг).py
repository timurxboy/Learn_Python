class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        
    @classmethod
    def from_string(cls, str_to_parse):
        first_name, last_name, salary = str_to_parse.split('-')
        return cls(first_name, last_name, int(salary))