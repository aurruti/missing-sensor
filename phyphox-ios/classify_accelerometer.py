import pandas as pd
import os

def classify_data(input_csv_path, p_timestamp1, p_timestamp2, p_timestamp3):

    # Read the CSV file
    df = pd.read_csv(input_csv_path)

    # Read the timestamp CSV file
    # timestamp_df = pd.read_csv('./timestamps.csv')

    

    # Define time intervals for each activity
    start_standup = p_timestamp3 + 60
    start_walk = start_standup + 30
    start_jog = start_walk + 30
    start_rest = start_jog + 30
    start_squat = start_rest + 30
    start_clap = start_squat + 15
    start_msrc12_1 = start_clap + 10
    start_msrc12_2 = start_msrc12_1 + 15
    start_msrc12_3 = start_msrc12_2 + 15
    start_msrc12_4 = start_msrc12_3 + 15
    start_msrc12_5 = start_msrc12_4 + 15
    start_msrc12_6 = start_msrc12_5 + 15
    start_msrc12_7 = start_msrc12_6 + 15
    start_msrc12_8 = start_msrc12_7 + 15
    start_msrc12_9 = start_msrc12_8 + 15
    start_msrc12_10 = start_msrc12_9 + 15
    start_msrc12_11 = start_msrc12_10 + 15
    start_msrc12_12 = start_msrc12_11 + 15

    # Define bin edges for classification
    bin_edges = [-float('inf'), p_timestamp1, p_timestamp2, p_timestamp3,
                 start_standup, start_walk, start_jog, start_rest,
                 start_squat, start_clap, start_msrc12_1, start_msrc12_2,
                 start_msrc12_3, start_msrc12_4, start_msrc12_5, start_msrc12_6,
                 start_msrc12_7, start_msrc12_8, start_msrc12_9, start_msrc12_10,
                 start_msrc12_11, start_msrc12_12, float('inf')]

    # Define labels for classification
    labels = ['freestyle', 'write_by_hand', 'write_on_pc', 'standardized_times', 'standup', 'walk', 'jog',
              'rest', 'squat', 'clap', 'msrc12_1', 'msrc12_2', 'msrc12_3', 'msrc12_4', 'msrc12_5',
              'msrc12_6', 'msrc12_7', 'msrc12_8', 'msrc12_9', 'msrc12_10', 'msrc12_11', 'msrc12_12']

    # Create a new column 'Label' and classify the data based on time intervals
    df['Labels'] = pd.cut(df['Time (s)'], bins=bin_edges, labels=labels)


    return df


def loop_data_folders(data_folders, timestamps_df):
    for data_folder in data_folders:
        participant_code = data_folder.split('-')[0].lower()  # Extract participant code
        timestamps_participant = timestamps_df[timestamps_df['Participant Code'].str.lower() == participant_code]

        if len(timestamps_participant) == 0:
            print(f"No timestamps found for participant {participant_code}. Skipping folder {data_folder}.")
            continue

        p_timestamp1 = timestamps_participant['Timestamp 1 (s)'].values[0]
        p_timestamp2 = timestamps_participant['Timestamp 2 (s)'].values[0]
        p_timestamp3 = timestamps_participant['Timestamp 3 (s)'].values[0]

        data_path = os.path.join('phyphox-ios', 'data', data_folder)
        for file in os.listdir(data_path):
            if file == 'converted_data.csv':
                input_csv_path = os.path.join(data_path, file)
                output_csv_path = os.path.join(data_path, 'labeled_data.csv')
                if not os.path.exists(output_csv_path):
                    df = classify_data(input_csv_path, p_timestamp1, p_timestamp2, p_timestamp3)
                    # Save the labeled data to a new CSV file
                    df.to_csv(output_csv_path, index=False)
                    print(f"Data labeled and saved to {output_csv_path}")
                else:
                    print(f"Skipping {input_csv_path}. Already classified.")


if __name__ == "__main__":
    # Define the folders containing raw data for left and right pockets
    data_folders = []

    # Generate elements for 20 participants with left and right pockets
    for i in range(1, 21):
        data_folders.append(f'p{i}-left-pocket')
        data_folders.append(f'p{i}-right-pocket')

    timestamps_path = './timestamps.csv'

    # Path definitions
    # self_path = os.path.realpath(__file__)
    # timestamps_path = self_path.replace('phyphox-ios\\classify_accelerometer.py', timestamps_path)
    timestamps_df = pd.read_csv(timestamps_path)

    # Process data folders
    loop_data_folders(data_folders, timestamps_df)