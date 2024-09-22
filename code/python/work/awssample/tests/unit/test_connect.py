from awssample.connect.connect import Connect


def test_init1():
    con = Connect("dynamodb")
    assert con.get_client()
    assert con.get_resource()


def test_init2():
    con = Connect("dynamodb", "profile_test")
    assert con.get_client()
    assert con.get_resource()


def test_init3():
    con = Connect("dynamodb", "profile_test", "ap-northeast-1")
    assert con.get_client()
    assert con.get_resource()
