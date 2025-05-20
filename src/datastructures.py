class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

        # Miembros iniciales
        self.add_member({
            "first_name": "John",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        })
        self.add_member({
            "first_name": "Jane",
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        })
        self.add_member({
            "first_name": "Jimmy",
            "age": 5,
            "lucky_numbers": [1]
        })

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        self._members = [m for m in self._members if m["id"] != id]

    def get_member(self, id):
        return next((m for m in self._members if m["id"] == id), None)

    def get_all_members(self):
        return self._members
