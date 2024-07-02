SHELL = /bin/bash
NUM ?= 100
NODE ?= 100
EDGE ?= 500

run:
	python3 ./dijkstra.py

test:
	python3 ./check.py


test_no_input:
	@python3 ./generator.py -n $(NODE) -N $(NODE) -m $(EDGE) -M $(EDGE) $(NUM) --has_negative_edges\
	| while read n m s; do \
		(echo "$$n $$m $$s "; \
		for ((i=1; i<=$$m; i++)); do \
			read line1; \
			echo "$$line1"; \
		done) \
		| python3 ./check.py ; \
		echo ----; \
	done

random_test:
	@time python3 ./generator.py  $(NUM) \
	| while read n m s; do \
		result=$$((echo "$$n $$m $$s "; \
		for ((i=1; i<=$$m; i++)); do \
			read line1; \
			echo "$$line1"; \
		done) \
		| python3 ./check.py); \
		if test "$$?" -ne 0; then \
			echo "$$result"; \
			exit 1; \
		fi; \
		echo -n .; \
	done
