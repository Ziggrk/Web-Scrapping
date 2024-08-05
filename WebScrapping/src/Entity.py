class Entity:
    def __init__(self, name, address, entity_type, programs, entity_list, score):
        self.name = name
        self.address = address
        self.entity_type = entity_type
        self.programs = self.split_programs(programs)
        self.entity_list = entity_list
        self.score = score

    def split_programs(self, programs):
        return programs.split('; ') if programs else []

    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "entity_type": self.entity_type,
            "programs": self.programs,
            "entity_list": self.entity_list,
            "score": self.score
        }