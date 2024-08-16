from cx_Freeze import setup, Executable
import sys

build_exe_options = {
    "packages": ["cv2", "mediapipe", "numpy", "math"],
    "excludes": [],
    "include_files": [],  # Add any non-Python files here
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use "Win32GUI" if you don't want a console window to appear

executables = [
    Executable(
        script="curl.py",  # Replace with your script's filename
        base=base,
        target_name="Biceps.exe",  # Name of the executable
    )
]

setup(
    name="Biceps",
    version="1.0",
    description="A simple OpenCV and MediaPipe application",
    options={"build_exe": build_exe_options},
    executables=executables,
)
