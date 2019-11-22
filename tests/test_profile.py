from context import profile

def test_instance_creation():
    myProfile = profile.Profile('clode')
    assert myProfile.profileName == 'clode'
    