run:
	python3 ./bubble_sort.py

test:
	python3 ./check.py optimize

test_no_input:
	python3 ./generator.py -l 1000 -L 1000 1 | python3 ./check.py optimize

NUM ?= 10

random_test:
	@python3 ./generator.py $(NUM) | while read line; do \
		result=$$(echo "$$line" | python3 ./check.py); \
		if test "$$?" -ne 0; then \
			echo "$$result"; \
			exit 1; \
		fi; \
		echo -n .; \
	done && \
	echo "PASS"
