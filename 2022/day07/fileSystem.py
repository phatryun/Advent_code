

class FileSystem:
    def __init__(self, dir_path, file_size=0, root=None):
        self.dir_path = dir_path
        self.file_size = file_size
        self.list_children = list()

    def get_dir_size(self):
        res = self.file_size
        for file in self.list_children:
            res += file.get_dir_size()

        return res

    def set_children(self, list_children):
        self.list_children = list_children

    def to_string(self, prefixe=""):
        res = f"{prefixe} - {self.dir_path} {self.file_size} \n"
        for child in self.list_children:
            res += child.to_string(prefixe=f"{prefixe} ")

        return res

    def calculate_dir_size(self):
        res = self.file_size
        for child in self.list_children:
            res += child.calculate_dir_size()

        return res
