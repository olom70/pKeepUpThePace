from context import profile
from context import enumandconst

myProfile = profile.Profile('clode')
  # corrected MET
  # Female / Normal Weight
  # 60 kg, 168 cm
  # 35 ans

def test_instance_creation():
    assert myProfile.profileName == 'clode'

def test_values_of_profile():
    myProfile.age = 35
    myProfile.gender = enumandconst.Gender.FEMALE
    myProfile.weight = 60
    myProfile.heightIntegerPart = 1
    myProfile.heightDecimalPart = 68
    myProfile.metricChoice = enumandconst.MetricChoice.ISO
    