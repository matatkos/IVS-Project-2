all: installer #run gui.py
	chmod +x gui.py
#todo installer done, add additional targets, copy additional files in installer when they will be available form other teammates

installer:
	mkdir ~/calculator
	mkdir ~/calculator/venv
	cp ./gui.py ~/calculator/gui.py
	cp ./mathlib.py ~/calculator/mathlib.py
	sudo apt-get install python-tk
	chmod +x ~/calculator/gui.py


delete:
	rm -rf ~/calculator

run:
	python3 ~/calculator/gui.py