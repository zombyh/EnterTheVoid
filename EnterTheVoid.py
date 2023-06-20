#!/usr/bin/env python3
# Gerenciador criado por Marcelo Rocha | m.rocha@outlook.com.br

import os

def update_packages():
    os.system("xbps-install -Suvy")
    os.system("flatpak update")
    os.system("update-grub")
    print("Pacotes atualizados com sucesso!")

def search_package():
    search = input("Digite o nome do pacote: ")
    if search:
        output_search = os.popen(f"xbps-query -Rs {search}").read()
        if output_search:
            print(output_search)
        else:
            print("Nenhum pacote encontrado!")

def install_package():
    install = input("Digite o nome do pacote a ser instalado: ")
    if install:
        os.system(f"xbps-install -fy {install}")
        print(f"Comando executado com sucesso!")

def remove_package():
    remove = input("Digite o nome do pacote a ser removido: ")
    if remove:
        os.system(f"sudo xbps-remove -fy {remove}")
        print(f"Comando executado com sucesso!")

def clean_packages():
    os.system("xbps-remove -Ooy")
    os.system("vkpurge rm all")
    os.system("rm /var/cache/xbps/*")
    os.system("flatpak uninstall --unused")
    print("Pacotes limpos com sucesso!")

def reconfigure_packages():
    os.system("xbps-reconfigure -af")
    print("Pacotes reconfigurados com sucesso!")

def list_services(): 
    usuario = input("Digite seu nome de usuário:")
    os.system(f"ls /etc/sv/ > /home/{usuario}/servicos_disponiveis.txt")
    os.system(f"ls /var/service/ > /home/{usuario}/servicos_ativos.txt")
    print("Foram criados arquivos de log na sua pasta de usuário")

def enable_service():
    service = input("Digite o nome do serviço que deseja ativar: ")
    os.system(f"ln -s /etc/sv/{service} /var/service")
    print("Comando executado com sucesso.")

def disable_service():
    service = input("Digite o nome do serviço que deseja desativar: ")
    os.system(f"rm -rf /var/service/{service}")
    print("Comando executado com sucesso.")

def main():
    while True:
        # Exibe o menu principal
        print("Escolha uma opção:")
        print("1 - Atualizar pacotes")
        print("2 - Pesquisar pacote")
        print("3 - Instalar pacote")
        print("4 - Remover pacote")
        print("5 - Limpar pacotes")
        print("6 - Reconfigurar pacotes")
        print("7 - Listar serviços ativos e disponiveis")
        print("8 - Ativar um serviço")
        print("9 - Desativar um serviço")
        print("0 - Sair")
        choice = input("Opção: ")

        if choice == "1":
            update_packages()
        elif choice == "2":
            search_package()
        elif choice == "3":
            install_package()
        elif choice == "4":
            remove_package()
        elif choice == "5":
            clean_packages()
        elif choice == "6":
            reconfigure_packages()
        elif choice == "7":
            list_services()
        elif choice == "8":
            enable_service()
        elif choice == "9":
            disable_service()
        elif choice == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
