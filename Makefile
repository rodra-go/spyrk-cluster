.PHONY: build

build:
	@docker build -t rodrago/rapids-openjdk ./docker/rapids-openjdk
	@docker build -t rodrago/spark-base-hadoop:2.4.6 ./docker/spark-base
	@docker build -t rodrago/spark-master-hadoop:2.4.6 ./docker/spark-master
	@docker build -t rodrago/spark-worker-hadoop:2.4.6 ./docker/spark-worker
