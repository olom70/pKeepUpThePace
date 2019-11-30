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
    myProfile.computeBMI()
    assert myProfile.displaybBMI() == 21
    assert myProfile.displaynBMI() == 21
    myProfile.computeRMR()
    assert myProfile.rRMRcal.get(enumandconst.RmrDates.A1918) == 1375.9863
    assert myProfile.rRMRml.get(enumandconst.RmrDates.A1918) == 3.1851534722222223
    assert myProfile.rRMRcal.get(enumandconst.RmrDates.A1990) == 1314
    myProfile.activityFactor = enumandconst.ActivityFactor.SEDENTARY
    myProfile.computeHBE()
    assert myProfile.hHBE.get(enumandconst.RmrDates.A1990) == 1839.6
    