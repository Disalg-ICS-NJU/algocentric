run:
	python3 ./bubble_sort.py

test:
	python3 ./check.py

ramdom_test:
	@python3 ./generator.py | while read line; do \
		result=$$(echo "$$line" | python3 ./check.py); \
		if test "$$?" -ne 0; then \
			echo "$$result"; \
			exit 1; \
		fi; \
		echo -n .; \
	done && \
	echo "PASS"
