SOURCE_DIR = ./src

all:
	cd $(SOURCE_DIR) && make all

%:
	cd $(SOURCE_DIR) && make $@

clean:
	rm -rf ./simulation_results/**