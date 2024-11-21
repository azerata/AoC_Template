import argparse
import os

argparser=argparse.ArgumentParser(description="Initiator to rename files to fit the day of the task.")

argparser.add_argument(--day, type=str, required=True)
args = argparser.parse_args()


if __name__=="__main__":
    args = argparser.parse_args()
    base_path = os.getcwd()
    
    test_file = os.path.join(base_path, f"test/test_{args.day}.py")
    main_file = os.path.join(base_path, f"main/{args.day}.py")

    os.rename()
