import START_Lab_1
import pandas as pd

def generate_parametrized_tests(filename):
    sol_df = pd.read_csv(filename, header=None)
    test_functions = []
    
    for index, row in sol_df.iterrows():
        if row[0].startswith("lab1"):
            test_name = row[0]
            test_code = row[1]
            test_functions.append(f"def test_{test_name}():\n    {test_code}")
    
    return "\n\n".join(test_functions)

sol_filename = "SAMP_SOL_Lab_1.py"

sol_df = pd.read_csv(sol_filename, header=None)

q1_tests = sol_df[sol_df[0].str.contains("lab1Question1")]

def test_q1():
    assert(1==1)