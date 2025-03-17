# SnapSort - Smart File Organizer

## Overview

SnapSort is a desktop application built with PyQt5 that helps users organize their files efficiently. It provides features such as automatic file sorting, duplicate file detection, bulk renaming, and customizable settings for sorting preferences and themes.

## Features

- **Sort Files**: Automatically categorizes files based on their extensions (e.g., Images, Documents, Videos, Music).
- **Set Rules**: Allows users to define custom sorting rules (feature under development).
- **Find Duplicates**: Scans for duplicate files in a selected folder and alerts the user.
- **Bulk Rename**: Renames multiple files in a folder systematically.
- **Settings**: Enables users to choose sorting preferences (A-Z, Z-A) and switch between Light and Dark themes.

## Installation

Ensure you have Python installed. Install dependencies using:

```sh
pip install PyQt5
```

Run the application:

```sh
python snap_sort.py
```

## Usage

1. **Load Files**: Select a folder containing the files you want to manage.
2. **Sort Files**: Click the "Sort Files" button to automatically categorize files.
3. **Find Duplicates**: Click the "Find Duplicates" button to scan for duplicate files.
4. **Bulk Rename**: Click "Bulk Rename" to rename all files in the selected folder.
5. **Settings**:
   - Choose sorting order (A-Z, Z-A)
   - Change the application theme (Light/Dark)
   - Click "Save Changes" to apply settings.

## File Sorting Logic

Files are categorized into predefined folders:

- **Images**: .jpg, .png, .gif
- **Documents**: .pdf, .docx, .txt
- **Videos**: .mp4, .avi, .mkv
- **Music**: .mp3, .wav

## Duplicate Detection

The app computes MD5 hashes of files to detect duplicates. If duplicates exist, the user is notified.

## Bulk Renaming

Files are renamed sequentially as `Renamed_File_1`, `Renamed_File_2`, etc., while preserving their extensions.

## Theme Customization

Users can toggle between **Light** and **Dark** themes via the settings menu. The theme is applied dynamically.

## Future Enhancements

- Custom user-defined rules for sorting
- Enhanced duplicate detection with preview
- Drag-and-drop file support
- Multi-language support

## License

This project is open-source and available for modification and distribution.
