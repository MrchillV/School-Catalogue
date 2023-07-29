class School:

  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, new_numberOfStudents):
    self.numberOfStudents = new_numberOfStudents

  def __repr__(self):
    return "A {} school named {} with {} students.".format(self.level, self.name, self.numberOfStudents)

# a = School("Codecademy high", "high", 200)
# print(a)
# print(a.get_name())
# print(a.get_level())
# a.set_numberOfStudents(300)
# print(a.get_numberOfStudents())

class PrimarySchool(School):

  def __init__(self, name, numberOfStudents,  pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy
    

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
   parentRepr = super().__repr__()
   return parentRepr + " The pickup policy is {}.".format(self.pickupPolicy)

# b = PrimarySchool("Codecademy", 400, "Pickup Allowed")
# print(b.get_pickupPolicy)
# print(b)

class HighSchool(School):

  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams

  def get_sportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + " The sports teams are {}.".format(self.sportsTeams)


# c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball", "Football", "Soccer", "Baseball"])
# print(c.get_sportsTeams)
# print(c)

