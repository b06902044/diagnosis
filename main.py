import protocol
import utils
import os
import time
import argparse
from selenium import webdriver

def getProtocol(user, password):
    cwd = os.getcwd()
    driver = webdriver.Firefox(executable_path = cwd + "/geckodriver")
    return protocol.Protocol(driver, user, password)

def getArgs():
    parser = argparse.ArgumentParser(description='Automatically protocol processer')
    parser.add_argument(
        '--time-gap', '-t', type=int, default=10,
        help='the time gap(minutes) to execute this process'
    )
    parser.add_argument(
        '--user', '-u', default="G806", help='user to login the portal'
    )
    parser.add_argument(
        '--password', '-p', default="G000000", help='password to login the portal'
    )
    args = parser.parse_args()
    
    return args.time_gap, args.user, args.password

if __name__ == '__main__':
    time_gap, user, password = getArgs()
    utils.init()
    
    while True:
        p = getProtocol(user, password)
        p.login()
        p.switch_to_main_page()
        p.do()
        p.quit()
        
        print("mission completed, sleep for %d minutes" % time_gap)
        time.sleep(60 * time_gap)
    
    