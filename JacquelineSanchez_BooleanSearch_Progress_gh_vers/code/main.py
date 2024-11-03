# libraries needed for manipulating the data from them .pkl file
import pandas as pd
import argparse
import os
import pickle

# `methods.py` and `index_table.py` files
from methods import method1, method2, method3
from index_table import load_data, create_index, save_posting_list  # Import the save function

# initializing the main.py file function to execute the program
def main():
    """
        main function to perform Boolean search on review data.
        This function handles command-line arguments, loads review data,
        creates an index, calls the appropriate search method, and saves results.
        """

    # setting up argument parsing for command line input
    parser = argparse.ArgumentParser(description="Perform the boolean search.")

    # defining command-line arguments
    parser.add_argument("-a1", "--aspect1", type=str, required=True, help="First word of the aspect")
    parser.add_argument("-a2", "--aspect2", type=str, required=True, help="Second word of the aspect")
    parser.add_argument("-o", "--opinion", type=str, required=True, help="Only word of the opinion")
    parser.add_argument("-m", "--method", type=str, required=True, help="Method of boolean operation (method1, method2, method3)")
    parser.add_argument("-r", "--reviews_file", type=str, required=True, help="Path to the reviews_segment.pkl file")

    # parse the arguments
    args = parser.parse_args()

    # load the review data
    review_df = load_data(args.reviews_file)

    # create an index table
    index_table = create_index(review_df)

    # save the posting list as JSON in the output directory
    output_dir = "../output"  # Adjusted path for the output directory
    os.makedirs(output_dir, exist_ok=True)
    save_posting_list(index_table, output_dir)  # Save posting list to the output directory

    # calling the appropriate method
    if args.method.lower() == "method1":
        result = method1(index_table, args.aspect1, args.aspect2, args.opinion)
    elif args.method.lower() == "method2":
        result = method2(index_table, args.aspect1, args.aspect2, args.opinion)
    elif args.method.lower() == "method3":
        result = method3(index_table, args.aspect1, args.aspect2, args.opinion)
    else:
        print("\n!! The method is not supported !!\n")
        return

    # saving results
    generated_pickles_dir = os.path.join(output_dir, "generated_pickles")  # Create path for generated pickles
    os.makedirs(generated_pickles_dir, exist_ok=True)

    # save the results in a pd dataframe and output it to a .pkl file
    revs = pd.DataFrame()
    revs["review_index"] = list(result)  # adjusting according to your result structure
    output_file = os.path.join(generated_pickles_dir, f"{args.aspect1}_{args.aspect2}_{args.opinion}_{args.method}.pkl")
    revs.to_pickle(output_file) # save it into .pkl form

# main program
if __name__ == "__main__":
    main()
