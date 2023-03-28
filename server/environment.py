ENVIRONMENT = 'development'

if ENVIRONMENT == 'development':
    SETTINGS_MODULE = 'server.settings.development'
if ENVIRONMENT == 'production':
    SETTINGS_MODULE = 'server.settings.production'
