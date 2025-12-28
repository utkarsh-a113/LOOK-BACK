import os

def print_directory_contents(path='/'):
    """
    Prints the names of all entries (files and directories)
    found in the given directory.

    :param path: Path to the directory (defaults to current directory)
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
        return
    except OSError as e:
        print(f"Error: {e}")
        return

    print(f"Contents of directory '{path}':")
    for entry in entries:
        print(entry)

if __name__ == "__main__":
    import sys
    dir_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    print_directory_contents(dir_path)
