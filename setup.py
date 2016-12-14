from qpage import *
import sys

def error_handler():
    close_files() # Close all of the open files
    vector_2 = error_finder() # load error and pass vector
    error_vector = vector_2[0] # extract errors
    pass_vector = vector_2[1] # extract pass
    print(str(len(error_vector)) + " Error") # print  number of errors
    print("Please Check Following :\n")
    for i in range(len(error_vector)): # print errors
        print(str(i + 1) + "-" + error_vector[i]) # print pass
    for i in range(len(pass_vector)):
        print(str(i + len(error_vector) + 1) + "-" + pass_vector[i])
    enter_to_exit() # get input from user to continue
    main_handler()

def file_handler():
    for i in actual_name:
        html_init(i)  # create pages html files
    menu_writer()  # write menu for each html file
    for i in actual_name:
        contain(i)  # write contains of each page
        html_end(i)  # end tags of each page
    css_creator()  # create css file
    icon_creator()
    robot_maker()
    close_files()

def main_handler_2():
    file_handler()
    print("Homepage is ready")
    print("Upload output folder contains directly to your host")
    print("Please Don't Change HTML Files Name")
    address_print()
    print_warning()
    logger(True)
    if internet():
        server()
    browse = int(input("Preview Homepage?[1] or Not[2]"))
    if browse == 1:
        preview()
        close_files()

def response_handler(response):
    if response:
        print(
            "At least one of the folders create for the first time ,\n"
            " please put your data in proper order and run program again\n Program Reboot Automaticly in 3 Sec")
        wait_func(3)
        main_handler(False)
        sys.exit()
def sample_handler():
    response=input("Press [S] to enter sample site material runing or other keys to continue with your data")
    print_line(70)
    if response.upper()=="S":
        sample_site_download(is_sample_downloaded())
def main_handler(control_flag=True):
    try:
        response = create_folder()
        print("QPAGE By S.Haghighi & M.M.Rahimi")
        print("Version : " + version)
        address_print()
        if control_flag==True:
            version_control()
        response_handler(response)
        sample_handler()
        clear_folder(out_dir)  # clear all of files in output directory
        page_name_update()  # update page names
        main_handler_2()
    except FileNotFoundError:  # error exception in FileNotFound ( When Something Missed)
        logger(False)
        error_handler()
    except ValueError:
        print("Bad Input")
        logger(False)
        close_files()
        enter_to_exit()
        main_handler()
    except PermissionError:
        logger(False)
        print("Files Is Open By Another Program")
        close_files()
        enter_to_exit()
        main_handler()

if __name__ == "__main__":
    main_handler()

