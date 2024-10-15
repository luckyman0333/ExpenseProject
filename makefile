data\hrtime\init:
	python .\hrtime_migrate\migrate_sqlite.py recreate

data\hrtime\migrate:
	python .\hrtime_migrate\migrate_sqlite.py migrate

data\hrtime\drop:
	python .\hrtime_migrate\migrate_sqlite.py drop
