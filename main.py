#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Deepin, Inc.
#               2014 Xu FaSheng
#
# Author:     Xu FaSheng <fasheng.xu@gmail.com>
# Maintainer: Xu FaSheng <fasheng.xu@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import getopt
import json
import subprocess
# from PyQt5.QtCore import QApplication
from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton

config = None
ITEM_APP_NAME = "AppName"
ITEM_LOG_DETAIL = "LogDetail"
ITEM_RESTART_COMMAND = "RestartCommand"
ITEM_RESTART_ENV = "RestartEnv"
ITEM_RESTART_DIRECTORY = "RestartDirectory"

def show_usage():
    print("deepin-crash-reporter <-h|--help> <-c|--config> jsonfile")

def parse_config(config_file):
    config = None
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
    except IOError:
        print("Open file failed: %s" % config_file)
    except:
        print("Unexpected error:", sys.exc_info()[0])
    return config
    
def on_click_restart():
    global config
    print("restart: %s" % config[ITEM_RESTART_COMMAND] )
    try:
        subprocess.Popen(config[ITEM_RESTART_COMMAND], cwd=config[ITEM_RESTART_DIRECTORY],
                         env=config[ITEM_RESTART_ENV])
    except:
        print("Unexpected error:", sys.exc_info()[0])
        
# TODO
def on_click_report():
    global config
    print("report: %s" % config[ITEM_APP_NAME] )

def main():
    # dispatch arguments
    config_file = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc:", ["help=", "config="])
    except getopt.GetoptError:
        show_usage()
        sys.exit(2)
    if len(opts) == 0:
        show_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            show_usage()
            sys.exit()
        elif opt in ("-c", "--config"):
            config_file = arg
    
    global config
    config = parse_config(config_file)
    if config == None:
        show_usage()
        sys.exit(1)
            
    # show message dialog
    dialog = QMessageBox(QMessageBox.Critical, "Deepin Crash Reporter", 'We are sorry, application "%s" was crashed, you can restart it or give a report to us.' % config[ITEM_APP_NAME] )
    detail = "Restart command: {0}\nEnvironment variables: {1} \nWorking directory: {2}\nLog detail:\n{3}".format(
        config[ITEM_RESTART_COMMAND], config[ITEM_RESTART_ENV], config[ITEM_RESTART_DIRECTORY], config[ITEM_LOG_DETAIL])
    dialog.setDetailedText(detail)
    
    restart = QPushButton("Restart")
    restart.clicked.connect(on_click_restart)
    report = QPushButton("Report")
    report.clicked.connect(on_click_report)
    
    dialog.addButton(restart, QMessageBox.ResetRole)
    dialog.addButton(report, QMessageBox.YesRole)
    dialog.addButton("Close", QMessageBox.NoRole)
    dialog.exec_()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # change to real path
    root_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(root_dir)
    
    main()
