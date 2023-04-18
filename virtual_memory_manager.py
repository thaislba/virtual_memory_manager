#    Virtual Memory Management
#    This project simulates the management of the virtual memory. For simplification it's being used text files to represent both the logical memory and the physical memory.
#    Author: Thais Andrade

import pandas as pd


def convert_logical_to_physical(logical_page):
    #This function receives a logical_page_number and returns the corresponding physical_page_number
    
    print(logical_page)

    # read text file into pandas DataFrame
    df = pd.read_csv("page_tables.csv", sep=",", converters={'pagina_logica': str, 'pagina_fisica': str})
    #given a logical_page get the physical_page
    physical_page = df.loc[df['pagina_logica'] == logical_page, 'pagina_fisica'].item()
    
    return str(physical_page)


def get_address_from_ram(physical_page, page_offset):
    #This function receives the physical_page_number and the page_offset and returns the physical_memory_address

    return physical_page + page_offset


def check_if_page_is_available(page):
    #checks if corresponding logical_page is available in physical_memory

    with open(r'physical_memory.txt', 'r') as file:
        content = file.read()
        if content.startswith(page): 
            print('Page exists')
            return True
        else:
            print('Page does not exist')
            return False


def main():

    #virtual address to be converted
    virtual_address  = "0000000000001111"

    #divides the virtual_address in two components and convert logical_page to physical_page
    logical_page     = virtual_address[0:8]
    page_offset      = virtual_address[8:16]
    physical_page = convert_logical_to_physical(logical_page)

    #checks if physical_page is available in ram and if so converts it to a physical address
    if check_if_page_is_available(physical_page) == True:
        physical_page = convert_logical_to_physical(logical_page)
        physical_address = get_address_from_ram(physical_page, page_offset)
        print("The physical_address of the virtual_address=",virtual_address, " is ", physical_address)
    else:
        print("Processo é inserido em fila de espera. Uma página física livre deve ser alocada.Carrega da memória secundária para a ram e busca novamente a physical_page")


if __name__ == "__main__":
    main()

