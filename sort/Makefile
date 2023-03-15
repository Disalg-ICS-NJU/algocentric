TARGET ?= merge_sort

run:
	python3 $(TARGET)/$(TARGET).py

test:
	python3 ./check.py $(TARGET)

test_no_input:
	@python3 ./generator.py -l 1000 -L 1000 10 | while read line; do \
		echo "$$line" | python3 ./check.py $(TARGET); \
		if test "$(TARGET)" = "bubble_sort"; then \
			echo "After optimization:"; \
			echo "$$line" | python3 ./check.py -o $(TARGET); \
		fi; \
		echo ----; \
	done

NUM ?= 10

random_test:
	@time python3 ./generator.py $(NUM) | while read line; do \
		result=$$(echo "$$line" | python3 ./check.py $(TARGET)); \
		if test "$$?" -ne 0; then \
			echo "$$result"; \
			exit 1; \
		fi; \
		echo -n .; \
	done && \
	echo "PASS"
