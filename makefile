DB_PLATFORM=hrtime.db
DB_PLATFORM_LOCATION=.\hrtime_migrate
DB_PLATFORM_PATH="$(DB_PLATFORM_LOCATION)\$(DB_PLATFORM)"
MIGRATION_DIRECTORY = .\hrtime_migrate


data\hrtime\drop:
	rm $(DB_PLATFORM_PATH)

data\hrtime\init:
	python "$(MIGRATION_DIRECTORY)\create_hrtime_sqlite.py" init -d $(DB_PLATFORM_PATH)

data\hrtime\reinit:
	python "$(MIGRATION_DIRECTORY)\create_hrtime_sqlite.py" reinit -d $(DB_PLATFORM_PATH)

data\hrtime\migrate-card:
	python "$(MIGRATION_DIRECTORY)\migrate_sqlite.py" migrate -p "$(MIGRATION_DIRECTORY)" -d $(DB_PLATFORM_PATH) -f "db_card.json"

data\hrtime\migrate-registration:
	python "$(MIGRATION_DIRECTORY)\migrate_sqlite.py" migrate -p "$(MIGRATION_DIRECTORY)" -d $(DB_PLATFORM_PATH) -f "db_registration.json"

data\hrtime\migrate-worker:
	python "$(MIGRATION_DIRECTORY)\migrate_sqlite.py" migrate -p "$(MIGRATION_DIRECTORY)" -d $(DB_PLATFORM_PATH) -f "db_user.json"

data\hrtime\migrate: data\hrtime\migrate-card data\hrtime\migrate-registration data\hrtime\migrate-worker