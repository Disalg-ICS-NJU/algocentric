SHELL = /bin/bash
NUM ?= 10

run:
	python3 ./closest_pairs.py

test:
	python3 ./check.py

test_no_input:
	@python3 ./generator.py -n 100 $(NUM) -x -1000 -X 1000 -y -100 -Y 1000 | \
	while read n; do \
		points="$$n"; \
		for i in $$(seq 1 $$n); do \
			read line; \
			points="$$points\n$$line"; \
		done; \
		echo -e "$$points" | python3 ./check.py; \
		echo "----"; \
	done

random_test:
	@time python3 ./generator.py $(NUM) | \
	while read n; do \
		points="$$n"; \
		for i in $$(seq 1 $$n); do \
			read line; \
			points="$$points\n$$line"; \
		done; \
		result=$$(echo -e "$$points" | python3 ./check.py); \
		if test "$$?" -ne 0; then \
			echo "$$result"; \
			exit 1; \
		fi; \
		echo -n .; \
	done && \
	echo "PASS"


