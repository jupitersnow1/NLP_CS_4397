# libraries needed for manipulating the data from .pkl file
import pandas as pd
import argparse
import os
from methods import method1, method2, method3
from index_table import load_data, create_index, save_posting_list, sort_index, save_sorted_keywords

# initializing the main.py file function to execute the program
def main():
    """
    main function to perform Boolean search on review data.
    This function handles command-line arguments, loads review data,
    creates an index, sorts it, calls the appropriate search method, and saves results.
    """

    # setting up argument parsing for command line input
    parser = argparse.ArgumentParser(description="Perform the boolean search.")

    # defining command-line arguments
    parser.add_argument("-a1", "--aspect1", type=str, required=True, help="First word of the aspect")
    parser.add_argument("-a2", "--aspect2", type=str, required=True, help="Second word of the aspect")
    parser.add_argument("-o", "--opinion", type=str, required=True, help="Only word of the opinion")
    parser.add_argument("-m", "--method", type=str, required=True, help="Method of boolean operation (method1, method2, method3)")
    parser.add_argument("-r", "--reviews_file", type=str, required=True, help="Path to the reviews_segment.pkl file")

    # parsing the arguments
    args = parser.parse_args()

    # load the review data
    review_df = load_data(args.reviews_file)


##############################

    # create an index table
    index_table = create_index(review_df)

    # save the posting list as JSON in the output directory
    output_dir = "../output"
    os.makedirs(output_dir, exist_ok=True)
    save_posting_list(index_table, output_dir)

    # sort keywords and save sorted output
    sorted_keywords = sort_index(index_table)
    save_sorted_keywords(sorted_keywords, output_dir)

################


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

    # save the results to a .pkl file
    generated_pickles_dir = os.path.join(output_dir, "generated_pickles")
    os.makedirs(generated_pickles_dir, exist_ok=True)

    revs = pd.DataFrame()
    revs["review_index"] = list(result)  # adjust according to your result structure
    output_file = os.path.join(generated_pickles_dir, f"{args.aspect1}_{args.aspect2}_{args.opinion}_{args.method}.pkl")
    revs.to_pickle(output_file)

if __name__ == "__main__":
    main()

