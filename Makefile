
all: run# installer #run gui.py
	chmod +x gui.py


installer:
	mkdir ~/calculator
	mkdir ~/calculator/venv
	cp ./gui.py ~/calculator/gui.py
	cp ./mathlib.py ~/calculator/mathlib.py
	sudo apt-get install python-tk
	chmod +x ~/calculator/gui.py


delete:
	#source ~/calculator/venv/bin/deactivate
	rm -rf ~/calculator

run:
	python3 ~/calculator/gui.py
