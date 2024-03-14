import pandas as pd

def excel_to_df_ms(path, columns = ['Time (s)', 'a: EMG RMS 1-1', 'Time (s)', 'a: EMG RMS 1-2', 'Time (s)', 'a: EMG RMS 1-3', 'Time (s)', 'a: EMG RMS 1-4']):
    """""
    For a given excel file; the function will return a dataframe with time in milliseconds.
    Input:
        path: str, path to the excel file
        columns: list, column names of the dataframe (by default it takes the names of the columns of a EMG report file)
    Returns:
        df: pd.DataFrame, dataframe with time in milliseconds
    """""
    # Read the Excel file
    df = pd.read_excel(path)
    # Convert time columns to milliseconds
    df.columns = columns
    df['Time (ms)'] = df['Time (s)'].apply(lambda x: float(x.replace(',', '.')) * 1000)
    df.drop(columns=['Time (s)'], inplace=True)
    return df

def save_to_csv_by_time_interval(df, start_time, end_time, output_file, time_column = 'Time (ms)'):
    """""
    Export a time interval of a given dataframe to a CSV file.
    Input:
        df: pd.DataFrame, dataframe with time in milliseconds
        start_time: int, start time of the interval in milliseconds
        end_time: int, end time in milliseconds
        output_file: str, name of the output file
        time_column: str, name of the time column (by default Time (ms))
    Returns:
        None
    """""
    df_time_interval = df[(df[time_column] >= start_time) & (df[time_column] <= end_time)]
    df_time_interval.to_csv(output_file, index=False)
    return None

def emg_test_classification(input_path, output_dir, start_write_by_hand, start_write_on_pc, start_standardized_times):
    """""
    Classify the EMG test based on the time intervals of the data collection activity.
    ATTENTION: This function WILL OVERWRITE files with the same name in the output directory.
    Input:
        input_path: str, path to the .xlsx file with the raw data.
        output_dir: str, path to the output directory
        start_write_by_hand: int, start time of the write by hand activity in milliseconds
        start_write_on_pc: int, start time of the write on PC activity in milliseconds
        start_standardized_times: int, start time of the standardized times activity in milliseconds
    Returns:
        None
    """""
    df = excel_to_df_ms(input_path)

    # Time definitions
    start_standup = start_standardized_times + 60000
    start_walk = start_standup + 30000
    start_jog = start_walk + 30000
    start_rest = start_jog + 30000
    start_squat  = start_rest + 30000
    start_clap  = start_squat + 15000
    start_msrc12_1 = start_clap + 10000
    start_msrc12_2 = start_msrc12_1 + 15000
    start_msrc12_3 = start_msrc12_2 + 15000
    start_msrc12_4 = start_msrc12_3 + 15000
    start_msrc12_5 = start_msrc12_4 + 15000
    start_msrc12_6 = start_msrc12_5 + 15000
    start_msrc12_7 = start_msrc12_6 + 15000
    start_msrc12_8 = start_msrc12_7 + 15000
    start_msrc12_9 = start_msrc12_8 + 15000
    start_msrc12_10 = start_msrc12_9 + 15000
    start_msrc12_11 = start_msrc12_10 + 15000
    start_msrc12_12 = start_msrc12_11 + 15000

    save_to_csv_by_time_interval(df, start_write_by_hand, start_write_on_pc, output_dir + '/write_by_hand.csv')
    save_to_csv_by_time_interval(df, start_write_on_pc, start_standardized_times, output_dir + '/write_on_pc.csv')
    save_to_csv_by_time_interval(df, start_standardized_times, start_standup, output_dir + '/scroll.csv')
    save_to_csv_by_time_interval(df, start_standup, start_walk, output_dir + '/standup.csv')
    save_to_csv_by_time_interval(df, start_walk, start_jog, output_dir + '/walk.csv')
    save_to_csv_by_time_interval(df, start_jog, start_rest, output_dir + '/jog.csv')
    save_to_csv_by_time_interval(df, start_rest, start_squat, output_dir + '/rest.csv')
    save_to_csv_by_time_interval(df, start_squat, start_clap, output_dir + '/squat.csv')
    save_to_csv_by_time_interval(df, start_clap, start_msrc12_1, output_dir + '/clap.csv')
    save_to_csv_by_time_interval(df, start_msrc12_1, start_msrc12_2, output_dir + '/msrc12_1.csv')
    save_to_csv_by_time_interval(df, start_msrc12_2, start_msrc12_3, output_dir + '/msrc12_2.csv')
    save_to_csv_by_time_interval(df, start_msrc12_3, start_msrc12_4, output_dir + '/msrc12_3.csv')
    save_to_csv_by_time_interval(df, start_msrc12_4, start_msrc12_5, output_dir + '/msrc12_4.csv')
    save_to_csv_by_time_interval(df, start_msrc12_5, start_msrc12_6, output_dir + '/msrc12_5.csv')
    save_to_csv_by_time_interval(df, start_msrc12_6, start_msrc12_7, output_dir + '/msrc12_6.csv')
    save_to_csv_by_time_interval(df, start_msrc12_7, start_msrc12_8, output_dir + '/msrc12_7.csv')
    save_to_csv_by_time_interval(df, start_msrc12_8, start_msrc12_9, output_dir + '/msrc12_8.csv')
    save_to_csv_by_time_interval(df, start_msrc12_9, start_msrc12_10, output_dir + '/msrc12_9.csv')
    save_to_csv_by_time_interval(df, start_msrc12_10, start_msrc12_11, output_dir + '/msrc12_10.csv')
    save_to_csv_by_time_interval(df, start_msrc12_11, start_msrc12_12, output_dir + '/msrc12_11.csv')
    save_to_csv_by_time_interval(df, start_msrc12_12, start_msrc12_12 + 15000, output_dir + '/msrc12_12.csv')

    return None

if __name__ == '__main__':
    ## TO-DO:
    ## Scrutinize EMG raw data files for the starting times of the activites
    ## Call emg_tes_classification function accordingly for the 20 data files.
    raise NotImplementedError