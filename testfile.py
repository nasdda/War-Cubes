import cx_Freeze
executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "Cube Wars",
    options = {"build_exe":{"packages":["pygame"],"include_files":["background.jpg"]}},
    executables = executables
)

