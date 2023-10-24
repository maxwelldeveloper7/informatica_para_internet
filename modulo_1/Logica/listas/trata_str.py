def formatar_nome(nome_completo: str) -> str:
        # Converte o nome completo para minúsculo e depois aplica o método title() para colocar a primeira letra de cada palavra em maiúscula
        nome_formatado = nome_completo.lower().title()

        # Substitui as ocorrências das preposições pela mesma palavra em minúsculo
        nome_formatado = (
            nome_formatado.replace(" De ", " de ")
            .replace(" Da ", " da ")
            .replace(" Das ", " das ")
            .replace(" Do ", " do ")
            .replace(" Dos ", " dos ")
        )

        return nome_formatado

nomes = ['MAXWELL DE OLIVEIRA CHAVES', 'ana clara athayde da silva']

for nome in nomes:
    print(formatar_nome(nome))