class AppConfig:
    """Конфиг клиент приложения."""

    BASE_URL = "127.0.0.1:5000/"
    COUNTERS_API = "api/counters/"

    @property
    def counters_endpoint(self):
        return self.BASE_URL + self.COUNTERS_API
