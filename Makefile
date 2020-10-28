#SPDX-License-Identifier: MIT

default:
	@ echo "Installation Commands:"
	@ echo "    install                         Installs Augur's full stack for production"
	@ echo "    clean                           Removes potentially troublesome compiled files"
	@ echo "    rebuild                         Removes build/compiled files & binaries and reinstalls the project"
	@ echo
	@ echo "Development Commands:"
	@ echo "    db                              Initialize a fresh Docker database container (restarts it if it's still running)"
	@ echo "    dev                             Starts the full stack in the background"
	@ echo "    dev-start                       Runs the backend and frontend servers in the background"
	@ echo "    dev-stop                        Stops the backgrounded backend & frontend server commands"
	@ echo
	@ echo "Testing Commands:"
	@ echo "    test-data                       Start the testing dataset Docker database"
	@ echo "    test                            Runs all tests"
	@ echo "    test-application                Runs all application unit tests (including metrics)"
	@ echo "    test-workers                    Run all worker unit tests"
	@ echo "    test-metric-routes              Run all metrics API tests"
	@ echo
	@ echo "Documentation Commands:"
	@ echo "    docs                            Generates the documentation"
	@ echo "    docs-view                       Generates the documentation, then opens it for local viewing"


#
#  Installation
#
.PHONY: install install-dev
.PHONY: install-spdx install-spdx-sudo install-augur-sbom
.PHONY: clean rebuild
install:
	@ ./scripts/install/install.sh prod

install-dev:
	@ ./scripts/install/install.sh dev

install-spdx:
	@ ./scripts/install/install-spdx.sh

install-spdx-sudo:
	@ ./scripts/install/install-spdx-sudo.sh

install-augur-sbom:
	@ ./scripts/install/nomos.sh

clean:
	@ scripts/control/clean.sh

rebuild:
	@ scripts/control/rebuild.sh prod

rebuild-dev:
	@ scripts/control/rebuild.sh dev


#
#  Development
#
.PHONY: dev-start dev-stop dev monitor-frontend monitor-backend monitor frontend backend-stop backend-start backend-restart backend clean rebuild

dev-start:
	@ scripts/control/start_augur.sh
	@ scripts/control/start_frontend.sh

dev-stop:
	@ augur backend stop
	@ scripts/control/kill_frontend.sh

dev: dev-stop dev-start

db:
	@ - docker stop augur_database
	@ - docker rm augur_database
	@ docker run -p 5434:5432 --name augur_database augurlabs/augur:database


#
# Testing
#
.PHONY: test test-data test-application test-metric-routes test-python-versions

test-data:
	@ - docker stop augur_test_data
	@ - docker rm augur_test_data
	@ docker run -p 5434:5432 --name augur_test_data augurlabs/augur:test_data@sha256:71da12114bf28584a9a64ede2fac0cbc8dffc8e2f4a2c61231206e2f82201c2f

test: test-application test-metric-routes test-workers

test-application:
	@ bash -c 'tox -e py-application'

test-workers:
	@ bash -c 'tox -e py-workers'

test-metric-routes:
	@ bash -c 'tox -e py-metric-routes'

test-python-versions:
	@ bash -c 'tox -e ALL'


#
# Documentation
#
.PHONY: docs docs-view
docs:
	@ bash -c 'cd docs/ && rm -rf build/ && make html;'

docs-view: docs
	@ bash -c 'open docs/build/html/index.html'


#
# Docker Shortcuts
# Do not use these unless you know what they mean.
.PHONY: compose-run compose-run-database
.PHONY: build-backend run-backend build-frontend run-frontend build-database run-database


compose-run:
	@ docker-compose -f docker-compose.yml up --build

compose-run-database:
	@ echo "**************************************************************************"
	@ echo "Make sure there are no database credentials in docker_env.txt!"
	@ echo "**************************************************************************"
	@ echo
	@ docker-compose -f docker-compose.yml -f database-compose.yml up --build

docker-build: docker-build-backend docker-build-frontend docker-build-database

docker-build-backend:
	@ docker build -t augurlabs/augur:backend -f util/docker/backend/Dockerfile .

docker-build-frontend:
	@ docker build -t augurlabs/augur:frontend -f util/docker/frontend/Dockerfile .

docker-build-database:
	@ docker build -t augurlabs/augur:database -f util/docker/database/Dockerfile .


docker-run-backend:
	@ - docker stop augur_backend
	@ - docker rm augur_backend
	@ docker run -p 5000:5000 --name augur_backend --env-file docker_env.txt augurlabs/augur:backend

docker-run-frontend:
	@ - docker stop augur_frontend
	@ - docker rm augur_frontend
	@ docker run -p 8080:8080 --name augur_frontend augurlabs/augur:frontend

docker-run-database:
	@ - docker stop augur_database
	@ - docker rm augur_database
	@ docker run -p 5434:5432 --name augur_database augurlabs/augur:database
