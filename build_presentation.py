import argparse
import os
import subprocess
import sys


def build_path(*components) -> str:
    """
    Build an absolute path from individual components in an OS-agnostic way.
    
    Returns
    -------
    str
        The absolute path corresponding to the input components.
    """
    return os.path.abspath(os.path.join(*components))


def touch(file_path: str) -> None:
    """
    Python implementation of POSIX `touch` command.
    
    Parameters
    ----------
    file_path : str
        Path to the file to be created.
    
    Notes
    -----
    Adapted from https://stackoverflow.com/a/12654798.
    """
    with open(file_path, 'a'):
        os.utime(file_path)


def create_project(project_name: str, parent_dir: str) -> None:
    _project_root = build_path(parent_dir, project_name)
    _src_dir = build_path(_project_root, 'src')
    _src_images = build_path(_src_dir, 'assets', 'img')
    _presentation_dir = build_path(_project_root, 'presentation')

    _paths = (
        _project_root,
        _src_dir,
        _src_images,
        _presentation_dir,
    )

    for _path in _paths:
        # Equivalent to POSIX `mkdir -p`
        os.makedirs(_path, exist_ok=True)

    # Create empty Markdown source file with standardized name
    _src_file_name = f'{project_name}.md'
    _src_file_path = build_path(_src_dir, _src_file_name)
    touch(_src_file_path)


def build_html(in_path: str, out_path: str) -> subprocess.CompletedProcess:
    _build = subprocess.run(['reveal-md', in_path, '--static', out_path])
    return _build


parser = argparse.ArgumentParser()
parser.add_argument(
    '-m',
    '--mode',
    choices=['create', 'build'],
    help=(
        'When mode=create, must specify project-name and, optionally, parent-folder. '
        'When mode=build, must specify input-path and output-path.'
    ),
)
parser.add_argument('-n', '--project-name', help='Name for the new project. Used when mode=create.')
parser.add_argument(
    '-p',
    '--parent-folder',
    default='.',
    help='Directory under which the new project will be created. Used when mode=create.',
)
parser.add_argument(
    '-i',
    '--input-path',
    help='Path to input file(s). Can be a file or a directory. Used when mode=build.',
)
parser.add_argument(
    '-o',
    '--output-path',
    help='Directory where static presentation will be created. Used when mode=build.',
)
parser.add_argument('remainder', nargs='?')

if __name__ == '__main__':
    args = parser.parse_args(sys.argv)

    if args.mode == 'create':
        if args.project_name is None or args.parent_folder is None:
            parser.error('When mode=create, must specify --project-name and --parent-folder.')
        create_project(project_name=args.project_name, parent_dir=args.parent_folder)
    elif args.mode == 'build':
        if args.input_path is None or args.output_path is None:
            parser.error('When mode=build, must specify --input-path and --output-path.')
        build_html(in_path=args.input_path, out_path=args.output_path)
    else:
        parser.print_usage()
        parser.exit()
