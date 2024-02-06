# clean.py

import pandas as pd
import argparse


def clean_data(input1, input2, output):
    # Step 1: Merge the two input data files based on the ID value
    contact_df = pd.read_csv(input1)
    other_df = pd.read_csv(input2)

    # Renaming the columns to have a common merge key
    contact_df.rename(columns={'respondent_id': 'id'}, inplace=True)

    # Merge the dataframes on 'id'
    merged_df = pd.merge(contact_df, other_df, on='id')

    # Step 2: Drop any rows with missing values
    merged_df.dropna(inplace=True)

    # Step 3: Drop any rows if their job value contains 'insurance' or 'Insurance'
    merged_df = merged_df[~merged_df['job'].str.contains('insurance', case=False)]

    # Step 4: Save the cleaned data in project folder
    merged_df.to_csv(output, index=False)


def main():
    parser = argparse.ArgumentParser(description='Clean and merge respondent data files.')
    parser.add_argument('input1', type=str, help='Path to the respondent_contact.csv file')
    parser.add_argument('input2', type=str, help='Path to the respondent_other.csv file')
    parser.add_argument('output', type=str, help='Path to the output file')

    args = parser.parse_args()
    clean_data(args.input1, args.input2, args.output)


if __name__ == "__main__":
    main()