
all: installer #run gui.py
	chmod +x gui.py


installer:
	mkdir ~/calculator
	mkdir ~/calculator/venv
	cp ./gui.py ~/calculator/gui.py
	cp ./mathlib.py ~/calculator/mathlib.py
	cp ./test_mathlib.py ~/calculator/test_mathlib.py
	sudo apt-get install python-tk
	sudo apt-get install python3-pytest
	sudo apt-get install doxygen
	chmod +x ~/calculator/gui.py

delete:
	#source ~/calculator/venv/bin/deactivate
	rm -rf ~/calculator

run:
	python3 ~/calculator/gui.py
doc:
	doxygen  Doxyfile
	cp -a ./html ~/calculator
	rm -rf  html

test: test_mathlib.py
	pytest ~/calculator/test_mathlib.py

