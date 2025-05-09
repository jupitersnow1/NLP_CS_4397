**Jacqueline Sanchez**  
**October 30, 2024**  

# Boolean Search  

## Overview
For this program there will be two main folders,
1. code
2. output

in the output file it will contain 12 pickle files generated by the following queries given


| Query                  | Method 1 | Method 2 | Method 3 | Number of Files |
|------------------------|----------|----------|----------|-----------------|
| `audio quality: poor`  | Yes      | Yes      | Yes      | 3               |
| `wifi signal: strong`  | Yes      | Yes      | Yes      | 3               |
| `gps map: useful`      | Yes      | Yes      | Yes      | 3               |
| `image quality: sharp` | Yes      | Yes      | Yes      | 3               |
| **total files**        | 4        | 4        | 4        | **12**          |
  
more Info on the `code` folder, [Go to Files from the Program and Their Info](#files-from-the-program-and-their-info)



## Objective of this Program
The objective of this program is to perform Boolean searches on a dataset of reviews. It allows users to query reviews based on specific aspects and opinions using various Boolean methods.

## Brief Background on Boolean Search
Boolean search refers to a search technique that enables users to combine keywords with operators such as AND, OR, and NOT to produce more relevant results. This method is widely used in information retrieval systems, including search engines and databases, to enhance the efficiency and accuracy of searches.

## Methodology
1. **Index Table Creation**: The program creates an index table that maps keywords to review IDs, enabling efficient searches based on user queries.
2. **Tokenization**: Reviews are tokenized into individual words for processing, ensuring that searches can accurately match user inputs.
3. **Boolean Search Methods**: The program implements three Boolean search methods to handle queries: 

   - **Method 1**: Returns reviews containing any of the specified aspects **or** opinions (using OR).
     - Syntax: [aspect1] **OR** [aspect2] **OR** [opinion]
       - Example:
         - Searching for `audio` **OR** `quality` **OR** `poor` will retrieve reviews that mention any of these terms. <br><br>
       
   - **Method 2**: Returns reviews that contain all specified aspects **and** the opinion (using AND).
     - Syntax: [aspect1] **AND** [aspect2] **AND** [opinion]
       - Example:
         - Searching for `audio` **AND** `quality` **AND** `poor` will retrieve only reviews that include all terms. <br> <br>
       
   - **Method 3**: Returns reviews that contain at least one aspect and the opinion (a combination of OR and AND).
     - Syntax: [aspect1] **OR** [aspect2] **AND** [opinion]
       - Example:
         - Searching for `audio` **OR** `quality` **AND** `poor` retrieves reviews that mention at least one aspect and the opinion. <br><br>

## Files from the Program and Their Info
- **`code`**: This folder contains the source code for the application.
  - **`tokenizer.py`**: A module for tokenizing the words from the provided `.pkl` file, breaking text into individual words for processing.
  - **`index_table.py`**: Contains functions to load the review data and create an index table for efficient querying.
  - **`methods.py`**: Implements the Boolean search methods that process user queries and return results based on specified criteria.
  - **`main.py`**: The main entry point of the application, handling user input, coordinating the flow of the program, and saving output results.
<br><br>
- **`output`**: This folder is intended to store the output of the main program.
  - Inside this folder, you will find a `generated_pickles` folder that contains pickle files generated from specific queries and methods executed during the program run.
  - The `posting_list.json` file, which contains the mapping of keywords to review IDs for efficient searching.

## Libraries Needed for the Program
To run this program, you will need the following Python libraries:

| File Name         | Required Libraries                  |
|-------------------|-------------------------------------|
| `tokenizer.py`    | `nltk`                              |
| `index_table.py`  | `collections`, `json`, `os`, `tqdm`       |
| `methods.py`      | `json`, `os`                        |
| `main.py`         | `argparse`, `pandas`, `os` |

### Library Descriptions
- **`pandas`**: For data manipulation and analysis, particularly to read the `reviews_segment.pkl` file.
- **`tqdm`**: For displaying progress bars during long-running processes.
- **`nltk`**: For natural language processing tasks, including tokenization.
- **`argparse`**: For parsing command-line arguments in `main.py`.
- **`pickle`**: For saving and loading data in Python’s binary format.
- **`json`**: For handling JSON data, particularly when saving the postings list. This module is included in Python’s standard library, so no installation is required.
- **`os`**: For interacting with the operating system, such as creating directories and managing file paths.
- **`collections`**: Specifically, `defaultdict` is used for constructing the index table efficiently.

You can install these libraries using pip:
```bash
pip install pandas tqdm nltk
```

## How to Run the Program
To execute the program, follow these steps:

### 1. **Open a Terminal**:
Access your command line interface (Terminal for macOS/Linux, Command Prompt or PowerShell for Windows).
   
### 2. **Navigate to the Project Directory**:
Use the `cd` command to change to the directory where your `code` folder is located. For example:
   ```bash
   cd path/to/your/project/code 
   ```
   At this point, you should be able to run the `main.py` file.
### 3. **How to run and execute the application**
  ```bash
   python main.py -a1 "wifi" -a2 "signal" -o "strong" -m "method3" -r "../reviews_segment.pkl"
   ```

 ### Command-Line Options
    
| Symbol | Meaning            | Example                          |
|--------|--------------------|----------------------------------|
| `-a1`  | Aspect 1           | `"wifi"`                         |
| `-a2`  | Aspect 2           | `"signal"`                       |
| `-o`   | Opinion            | `"strong"`                       |
| `-m`   | Method             | `"method3"`                      |
| `-r`   | File to read from  | `"../reviews_segment.pkl"`       |
    
### Description of Parameters
- **`-a1`**: The first aspect to query in the reviews.
- **`-a2`**: The second aspect to query in the reviews.
- **`-o`**: The opinion that you want to filter the reviews by.
- **`-m`**: The Boolean search method to use (e.g., method1, method2, method3).
- **`-r`**: The path to the `.pkl` file containing the review data.

Click here to read about the querying methods the program contains under `Boolean Search Methods` **->** [m](#Methodology) 



## Output Files
The output files will contain the `review_id` for each keyword found in the index table corresponding to the specified query.

- **Naming Convention**: 
  - The files are named using the format: `aspect1_aspect2_opinion.pkl`
    - Example: 
      - `audio_quality_poor_method1.pkl`
      - The `audio_quality_poor_method1.pkl` file will contain the `review_index` for reviews that include `audio AND quality AND poor`. 
      - The `review_index` entries will appear in the form of identifiers like 'R100MJSC6EH1YH'.

## Where to Find Your Output
An `output` folder will be generated. Inside, you will find the `generated_pickles` folder containing your `.pkl` files.

Thank you for exploring my program! Special thanks to my mentors for their invaluable guidance.