def shells_and_users(read_file, write_file):
    with open(read_file, 'r') as read_text:
        shells = {}
        for line in read_text.readlines():
            if not line.startswith('#'):
                shell = line.strip().split(':')[-1]
                user = line.strip().split(':')[0]
                if shell not in shells:
                    shells[shell] = [user]
                else:
                    shells[shell].append(user)

    with open(write_file,'w') as write_text:
        for shells, users in shells.items():
            write_text.write(f'{shell}: {', '.join(users)}\n')


shells_and_users('user_database_short.txt','shells_and_users.txt')