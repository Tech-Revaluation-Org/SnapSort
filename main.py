from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QVBoxLayout, QHBoxLayout, QFileDialog
import os

class SnapSortUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("SnapSort - Smart File Organizer")
        self.setGeometry(500, 200, 800, 600)
        
        self.file_list = QListWidget()
        self.log_label = QLabel("Action Log:")
        
        self.sort_btn = QPushButton("Sort Files")
        self.rules_btn = QPushButton("Set Rules")
        self.duplicates_btn = QPushButton("Find Duplicates")
        self.rename_btn = QPushButton("Bulk Rename")
        self.setting_btn = QPushButton("Settings")
        
        self.sort_btn.clicked.connect(self.sort_files)
        self.rules_btn.clicked.connect(self.set_rules)
        self.duplicates_btn.clicked.connect(self.find_duplicates)
        self.rename_btn.clicked.connect(self.bulk_rename)
        self.setting_btn.clicked.connect(self.open_settings)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.sort_btn)
        button_layout.addWidget(self.rules_btn)
        button_layout.addWidget(self.duplicates_btn)
        button_layout.addWidget(self.rename_btn)
        button_layout.addWidget(self.setting_btn)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Files:"))
        main_layout.addWidget(self.file_list)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.log_label)
        
        self.setLayout(main_layout)
        
        self.load_files()
    
    def load_files(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.file_list.clear()
            for file in os.listdir(folder):
                self.file_list.addItem(file)
            self.log_label.setText(f"Loaded files from: {folder}")
    
    def sort_files(self):
        self.log_label.setText("Sorting files...")
        # Add sorting logic here
    
    def set_rules(self):
        self.log_label.setText("Opening rule settings...")
        # Add rule setting logic here
    
    def find_duplicates(self):
        self.log_label.setText("Scanning for duplicates...")
        # Add duplicate finding logic here
    
    def bulk_rename(self):
        self.log_label.setText("Renaming files...")
        # Add bulk renaming logic here
    
    def open_settings(self):
        self.log_label.setText("Opening settings...")
        # Add settings logic here

if __name__ == "__main__":
    app = QApplication([])
    window = SnapSortUI()
    window.show()
    app.exec_()