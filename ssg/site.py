import Path from pathlib

class Site:

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build():
        self.dest.mkdir(parents=True, exist_ok=True)

        for path in self.source.rglob("*"):
            if (path.isdirectory()):
                create_dir(path)
