all:
	make launch
	
akce: src/akce.py
	@echo "python3.6 src/launch.py" > launch
	@chmod 777 launch

