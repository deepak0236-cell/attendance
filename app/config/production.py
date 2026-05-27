class ProductionConfig:

    DEBUG = False

    SQLALCHEMY_DATABASE_URI = \
        'mysql://root:password@localhost/attendance'