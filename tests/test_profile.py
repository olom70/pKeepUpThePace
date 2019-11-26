from context import profile
from context import enumandconst

myProfile = profile.Profile('clode')
  # corrected MET
  # Female / Normal Weight
  # 60 kg, 168 cm
  # 35 ans

def test_instance_creation():
    print("Is profilename OK ?")
    assert myProfile.profileName == 'clode'

def test_values_of_profile():
    # populate the metrics
    myProfile.age = 35
    print("age verification:")
    print(myProfile.age)
    assert myProfile.age == 35
    myProfile.gender = enumandconst.Gender.FEMALE
    myProfile.weight = 60
    myProfile.heightIntegerPart = 1
    myProfile.heightDecimalPart = 68
    myProfile.metricChoice = enumandconst.MetricChoice.ISO
    print("calculate BMI")
    myProfile.computeBMI()
    print(myProfile.nBMI)
    print(myProfile.bBMI)
    assert myProfile.bBMI == 21.258503401360546
    assert myProfile.nBMI == 21.32167888506797
    