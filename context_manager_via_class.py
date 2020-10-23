class File(object):

    # Constructor metodumuzu yazalim
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        # Islemleri yapildigi metod
        self.f_obj = open(self.file_name, self.mode)
        return self.f_obj

    def __exit__(self, exc_type, exc_val, traceback):
        # Dosya kapama islemi
        self.f_obj.close()


with File('deneme.txt', 'w') as f_write:
    f_write.write('Deneme...')
    print(f"Dosya Kapatildi mi?[With Body] -> {f_write.closed}")

print(f"Dosya Kapatildi mi?[With blogu disi] -> {f_write.closed}")
