
all: installer #run gui.py
	chmod +x gui.py


installer:
	mkdir ~/calculator
	mkdir ~/calculator/venv
	cp ./gui.py ~/calculator/gui.py
	cp ./mathlib.py ~/calculator/mathlib.py
	apt install python3-venv
	python3 -m venv ~/calculator/venv
	source ~/calculator/venv/bin/activate
	python3 -m sudo apt-get install python-tk
	chmod +x ~/calculator/gui.py


delete:
	rm -rf ~/calculator

run:
	python3 ~/calculator/gui.pyS