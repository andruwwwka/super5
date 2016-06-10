from redactor.handlers import SimpleUploader


class CustomHandler(SimpleUploader):

    def save_file(self):
        if not hasattr(self, 'real_path'):
            self.real_path = '/' + self.file_storage.save(
                self.get_full_path()[1:],
                self.get_file()
            )
        return self.real_path
