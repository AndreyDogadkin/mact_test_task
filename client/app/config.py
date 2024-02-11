class AppConfig:
    """Конфиг клиент приложения."""

    BASE_URL = "http://127.0.0.1:5000/"
    COUNTERS_ENDPOINT = "api/counters/"

    @property
    def counters_url(self) -> str:
        return self.BASE_URL + self.COUNTERS_ENDPOINT


config = AppConfig()
