# Запустите скрипт в папке Sem7, чтобы увидеть работу вживую

from working_with_files import renaming

renaming.rename_group_files("result", ".txt", ".bin", range_of_name_to_keep=(0, 3), width_of_id=2)
