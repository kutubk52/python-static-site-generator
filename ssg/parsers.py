import shutil
from typing import List
from pathlib import Path

class Parser:
    @List[str]
    extensions = []

    def valid_extension(self, extension):
        return if extension in self.extensions
    
    def parser(path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(path):
        with open(path) as file:
            return file.read()

    def write(path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path) as file:
            write(file)

    def copy(path, source, dest):
        shutil.copy2(path, dest/Path(source))
    
class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(path: Path, source: Path, dest: Path):
        Parser.copy(path, source, dest)

        

