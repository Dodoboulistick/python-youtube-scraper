from utils import get_output
import argparse 

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--input', help='Input JSON file with URLs', required=True)
        parser.add_argument('--output', help='Output JSON file with data', required=True)
        args = parser.parse_args()
        argdict = vars(args)
        input_parameter = argdict['input']
        output_parameter = argdict['output']
        get_output(input_file=input_parameter, output_file=output_parameter)
    except:
        print("Error in arguments")
        return -1
    return 0

main()