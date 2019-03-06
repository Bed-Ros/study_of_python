import os


def create_files_list(direction):
    files_list = []
    for n in os.walk(direction):
        if n[2]:
            for t in n[2]:
                files_list.append(os.path.normpath(n[0] + '/' + t))
    return files_list


def check_file_twins(dirs_list):
    twins_list = []
    for ffd in range(len(dirs_list)):
        try:
            first_file = open(dirs_list[ffd], 'rb').read()
        except:
            print('Не смог обработать файл ' + dirs_list[ffd])
        else:
            for sfd in range(ffd + 1, len(dirs_list)):
                if dirs_list[ffd] != dirs_list[sfd]:
                    try:
                        second_file = open(dirs_list[sfd], 'rb').read()
                    except:
                        print('Не смог обработать файл ' + dirs_list[sfd])
                    else:
                        if first_file == second_file:
                            twins_list.append([dirs_list[ffd], dirs_list[sfd]])
    return twins_list


def main():
    initial_dir = r'C:/'
    print('Создается список всех файлов папки ' + initial_dir)
    files_list = create_files_list(initial_dir)
    print('Идет поиск близнецов')
    twins = check_file_twins(files_list)
    print('Файлы - близнецы:')
    for pair in twins:
        print(pair[0] + ' = ' + pair[1])


if __name__ == '__main__':
    main()
