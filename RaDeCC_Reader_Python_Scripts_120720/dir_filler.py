



#__________________________________________________________________________________________________________________________________________________________
"""Working Code, Do Not Change"""
#__________________________________________________________________________________________________________________________________________________________

"""
This function takes directory tree generated by dir_constructor_v2 and searches the folder containing all the reads (copyDir) for each deployment type, deployment number and depth, populating
each folder with the corresponding reads.

At the end it compares the list of files in the copyDir with a list of files that have been copied to see if any have been left out. It then prints the number of files that were left out or
not copied.
"""



# Import the os module, for the os.walk function
import os, shutil
from pathlib import Path



def dir_filler(output_directory, input_directory, acstd_date_dict, thstd_start_activity_dict, blank_name_list, acstd, thstd, blank, log_df, logfile_directory, linear_data_type, sample_variable, sub_sample_variable):

    list_of_input_files = os.listdir(input_directory)
    list_of_files_copied = []
    # print('Output?',output_directory/blank)

    logsheet_filename = logfile_directory.parts[-1]
    shutil.copy(input_directory/logsheet_filename, output_directory/'Logsheet'/logsheet_filename)
    list_of_files_copied.append(logsheet_filename)

    for filename in list_of_input_files:
        # blanks
        for blank_name in blank_name_list:
            # print(blank_name in filename)
            if blank_name.lower() in filename.lower():
                shutil.copy(input_directory/filename, output_directory/blank/filename)
                list_of_files_copied.append(filename)
        # thorium standards
        for thstd_name in thstd_start_activity_dict.keys():
            # print(thstd_name.lower() in filename.lower())
            if thstd_name.lower() in filename.lower():
                shutil.copy(input_directory/filename, output_directory/thstd/filename)
                list_of_files_copied.append(filename)
        # actinium standards
        for acstd_name in acstd_date_dict.keys():
            # print(acstd_name in filename)
            if acstd_name.lower() in filename.lower():
                shutil.copy(input_directory/filename, output_directory/acstd/filename)
                list_of_files_copied.append(filename)
        # samples
        if linear_data_type == False:
            for i in range(len(log_df)):
                if log_df[sample_variable].iloc[i].lower() in filename.lower() and str(log_df[sub_sample_variable].iloc[i]).lower() in filename.lower():
                    shutil.copy(input_directory/filename, output_directory/'Read_Files'/log_df[sample_variable].iloc[i]/str(log_df[sub_sample_variable].iloc[i])/filename)
                    list_of_files_copied.append(filename)
        if linear_data_type == True:
            for i in range(len(log_df)):
                if log_df[sample_variable].iloc[i].lower() in filename.lower():
                    shutil.copy(input_directory/filename, output_directory/'Read_Files'/log_df[sample_variable].iloc[i]/filename)
                    list_of_files_copied.append(filename)
    
    list_of_uncopied_files = list(set(list_of_input_files)-set(list_of_files_copied))
    for filename in list_of_uncopied_files:
        shutil.copy(input_directory/filename, output_directory/'Misc'/filename)
            
    
