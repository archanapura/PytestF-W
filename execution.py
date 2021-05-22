from multiprocessing import Process
import os
import subprocess


def start_execution2(test_name):
    os.system("cd C:\\Users\\archa\\PycharmProjects\\pytestLearnTest")
    os.system("pytest -s --alluredir=./results")
    #os.system("pytest -m markName --alluredir=./results")
    os.system("allure serve ./results")

if __name__ == "__main__":

    names = ['Test_Case_A.py', 'Test_Case_A.py']
    procs = []

    for name in names:
        proc = Process(target=start_execution2, args=(name,))
        procs.append(proc)

    for proc in procs:
        proc.start()
        proc.join()