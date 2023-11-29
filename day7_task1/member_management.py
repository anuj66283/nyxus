from error_handling import AlreadyExists, NotExist

class LibraryMember:
    members_list = {}

    @classmethod
    def add_member(cls, member_id, name):
        if member_id in cls.members_list:
            raise AlreadyExists

        rslt = {'name': name}

        cls.members_list[member_id] = rslt


    def update_member(cls, member_id, name):
        if member_id not in cls.members_list:
            raise NotExist

        cls.members_list[member_id]['name'] = name


    @classmethod
    def remove_member(cls, member_id):
        if member_id not in cls.members_list:
            raise NotExist
        
        del cls.members_list[member_id]