# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyminer_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ui(object):
    def setupUi(self, ui):
        ui.setObjectName("ui")
        ui.resize(1009, 687)
        self.centralwidget = QtWidgets.QWidget(ui)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.rs = QtWidgets.QWidget()
        self.rs.setObjectName("rs")
        self.widget = QtWidgets.QWidget(self.rs)
        self.widget.setGeometry(QtCore.QRect(10, 10, 961, 581))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.scan = QtWidgets.QPushButton(self.widget)
        self.scan.setObjectName("scan")
        self.horizontalLayout_4.addWidget(self.scan)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gen = QtWidgets.QPushButton(self.widget)
        self.gen.setObjectName("gen")
        self.horizontalLayout_3.addWidget(self.gen)
        self.gen_all = QtWidgets.QPushButton(self.widget)
        self.gen_all.setObjectName("gen_all")
        self.horizontalLayout_3.addWidget(self.gen_all)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.clear = QtWidgets.QPushButton(self.widget)
        self.clear.setObjectName("clear")
        self.horizontalLayout_3.addWidget(self.clear)
        self.clear_outdated = QtWidgets.QPushButton(self.widget)
        self.clear_outdated.setObjectName("clear_outdated")
        self.horizontalLayout_3.addWidget(self.clear_outdated)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.rs, "")
        self.ds = QtWidgets.QWidget()
        self.ds.setObjectName("ds")
        self.widget1 = QtWidgets.QWidget(self.ds)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 961, 581))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line_11 = QtWidgets.QFrame(self.widget1)
        self.line_11.setLineWidth(4)
        self.line_11.setMidLineWidth(4)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_3.addWidget(self.line_11, 6, 0, 1, 1)
        self.ptc_img2 = QtWidgets.QLineEdit(self.widget1)
        self.ptc_img2.setObjectName("ptc_img2")
        self.gridLayout_3.addWidget(self.ptc_img2, 12, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 12, 0, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.widget1)
        self.line_9.setLineWidth(4)
        self.line_9.setMidLineWidth(4)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_3.addWidget(self.line_9, 14, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget1)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 8, 0, 1, 1)
        self.probe_out_file = QtWidgets.QLineEdit(self.widget1)
        self.probe_out_file.setObjectName("probe_out_file")
        self.gridLayout_3.addWidget(self.probe_out_file, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 11, 0, 1, 1)
        self.pde_run = QtWidgets.QPushButton(self.widget1)
        self.pde_run.setObjectName("pde_run")
        self.gridLayout_3.addWidget(self.pde_run, 4, 3, 1, 1)
        self.pcf_open = QtWidgets.QPushButton(self.widget1)
        self.pcf_open.setObjectName("pcf_open")
        self.gridLayout_3.addWidget(self.pcf_open, 3, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 14, 1, 1, 1)
        self.dol_open = QtWidgets.QPushButton(self.widget1)
        self.dol_open.setObjectName("dol_open")
        self.gridLayout_3.addWidget(self.dol_open, 2, 3, 1, 1)
        self.ptc_2_frame_run = QtWidgets.QPushButton(self.widget1)
        self.ptc_2_frame_run.setObjectName("ptc_2_frame_run")
        self.gridLayout_3.addWidget(self.ptc_2_frame_run, 13, 3, 1, 1)
        self.cps_run = QtWidgets.QPushButton(self.widget1)
        self.cps_run.setObjectName("cps_run")
        self.gridLayout_3.addWidget(self.cps_run, 16, 3, 1, 1)
        self.ptc_img1 = QtWidgets.QLineEdit(self.widget1)
        self.ptc_img1.setObjectName("ptc_img1")
        self.gridLayout_3.addWidget(self.ptc_img1, 11, 1, 1, 1)
        self.ptc_n_frame_run = QtWidgets.QPushButton(self.widget1)
        self.ptc_n_frame_run.setObjectName("ptc_n_frame_run")
        self.gridLayout_3.addWidget(self.ptc_n_frame_run, 9, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 10, 1, 1, 1)
        self.download = QtWidgets.QCheckBox(self.widget1)
        self.download.setChecked(True)
        self.download.setObjectName("download")
        self.gridLayout_3.addWidget(self.download, 1, 3, 1, 1)
        self.cps_open = QtWidgets.QPushButton(self.widget1)
        self.cps_open.setObjectName("cps_open")
        self.gridLayout_3.addWidget(self.cps_open, 15, 3, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.widget1)
        self.line_10.setLineWidth(4)
        self.line_10.setMidLineWidth(4)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_3.addWidget(self.line_10, 10, 0, 1, 1)
        self.data_output_loc = QtWidgets.QLineEdit(self.widget1)
        self.data_output_loc.setObjectName("data_output_loc")
        self.gridLayout_3.addWidget(self.data_output_loc, 2, 1, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.widget1)
        self.line_12.setLineWidth(4)
        self.line_12.setMidLineWidth(4)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout_3.addWidget(self.line_12, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 15, 0, 1, 1)
        self.custom_python_script = QtWidgets.QLineEdit(self.widget1)
        self.custom_python_script.setObjectName("custom_python_script")
        self.gridLayout_3.addWidget(self.custom_python_script, 15, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.probe_cfg_file = QtWidgets.QLineEdit(self.widget1)
        self.probe_cfg_file.setObjectName("probe_cfg_file")
        self.horizontalLayout_5.addWidget(self.probe_cfg_file)
        self.pcf_edit = QtWidgets.QPushButton(self.widget1)
        self.pcf_edit.setObjectName("pcf_edit")
        self.horizontalLayout_5.addWidget(self.pcf_edit)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.ptc_img2_open = QtWidgets.QPushButton(self.widget1)
        self.ptc_img2_open.setObjectName("ptc_img2_open")
        self.gridLayout_3.addWidget(self.ptc_img2_open, 12, 3, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.widget1)
        self.label_1.setObjectName("label_1")
        self.gridLayout_3.addWidget(self.label_1, 1, 0, 1, 1)
        self.ptc_img1_open = QtWidgets.QPushButton(self.widget1)
        self.ptc_img1_open.setObjectName("ptc_img1_open")
        self.gridLayout_3.addWidget(self.ptc_img1_open, 11, 3, 1, 1)
        self.ptc_file_filter = QtWidgets.QLineEdit(self.widget1)
        self.ptc_file_filter.setObjectName("ptc_file_filter")
        self.gridLayout_3.addWidget(self.ptc_file_filter, 8, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 7, 0, 1, 1)
        self.pdd_open = QtWidgets.QPushButton(self.widget1)
        self.pdd_open.setObjectName("pdd_open")
        self.gridLayout_3.addWidget(self.pdd_open, 7, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 6, 1, 1, 1)
        self.ptc_data_dir = QtWidgets.QLineEdit(self.widget1)
        self.ptc_data_dir.setObjectName("ptc_data_dir")
        self.gridLayout_3.addWidget(self.ptc_data_dir, 7, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.tabWidget.addTab(self.ds, "")
        self.cr = QtWidgets.QWidget()
        self.cr.setObjectName("cr")
        self.widget2 = QtWidgets.QWidget(self.cr)
        self.widget2.setGeometry(QtCore.QRect(10, 10, 961, 581))
        self.widget2.setObjectName("widget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.crunch_cfg_open = QtWidgets.QPushButton(self.widget2)
        self.crunch_cfg_open.setObjectName("crunch_cfg_open")
        self.gridLayout_4.addWidget(self.crunch_cfg_open, 1, 2, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_4.addWidget(self.lineEdit_12, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.widget2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 6, 0, 1, 1)
        self.data_crunch = QtWidgets.QPushButton(self.widget2)
        self.data_crunch.setObjectName("data_crunch")
        self.gridLayout_4.addWidget(self.data_crunch, 3, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.widget2)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 12, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plot_type_plot = QtWidgets.QRadioButton(self.widget2)
        self.plot_type_plot.setChecked(True)
        self.plot_type_plot.setObjectName("plot_type_plot")
        self.buttonGroup = QtWidgets.QButtonGroup(ui)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.plot_type_plot)
        self.horizontalLayout_2.addWidget(self.plot_type_plot)
        self.plot_type_boxplot = QtWidgets.QRadioButton(self.widget2)
        self.plot_type_boxplot.setObjectName("plot_type_boxplot")
        self.buttonGroup.addButton(self.plot_type_boxplot)
        self.horizontalLayout_2.addWidget(self.plot_type_boxplot)
        self.plot_type_barplot = QtWidgets.QRadioButton(self.widget2)
        self.plot_type_barplot.setObjectName("plot_type_barplot")
        self.buttonGroup.addButton(self.plot_type_barplot)
        self.horizontalLayout_2.addWidget(self.plot_type_barplot)
        self.plot_type_heatmap = QtWidgets.QRadioButton(self.widget2)
        self.plot_type_heatmap.setObjectName("plot_type_heatmap")
        self.buttonGroup.addButton(self.plot_type_heatmap)
        self.horizontalLayout_2.addWidget(self.plot_type_heatmap)
        self.plot_type_hist = QtWidgets.QRadioButton(self.widget2)
        self.plot_type_hist.setChecked(False)
        self.plot_type_hist.setObjectName("plot_type_hist")
        self.buttonGroup.addButton(self.plot_type_hist)
        self.horizontalLayout_2.addWidget(self.plot_type_hist)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 7, 1, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_29 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_11.addWidget(self.label_29)
        self.pywebify = QtWidgets.QRadioButton(self.widget2)
        self.pywebify.setChecked(True)
        self.pywebify.setObjectName("pywebify")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(ui)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.pywebify)
        self.horizontalLayout_11.addWidget(self.pywebify)
        self.simple_report = QtWidgets.QRadioButton(self.widget2)
        self.simple_report.setObjectName("simple_report")
        self.buttonGroup_3.addButton(self.simple_report)
        self.horizontalLayout_11.addWidget(self.simple_report)
        self.gridLayout_4.addLayout(self.horizontalLayout_11, 18, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 5, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.plot_groups = QtWidgets.QLineEdit(self.widget2)
        self.plot_groups.setObjectName("plot_groups")
        self.horizontalLayout_9.addWidget(self.plot_groups)
        self.label_4 = QtWidgets.QLabel(self.widget2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.plot_wrap = QtWidgets.QLineEdit(self.widget2)
        self.plot_wrap.setObjectName("plot_wrap")
        self.horizontalLayout_9.addWidget(self.plot_wrap)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 10, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_30 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_6.addWidget(self.label_30)
        self.pixel_crunch_select = QtWidgets.QRadioButton(self.widget2)
        self.pixel_crunch_select.setChecked(True)
        self.pixel_crunch_select.setObjectName("pixel_crunch_select")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(ui)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.pixel_crunch_select)
        self.horizontalLayout_6.addWidget(self.pixel_crunch_select)
        self.mini_crunch_select = QtWidgets.QRadioButton(self.widget2)
        self.mini_crunch_select.setChecked(False)
        self.mini_crunch_select.setObjectName("mini_crunch_select")
        self.buttonGroup_2.addButton(self.mini_crunch_select)
        self.horizontalLayout_6.addWidget(self.mini_crunch_select)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.plot_custom = QtWidgets.QLineEdit(self.widget2)
        self.plot_custom.setObjectName("plot_custom")
        self.gridLayout_4.addWidget(self.plot_custom, 16, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.widget2)
        self.label_31.setObjectName("label_31")
        self.gridLayout_4.addWidget(self.label_31, 19, 0, 1, 1)
        self.report_gen = QtWidgets.QPushButton(self.widget2)
        self.report_gen.setObjectName("report_gen")
        self.gridLayout_4.addWidget(self.report_gen, 19, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.widget2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 13, 0, 1, 1)
        self.data_folder_open = QtWidgets.QPushButton(self.widget2)
        self.data_folder_open.setObjectName("data_folder_open")
        self.gridLayout_4.addWidget(self.data_folder_open, 2, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 1, 0, 1, 1)
        self.plot_data_file = QtWidgets.QLineEdit(self.widget2)
        self.plot_data_file.setObjectName("plot_data_file")
        self.gridLayout_4.addWidget(self.plot_data_file, 5, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 4, 1, 1, 1)
        self.plot_plot = QtWidgets.QPushButton(self.widget2)
        self.plot_plot.setObjectName("plot_plot")
        self.gridLayout_4.addWidget(self.plot_plot, 17, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.plot_x = QtWidgets.QLineEdit(self.widget2)
        self.plot_x.setObjectName("plot_x")
        self.horizontalLayout_7.addWidget(self.plot_x)
        self.label_33 = QtWidgets.QLabel(self.widget2)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_7.addWidget(self.label_33)
        self.plot_y = QtWidgets.QLineEdit(self.widget2)
        self.plot_y.setObjectName("plot_y")
        self.horizontalLayout_7.addWidget(self.plot_y)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 8, 1, 1, 1)
        self.plot_fig_groups = QtWidgets.QLineEdit(self.widget2)
        self.plot_fig_groups.setObjectName("plot_fig_groups")
        self.gridLayout_4.addWidget(self.plot_fig_groups, 6, 1, 1, 1)
        self.plot_legend = QtWidgets.QLineEdit(self.widget2)
        self.plot_legend.setObjectName("plot_legend")
        self.gridLayout_4.addWidget(self.plot_legend, 12, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.widget2)
        self.label_28.setObjectName("label_28")
        self.gridLayout_4.addWidget(self.label_28, 15, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.widget2)
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 9, 0, 1, 1)
        self.plot_data_open = QtWidgets.QPushButton(self.widget2)
        self.plot_data_open.setObjectName("plot_data_open")
        self.gridLayout_4.addWidget(self.plot_data_open, 5, 2, 1, 1)
        self.plot_filter = QtWidgets.QLineEdit(self.widget2)
        self.plot_filter.setObjectName("plot_filter")
        self.gridLayout_4.addWidget(self.plot_filter, 13, 1, 1, 1)
        self.plot_filename = QtWidgets.QLineEdit(self.widget2)
        self.plot_filename.setObjectName("plot_filename")
        self.gridLayout_4.addWidget(self.plot_filename, 15, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.plot_row = QtWidgets.QLineEdit(self.widget2)
        self.plot_row.setObjectName("plot_row")
        self.horizontalLayout_8.addWidget(self.plot_row)
        self.label_34 = QtWidgets.QLabel(self.widget2)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_8.addWidget(self.label_34)
        self.plot_col = QtWidgets.QLineEdit(self.widget2)
        self.plot_col.setObjectName("plot_col")
        self.horizontalLayout_8.addWidget(self.plot_col)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 9, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.crunch_replot = QtWidgets.QPushButton(self.widget2)
        self.crunch_replot.setMaximumSize(QtCore.QSize(70, 16777215))
        self.crunch_replot.setObjectName("crunch_replot")
        self.horizontalLayout_10.addWidget(self.crunch_replot)
        self.gridLayout_4.addLayout(self.horizontalLayout_10, 3, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.widget2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 7, 0, 1, 1)
        self.report_folder = QtWidgets.QLineEdit(self.widget2)
        self.report_folder.setObjectName("report_folder")
        self.gridLayout_4.addWidget(self.report_folder, 19, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.widget2)
        self.label_32.setObjectName("label_32")
        self.gridLayout_4.addWidget(self.label_32, 16, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.widget2)
        self.label_27.setObjectName("label_27")
        self.gridLayout_4.addWidget(self.label_27, 14, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.crunch_cfg_file = QtWidgets.QLineEdit(self.widget2)
        self.crunch_cfg_file.setObjectName("crunch_cfg_file")
        self.horizontalLayout.addWidget(self.crunch_cfg_file)
        self.crunch_cfg_edit = QtWidgets.QPushButton(self.widget2)
        self.crunch_cfg_edit.setObjectName("crunch_cfg_edit")
        self.horizontalLayout.addWidget(self.crunch_cfg_edit)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.widget2)
        self.label_26.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_26, 10, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.widget2)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 8, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 2, 0, 1, 1)
        self.plot_title = QtWidgets.QLineEdit(self.widget2)
        self.plot_title.setObjectName("plot_title")
        self.gridLayout_4.addWidget(self.plot_title, 14, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.widget2)
        self.line_2.setLineWidth(4)
        self.line_2.setMidLineWidth(4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.widget2)
        self.line.setLineWidth(4)
        self.line.setMidLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 4, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.widget2)
        self.line_3.setLineWidth(4)
        self.line_3.setMidLineWidth(4)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 18, 0, 1, 1)
        self.tabWidget.addTab(self.cr, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.status)
        ui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ui)
        self.statusbar.setObjectName("statusbar")
        ui.setStatusBar(self.statusbar)

        self.retranslateUi(ui)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(ui)

    def retranslateUi(self, ui):
        _translate = QtCore.QCoreApplication.translate
        ui.setWindowTitle(_translate("ui", "MainWindow"))
        self.scan.setText(_translate("ui", "Scan For Available Scripts"))
        self.gen.setText(_translate("ui", "Generate Selected"))
        self.gen_all.setText(_translate("ui", "Generate All"))
        self.pushButton.setText(_translate("ui", "Edit Config"))
        self.clear.setText(_translate("ui", "Clear Selected"))
        self.clear_outdated.setText(_translate("ui", "Clear Outdated"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rs), _translate("ui", "Regrind Script"))
        self.label_11.setText(_translate("ui", "Image 2"))
        self.label_12.setText(_translate("ui", "File Filter String"))
        self.label_2.setText(_translate("ui", "Image 1"))
        self.pde_run.setText(_translate("ui", "Run"))
        self.pcf_open.setText(_translate("ui", "Open"))
        self.label_10.setText(_translate("ui", "Custom Python Script"))
        self.dol_open.setText(_translate("ui", "Open"))
        self.ptc_2_frame_run.setText(_translate("ui", "Run"))
        self.cps_run.setText(_translate("ui", "Run"))
        self.ptc_n_frame_run.setText(_translate("ui", "Run"))
        self.label_9.setText(_translate("ui", "PTC 2 Frame"))
        self.download.setText(_translate("ui", "Save"))
        self.cps_open.setText(_translate("ui", "Open"))
        self.label_5.setText(_translate("ui", "Probe Config File"))
        self.label_7.setText(_translate("ui", "Probe Data Extraction"))
        self.label_6.setText(_translate("ui", "Script Path"))
        self.pcf_edit.setText(_translate("ui", "Edit"))
        self.ptc_img2_open.setText(_translate("ui", "Open"))
        self.label_1.setText(_translate("ui", "Probe Output Location"))
        self.ptc_img1_open.setText(_translate("ui", "Open"))
        self.label.setText(_translate("ui", "Folder"))
        self.pdd_open.setText(_translate("ui", "Open"))
        self.label_8.setText(_translate("ui", "PTC N Frame"))
        self.label_3.setText(_translate("ui", "Data Output Location"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ds), _translate("ui", "Data Extraction"))
        self.crunch_cfg_open.setText(_translate("ui", "Open"))
        self.label_21.setText(_translate("ui", "Fig Groups"))
        self.data_crunch.setText(_translate("ui", "Crunch"))
        self.label_22.setText(_translate("ui", "legend"))
        self.plot_type_plot.setText(_translate("ui", "Plot"))
        self.plot_type_boxplot.setText(_translate("ui", "Boxplot"))
        self.plot_type_barplot.setText(_translate("ui", "Barplot"))
        self.plot_type_heatmap.setText(_translate("ui", "Heat Map"))
        self.plot_type_hist.setText(_translate("ui", "Histogram"))
        self.label_29.setText(_translate("ui", "Reporting"))
        self.pywebify.setText(_translate("ui", "Pywebify"))
        self.simple_report.setText(_translate("ui", "Simple Report"))
        self.label_20.setText(_translate("ui", "Data File"))
        self.label_4.setText(_translate("ui", "Wrap"))
        self.label_30.setText(_translate("ui", "Cruncher"))
        self.pixel_crunch_select.setText(_translate("ui", "Pixel Crunch"))
        self.mini_crunch_select.setText(_translate("ui", "Mini Crunch"))
        self.label_31.setText(_translate("ui", "Folder"))
        self.report_gen.setText(_translate("ui", "Report"))
        self.label_19.setText(_translate("ui", "Filter"))
        self.data_folder_open.setText(_translate("ui", "Open"))
        self.label_15.setText(_translate("ui", "Config File"))
        self.label_18.setText(_translate("ui", "Plotting - Five Cent Plots"))
        self.plot_plot.setText(_translate("ui", "Plot"))
        self.label_33.setText(_translate("ui", "Y"))
        self.label_28.setText(_translate("ui", "Filename"))
        self.label_25.setText(_translate("ui", "Row"))
        self.plot_data_open.setText(_translate("ui", "Open"))
        self.label_34.setText(_translate("ui", "Col"))
        self.crunch_replot.setText(_translate("ui", "Replot"))
        self.label_23.setText(_translate("ui", "Plot Type"))
        self.label_32.setText(_translate("ui", "Custom"))
        self.label_27.setText(_translate("ui", "Title"))
        self.crunch_cfg_edit.setText(_translate("ui", "Edit"))
        self.label_26.setText(_translate("ui", "Groups"))
        self.label_24.setText(_translate("ui", "X"))
        self.label_16.setText(_translate("ui", "Data Folder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cr), _translate("ui", "Crunch"))
        self.status.setText(_translate("ui", "Status"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = QtWidgets.QMainWindow()
    ui = Ui_ui()
    ui.setupUi(ui)
    ui.show()
    sys.exit(app.exec_())
