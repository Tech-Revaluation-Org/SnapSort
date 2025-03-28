from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox, QComboBox
from PyQt5.QtGui import QPalette, QColor
import os, shutil, hashlib
from collections import defaultdict

class SettingsWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Settings")
        self.setGeometry(550, 250, 400, 200)
        
        self.theme_label = QLabel("Select Theme:")
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Light", "Dark"])
        
        self.sort_label = QLabel("Sorting Order:")
        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["A-Z", "Z-A"])
        
        self.save_btn = QPushButton("Save Changes")
        self.save_btn.clicked.connect(self.save_changes)
        
        layout = QVBoxLayout()
        layout.addWidget(self.theme_label)
        layout.addWidget(self.theme_combo)
        layout.addWidget(self.sort_label)
        layout.addWidget(self.sort_combo)
        layout.addWidget(self.save_btn)
        
        self.setLayout(layout)
    
    def save_changes(self):
        selected_theme = self.theme_combo.currentText()
        selected_sort = self.sort_combo.currentText()
        self.parent.apply_settings(selected_theme, selected_sort)
        self.close()

class SnapSortUI(QWidget):
    def __init__(self):
        super().__init__()
        self.theme = "Light"
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
            files = os.listdir(folder)
            if hasattr(self, 'sort_order') and self.sort_order == "Z-A":
                files.sort(reverse=True)
            else:
                files.sort()
            for file in files:
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
        self.log_label.setText("Setting rules feature to be implemented.")
    
    def find_duplicates(self):
        if hasattr(self, 'folder_path'):
            self.log_label.setText("Scanning for duplicates...")
            hashes = defaultdict(list)
            
            for file in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, file)
                if os.path.isfile(file_path):
                    file_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
                    hashes[file_hash].append(file_path)
            
            duplicates = [v for v in hashes.values() if len(v) > 1]
            if duplicates:
                self.log_label.setText("Duplicate files detected! Check logs.")
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
        self.settings_window = SettingsWindow(self)
        self.settings_window.show()
    
    def apply_settings(self, theme, sort_order):
        self.sort_order = sort_order
        self.change_theme(theme)
        self.load_files()
        self.log_label.setText(f"Applied settings: Theme - {theme}, Sorting - {sort_order}")
    
    def change_theme(self, theme):
        palette = QPalette()
        if theme == "Dark":
            palette.setColor(QPalette.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        else:
            palette.setColor(QPalette.Window, QColor(255, 255, 255))
            palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        QApplication.instance().setPalette(palette)

if __name__ == "__main__":
    app = QApplication([])
    window = SnapSortUI()
    window.show()
    app.exec_()
