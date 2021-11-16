__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"

"""
Exercise: Refactoring
Code to refactor is located as line commands at the end
"""


def main():
    # adding Specialists
    electricien_alice = Electricien("Alice Aliceville", 10.05)
    electricien_peter = Electricien("Peter Aliceville", 11.05)
    electricien_bob = Electricien("Bobby Bobsville", 13.00)
    electricien_tom = Electricien("Tom Aliceville", 20.05)
    electricien_henk = Electricien("Henk Aliceville", 10.15)
    painter_bob = Painter("Bob Bobsville", 8.75)
    painter_aaron = Painter("Aaron Bobsville", 8.75)
    painter_robert = Painter("Robert Bobsville", 8.15)
    plumber_graig = Plumber("Craig Craigsville", 12.35)
    plumber_thomas = Plumber("Thomas Craigsville", 12.15)
    # adding HomeOwners
    home_owner_alfred = HomeOwner("Alfred Alfredson", "Alfredslane 123")
    home_owner_bert = HomeOwner("Bert Bertson", "Bertslane 231")
    home_owner_candice = HomeOwner("Candice Candicedottir", "Candicelane 312")

    # testing
    test = home_owner_bert.needs(["electricien", "plumber"])
    print(test)


class HomeOwner:
    def __init__(self, owner_name: str, address: str):
        self.owner_name = owner_name
        self.address = address

    def needs(self, specialities: list, cheapest: bool = True) -> list:
        specialist_list = []
        if type(specialities) == list:
            for speciality in specialities:
                if cheapest:
                    specialist_list.append(Specialist.get_cheapest(speciality))
                else:
                    specialist_list.append(Specialist.get_all_specialists(speciality))
        else:
            raise TypeError("Argument 'specialities' must be a list!")
        return specialist_list


class Specialist:
    all_specialists = []
    all_specialities = set()

    def __init__(self, specialist_name: str, profession: str, wage_per_hour: float):
        if type(specialist_name) != str:
            raise TypeError("Name of specialist must be a string!")
        else:
            self.specialist_name = specialist_name
        self.profession = profession
        if type(wage_per_hour) == int:
            wage_per_hour = float(wage_per_hour)
        if type(wage_per_hour) != float:
            raise TypeError(f"The wage per hour of {self.specialist_name} should be a float!")
        else:
            self.hour_price = wage_per_hour
        self.all_specialists.append((specialist_name, profession, wage_per_hour))
        self.all_specialities.add(profession)

    @classmethod
    def get_specialities_sorted(cls, set_desc=False):
        sort_list = list(Specialist.all_specialities)
        sort_list.sort(reverse=set_desc)
        return sort_list

    @classmethod
    def get_all_specialists(cls, speciality: str):
        specialist_list = []
        for specialist in Specialist.all_specialists:
            if specialist[1] == speciality:
                specialist_list.append(specialist)
        return specialist_list

    @classmethod
    def get_cheapest(cls, speciality: str):
        lowest_wage = 0.0
        speciality_list = []
        if speciality not in Specialist.all_specialities:
            raise ValueError(f"{speciality} is not in the list of specialities!")
        for item in Specialist.all_specialists:
            if item[1] == speciality:
                if lowest_wage == 0.0:
                    speciality_list.append((item[0], item[2]))
                    lowest_wage = item[2]
                elif lowest_wage > item[2]:
                    speciality_list.clear()
                    speciality_list.append((item[0], item[2]))
                    lowest_wage = item[2]
                elif lowest_wage == item[2]:
                    speciality_list.append((item[0], item[2]))
                    lowest_wage = item[2]
        return speciality_list


class Electricien(Specialist):
    def __init__(self, specialist_name: str, wage_per_hour: float):
        super().__init__(specialist_name, "electricien", wage_per_hour)


class Plumber(Specialist):
    def __init__(self, specialist_name: str, wage_per_hour: float):
        super().__init__(specialist_name, "plumber", wage_per_hour)


class Painter(Specialist):
    def __init__(self, specialist_name: str, wage_per_hour: float):
        super().__init__(specialist_name, "painter", wage_per_hour)


if __name__ == "__main__":
    main()


# alice_name = "Alice Aliceville"
# alice_profession = "electrician"
# bob_name = "Bob Bobsville"
# bob_profession = "painter"
# craig_name = "Craig Craigsville"
# craig_profession = "plumber"

# alfred_name = "Alfred Alfredson"
# alfred_address = "Alfredslane 123"
# alfred_needs = ["painter", "plumber"]
# bert_name = "Bert Bertson"
# bert_address = "Bertslane 231"
# bert_needs = ["plumber"]
# candice_name = "Candice Candicedottir"
# candice_address = "Candicelane 312"
# candice_needs = ["electrician", "painter"]

# alfred_contracts = []
# for need in alfred_needs:
#     if need == alice_profession:
#         alfred_contracts.append(alice_name)
#     elif need == bob_profession:
#         alfred_contracts.append(bob_name)
#     elif need == craig_profession:
#         alfred_contracts.append(craig_name)

# bert_contracts = []
# for need in bert_needs:
#     if need == alice_profession:
#         bert_contracts.append(alice_name)
#     elif need == bob_profession:
#         bert_contracts.append(bob_name)
#     elif need == craig_profession:
#         bert_contracts.append(craig_name)

# candice_contracts = []
# for need in candice_needs:
#     if need == alice_profession:
#         candice_contracts.append(alice_name)
#     elif need == bob_profession:
#         candice_contracts.append(bob_name)
#     elif need == craig_profession:
#         candice_contracts.append(craig_name)

# print("=======================================================================")
# print("Alfred's contracts:", alfred_contracts)
# print("Bert's contracts:", bert_contracts)
# print("Candice's contracts:", candice_contracts)
# print("=======================================================================")
# print("Output:")
# print("Alfred's contracts: ['Bob Bobsville', 'Craig Craigsville']")
# print("Bert's contracts: ['Craig Craigsville']")
# print("Candice's contracts: ['Alice Aliceville', 'Bob Bobsville']")
# print("=======================================================================")
