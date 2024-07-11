image=csci-env/base-dev
container=cscienv-nbgrader-exchange-dev
export

deps:
	pip install -r requirements-dev.txt

update-deps:
	python -m venv deps+update             && \
	    . deps+update/bin/activate         && \
	    pip install -r requirements-dev.in && \
	    pip freeze > requirements-dev.txt  && \
	    deactivate                         && \
	    rm -rf deps+update

try:
	dev/start-container.sh

dev-clean:
	docker container rm -f ${container}
	docker image rm ${image}
