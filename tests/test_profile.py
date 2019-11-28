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
    # populate the metrics
    myProfile.age = 35
    assert myProfile.age == 35
    myProfile.gender = enumandconst.Gender.FEMALE
    myProfile.weightIntegerPart = 60
    myProfile.weightDecimalPart = 0
    myProfile.heightIntegerPart = 1
    myProfile.heightDecimalPart = 68
    myProfile.metricChoice = enumandconst.MetricChoice.ISO
    assert myProfile.displaybBMI() == 21
    assert myProfile.displaynBMI() == 21
    