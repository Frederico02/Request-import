def format_strings(input_list):
    formatted_list = []
    for item in input_list:
        prefix = item[:3]  # Pega os três primeiros caracteres (DE1)
        main_part = item[3:]

        # Adicionar a string original
        formatted_list.append(item)

        # Formatar a string original
        formatted_list.append(f"{main_part}.{prefix}")

        # Trocar o 'K' por 'R' e formatar
        modified_part = main_part.replace('K', 'R', 1)
        formatted_list.append(f"{modified_part}.{prefix}")

        # Adicionar linha separadora
        formatted_list.append('--------------------------')

    return formatted_list


def save_to_txt(formatted_list, file_name='output.txt'):
    with open(file_name, 'w') as file:
        for line in formatted_list:
            file.write(line + '\n')


# Lista de strings de entrada
input_list = [
    'DE1K9A0AN6',
    'DE1K9A0AN8',
    'DE1K9A0AC2',
    'DE1K9A0AS5',
    'DE1K9A0B2B',
    'DE1K9A0B3P',
    'DE1K9A0B63',
    'DE1K9A0CKD',
    'DE1K9A0B3T',
    'DE1K9A0BQH',
    'DE1K9A0CUK',
    'DE1K9A0DFB',
    'DE1K9A08MT',
    'DE1K9A09RM',
    'DE1K9A09RP',
    'DE1K9A0AQN',
    'DE1K9A0AW1',
    'DE1K9A0AWL',
    'DE1K9A0BHF',
    'DE1K9A0BT6',
    'DE1K9A0CRL',
    'DE1K9A0BLG',
    'DE1K9A0BRY',
    'DE1K9A0B8L'
]

# Formatar as strings
formatted_list = format_strings(input_list)

# Salvar em um arquivo txt
save_to_txt(formatted_list)

print("Arquivo gerado com sucesso!")
