from services.exchange_calculations import calculer_variation, calculer_moyenne

def test_calculer_moyenne():
    assert calculer_moyenne([10, 20, 30]) == 20
    assert calculer_moyenne([]) == 0

def test_calculer_variation():
    assert calculer_variation(100, 110) == 10.0
    assert calculer_variation(100, 90) == -10.0