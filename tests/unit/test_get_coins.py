from services.get_coins import GetCoins


class TestGetCoins:
    def test_get_dollar(self):
        get_dollar = GetCoins.get_dollar()
        assert type(get_dollar) is float

    def test_get_euro(self):
        get_dollar = GetCoins.get_euro()
        assert type(get_dollar) is float
