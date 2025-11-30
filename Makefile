.PHONY: all run usage clean
all:
	@python run_all.py --all

run:
	@python run_all.py

usage:
	@python run_all.py --help

clean:
	@rm -rf __pycache__
	@for d in */ ; do \
		[ -d "$$d" ] || continue; \
		rm -rf "$$d/__pycache__"; \
	done