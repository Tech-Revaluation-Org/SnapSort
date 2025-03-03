import os
import hashlib
from collections import defaultdict
from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QTextBrowser, QTabWidget, QListWidget, QFileDialog, QMessageBox
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class FileAnalysisDialog(QDialog):
    def __init__(self, folder_path, parent=None):
        super().__init__(parent)
        self.folder_path = folder_path
        self.setWindowTitle("File Analysis")
        self.setMinimumSize(800, 600)
        self.init_ui()
        self.analyze_files()

    def init_ui(self):
        layout = QVBoxLayout()
        self.tabs = QTabWidget()
        
        # Summary Tab
        self.summary_browser = QTextBrowser()
        self.tabs.addTab(self.summary_browser, "Summary")
        
        # File Types Tab
        self.type_canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.tabs.addTab(self.type_canvas, "File Types")
        
        # Size Distribution Tab
        self.size_canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.tabs.addTab(self.size_canvas, "Size Distribution")
        
        # File Hashes Tab
        self.hash_list = QListWidget()
        self.tabs.addTab(self.hash_list, "File Hashes")
        
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def analyze_files(self):
        file_types = defaultdict(int)
        sizes = []
        total_size = 0
        file_hashes = []

        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                path = os.path.join(root, file)
                size = os.path.getsize(path)
                file_type = os.path.splitext(file)[1].lower() or "No Extension"
                file_types[file_type] += 1
                sizes.append(size / (1024 * 1024))  # Convert to MB
                total_size += size
                
                # Calculate file hash
                file_hash = self.calculate_file_hash(path)
                file_hashes.append((file, file_hash))

        # Summary Tab
        summary = f"""
        Total Files: {sum(file_types.values())}
        Total Folders: {sum([len(dirs) for root, dirs, files in os.walk(self.folder_path)])}
        Total Size: {self.format_size(total_size)}
        Unique Extensions: {len(file_types)}
        """
        self.summary_browser.setText(summary)

        # File Types Chart
        self.plot_file_types(file_types)

        # Size Distribution Chart
        self.plot_size_distribution(sizes)

        # File Hashes
        self.display_file_hashes(file_hashes)

    def calculate_file_hash(self, file_path):
        """Calculate SHA-256 hash of a file."""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()

    def plot_file_types(self, file_types):
        """Plot file type distribution."""
        fig = self.type_canvas.figure
        fig.clear()
        ax = fig.add_subplot(111)
        labels = [ext if count > 0 else '' for ext, count in file_types.items()]
        ax.pie(file_types.values(), labels=labels, autopct='%1.1f%%')
        ax.set_title("File Type Distribution")
        self.type_canvas.draw()

    def plot_size_distribution(self, sizes):
        """Plot size distribution."""
        fig = self.size_canvas.figure
        fig.clear()
        ax = fig.add_subplot(111)
        ax.hist(sizes, bins=20, edgecolor='black')
        ax.set_xlabel("File Size (MB)")
        ax.set_ylabel("Count")
        ax.set_title("Size Distribution")
        self.size_canvas.draw()

    def display_file_hashes(self, file_hashes):
        """Display file hashes in the list widget."""
        self.hash_list.clear()
        for file_name, file_hash in file_hashes:
            self.hash_list.addItem(f"{file_name}: {file_hash}")

    def format_size(self, size):
        """Format size in a human-readable way."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} TB"

# Example usage of the enhanced FileAnalysisDialog
if __name__ == "__main__":
    app = QApplication([])
    folder_path = QFileDialog.getExistingDirectory(None, "Select Folder")
    if folder_path:
        dialog = FileAnalysisDialog(folder_path)
        dialog.exec_()
    app.exec_()
