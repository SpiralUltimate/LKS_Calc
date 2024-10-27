
OUTPUT_PATH = ./output/

BUILD_FLAGS = --onefile --clean --distpath $(OUTPUT_PATH)

output: LKS_calc.py
	pyinstaller $(BUILD_FLAGS) LKS_calc.py

clean:
	del *.spec