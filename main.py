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
# from PyQt5.QtCore import QApplication
from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton

def showUsage():
    print("deepin-crash-reporter <-h|--help> <-l|--logid> logid")

def onClickRestart():
    print("restart")

# TODO
def onClickReport():
    print("report")

def main():
    # dispatch arguments
    logid = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hl:", ["help=", "logid="])
    except getopt.GetoptError:
        showUsage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            showUsage()
            sys.exit()
        elif opt in ("-l", "--logid"):
            logid = arg
    
    app = QApplication(sys.argv)
    
    # change to real path
    root_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(root_dir)
    
    # TODO get detail log
    
    # show message dialog
    dialog = QMessageBox(QMessageBox.Critical, "Deepin Crash Reporter", "hhh")
    dialog.setDetailedText("hahahaha")
    
    restart = QPushButton("Restart")
    restart.clicked.connect(onClickRestart)
    report = QPushButton("Report")
    report.clicked.connect(onClickReport)
    
    # dialog.addButton("Restart", QMessageBox.YesRole)
    dialog.addButton(restart, QMessageBox.ResetRole)
    dialog.addButton(report, QMessageBox.YesRole)
    dialog.addButton("Close", QMessageBox.NoRole)
    print(dialog.exec_())
    
if __name__ == '__main__':
    main()
