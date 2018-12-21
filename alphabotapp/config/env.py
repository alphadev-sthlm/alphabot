class EnvConfig(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    # SECRET = get_env('SECRET')


class DevelopmentEnv(EnvConfig):
    """Configurations for Development."""
    DEBUG = True
    TESTING = True


class ProductionEnv(EnvConfig):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_env = {
    'development': DevelopmentEnv,
    'production': ProductionEnv,
}
