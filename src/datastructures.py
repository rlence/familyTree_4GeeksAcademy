
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:

    def __init__(self, firstname):
        self.firstname = firstname
        # self.last_name = last_name
        # self.age = age
        # self.lucky_numbers = lucky_numbers

        # example list of members
        self._members = [{
            "id":self._generateId(),
            "first_name": "John",
            "lastname":"Jackson",
            "age":33,
            "lucky_numbers":[7, 13, 22]
        },{
            "id":self._generateId(),
            "first_name": "Jane",
            "lastname":"Jackson",
            "age":35,
            "lucky_numbers":[10, 14, 3]
        },{
            "id":1,
            "first_name": "Jimmy",
            "lastname":"Jackson",
            "age":5,
            "lucky_numbers":[1]
        },]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member["id"] = self._generateId()
        self._members.append(member)
        return 200

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if(member['id'] == id):
                self._members.remove(member)
                return {"done":id}
        return 404

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if(member['id'] == id):
                return member
        return 404
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
