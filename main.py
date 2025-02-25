from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox
import os, shutil
from collections import defaultdict

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
            self.folder_path = folder
            self.file_list.clear()
            for file in os.listdir(folder):
                self.file_list.addItem(file)
            self.log_label.setText(f"Loaded files from: {folder}")
    
    def sort_files(self):
        if hasattr(self, 'folder_path'):
            self.log_label.setText("Sorting files...")
            extensions = {"Images": [".jpg", ".png", ".gif"],
                          "Documents": [".pdf", ".docx", ".txt"],
                          "Videos": [".mp4", ".avi", ".mkv"],
                          "Music": [".mp3", ".wav"]}
            
            for category, exts in extensions.items():
                category_path = os.path.join(self.folder_path, category)
                if not os.path.exists(category_path):
                    os.makedirs(category_path)
                
                for file in os.listdir(self.folder_path):
                    file_path = os.path.join(self.folder_path, file)
                    if os.path.isfile(file_path) and any(file.lower().endswith(ext) for ext in exts):
                        shutil.move(file_path, os.path.join(category_path, file))
            
            self.load_files()
            self.log_label.setText("Sorting completed.")
        else:
            self.log_label.setText("No folder selected.")
    
    def set_rules(self):
        self.log_label.setText("Opening rule settings...")
        # Add rule setting logic here
    
    def find_duplicates(self):
        if hasattr(self, 'folder_path'):
            self.log_label.setText("Scanning for duplicates...")
            file_hashes = defaultdict(list)
            
            for file in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, file)
                if os.path.isfile(file_path):
                    file_hashes[file].append(file_path)
            
            duplicates = {k: v for k, v in file_hashes.items() if len(v) > 1}
            
            if duplicates:
                self.log_label.setText("Duplicates found! Check logs.")
                QMessageBox.information(self, "Duplicates Found", "Duplicate files detected!")
            else:
                self.log_label.setText("No duplicates found.")
        else:
            self.log_label.setText("No folder selected.")
    
    def bulk_rename(self):
        if hasattr(self, 'folder_path'):
            self.log_label.setText("Renaming files...")
            count = 1
            
            for file in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, file)
                if os.path.isfile(file_path):
                    file_extension = os.path.splitext(file)[1]
                    new_name = f"Renamed_File_{count}{file_extension}"
                    new_path = os.path.join(self.folder_path, new_name)
                    os.rename(file_path, new_path)
                    count += 1
            
            self.load_files()
            self.log_label.setText("Bulk rename completed.")
        else:
            self.log_label.setText("No folder selected.")
    
    def open_settings(self):
        QMessageBox.information(self, "Settings", "Settings window placeholder.")
        self.log_label.setText("Opened settings.")

if __name__ == "__main__":
    app = QApplication([])
    window = SnapSortUI()
    window.show()
    app.exec_()
