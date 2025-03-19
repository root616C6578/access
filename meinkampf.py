import subprocess


def change_owner():
    subprocess.run("takeown /f C:\Windows\System32\cmd.exe", shell=True)
    subprocess.run("takeown /f C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", shell=True)
    subprocess.run("takeown /f C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe", shell=True)
    subprocess.run("icacls C:\Windows\System32\cmd.exe /grant Administrator:F", shell=True)
    subprocess.run("icacls C:\Windows\System32\WindowsPowerShell\v1.0\\powershell.exe /grant Administrator:F", shell=True)
    subprocess.run("icacls C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe /grant Administrator:F", shell=True)
    subprocess.run("icacls C:\Windows\system32\WindowsPowerShell\v1.0\powershell_ise.exe /grant Administrator:F", shell=True)
def block_access(user):
    cmd_block = f'icacls C:\Windows\System32\cmd.exe /deny {user}:(RX)'
    ps_block = f'icacls C:\Windows\System32\WindowsPowerShell\v1.0\\powershell.exe /deny {user}:(RX)'
    ps_block2 = f'icacls C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe /deny {user}:(RX)'
    ps_block3 = f'icacls C:\Windows\system32\WindowsPowerShell\v1.0\powershell_ise.exe /deny {user}:(RX)'
    subprocess.run(cmd_block, shell=True)
    subprocess.run(ps_block, shell=True)
    subprocess.run(ps_block2, shell=True)
    subprocess.run(ps_block3, shell=True)
    print(f"Доступ до cmd.exe та powershell.exe заблоковано для {user}")

if __name__ == "__main__":
    users = ['user1', 'user2', 'user3', 'user4','user5', 'user6', 'user7', 'user8', 'user9', 'user10']
    change_owner()
    for user in users:    
        print(f"Блокую {user}...")
        block_access(user)
    print("Готово!")
    
size = input("Введіть розмір грудей: ")
b = ' ' * int(size)
boobs = f'({b}.{b}Y{b}.{b})'
print(boobs)