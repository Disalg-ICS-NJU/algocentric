SHELL = /bin/bash
NUM ?= 20
N ?= 13

run:
	python3 ./matrix_mult.py

test:
	python3 ./check.py

test_no_input:
	@python3 ./generator.py $(NUM) -N $(N) | while read line1; do \
		read line2; echo -e "$$line1\n$$line2" | python3 ./check.py; \
		echo ----; \
	done

random_test:
	@time python3 ./generator.py $(NUM) -N $(N) | while read line1; do \
		read line2; result=$$(echo -e "$$line1\n$$line2" | python3 ./check.py); \
		if test "$$?" -ne 0; then \
			echo "$$result"; \
			exit 1; \
		fi; \
		echo -n .; \
	done && \
	echo "PASS"
