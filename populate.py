import pathlib
import sys

ADVENT_OF_CODE_DIR = pathlib.Path.home().joinpath("Documents", "programming", "Advent of Code")
TEMPLATE_FILE = ADVENT_OF_CODE_DIR.joinpath("aoc_template.py")
#TEST_TEMPLATE_FILE = ADVENT_OF_CODE_DIR.joinpath("test_aoc_template.py") 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: populate.py [year]")
        exit()
    for year in sys.argv[1:]:
        # get arg
        # check arg?
        # create dir with arg name
        year_dir = ADVENT_OF_CODE_DIR.joinpath(year)
        if year_dir.exists():
            print(f"{year_dir} already exists")
            exit()

        year_dir.mkdir()
        # populate with samples, data, solvers
        sample_dir = year_dir.joinpath("sample")
        sample_dir.mkdir()
        data_dir = year_dir.joinpath("data")
        data_dir.mkdir()
        code_dir = year_dir.joinpath("code")
        code_dir.mkdir()

        # for each day, create a file in each dir
        for day in range(1, 26):
            #[].map(.joinpath(f"{day}.txt").touch())
            sample_dir.joinpath(f"{day}.txt").touch()
            
            data_dir.joinpath(f"{day}.txt").touch()
            
            #solvers_dir.joinpath(f"{day}.txt").touch()
            # add code file
            solve_file = code_dir.joinpath(f"{day}.py")
            solve_file.write_bytes(TEMPLATE_FILE.read_bytes())
        """
        # populate year dir with day dirs
        # each contains day.py sample.txt input.txt
        for day in range(1, 26):
            day_dir = year_dir.joinpath(f"{day}")
            day_dir.mkdir()
            day_dir.joinpath("sample.txt").touch()
            day_dir.joinpath("input.txt").touch()
            day_str = f"aoc_{year}_{day}"
            # add code file
            code_file = day_dir.joinpath(f"{day_str}.py")
            code_file.write_bytes(TEMPLATE_FILE.read_bytes())
            # add test file
            # test_file = day_dir.joinpath(f"test_{day_str}.py")
            # test_file.write_bytes(TEST_TEMPLATE_FILE.read_bytes())
        """
