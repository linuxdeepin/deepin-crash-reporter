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
# from PyQt5.QtCore import QApplication
from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton

def onClickRestart():
    print("restart")

# TODO
def onClickReport():
    print("report")

def main():
    root_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(root_dir)

    app = QApplication(sys.argv)
    # QMessageBox.information(None, "Success!",
                            # "Hello \"%s\"!")
    # QMessageBox.
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
    # print(dialog.show())
    
    
    # QMessageBox msgBox(QMessageBox::Warning, tr("QMessageBox::warning()"),
    #                    MESSAGE, 0, this);
    # msgBox.setDetailedText(MESSAGE_DETAILS);
    # msgBox.addButton(tr("Save &Again"), QMessageBox::AcceptRole);
    # msgBox.addButton(tr("&Continue"), QMessageBox::RejectRole);
    # if (msgBox.exec() == QMessageBox::AcceptRole)
    #     warningLabel->setText(tr("Save Again"));
    # else
    #     warningLabel->setText(tr("Continue"));

    # sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
