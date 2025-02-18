from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QVBoxLayout, QHBoxLayout

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

if __name__ == "__main__":
    app = QApplication([])
    window = SnapSortUI()
    window.show()
    app.exec_()
