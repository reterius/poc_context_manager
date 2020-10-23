from contextlib import contextmanager


@contextmanager
def file_process(dosya_adi, mod):
    dosya = open(dosya_adi, mod)  # __init__ islemi
    yield dosya  # __enter__ islemi
    dosya.close()  # __exit__ islemi


with file_process('deneme.txt', 'w') as f_write:
    f_write.write('Test...')
    print(f"Dosya Kapatildi mi?[With Body] -> {f_write.closed}")

print(f"Dosya Kapatildi mi?[With blogu disi] -> {f_write.closed}")
