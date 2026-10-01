import pymysql

# Registramos PyMySQL como reemplazo de MySQLdb
pymysql.install_as_MySQLdb()

from django.db.backends.mysql.features import DatabaseFeatures
DatabaseFeatures.minimum_database_version = None
