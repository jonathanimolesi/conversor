# Conversor wav/nmf

Programa pessoal para manipular/converter arquivos de áudios da Ura. Fazer consulta no Sql dos caminhos das id's
de ligações.

Arquivo Wav que não roda em qualquer software, para mp3. Arquivos nmf com conversão tanto para wav quanto para mp3.
Prioridade é a conversão e espaço em disco, e não a mais alta qualidade de som do áudio.

A parte do código NMF converter é de autoria do Dmitry Misharov
https://github.com/quarckster/nmf_to_wav

A consulta é feita através de escolha por mês e ano que necessito, utilizando uma planilha externa via pandas.
 Aba Converter
    Selecione método:
        Arquivo Único -> Converter apenas um arquivo
        Pasta -> Converte todos os áudios dentro dessa pasta
        Multiplas pastas -> Converte todos os áudios, dentro de todas as subpastas de uma pasta raiz
    Formato original:
        Radio button com opções de WAV ou NMF. Formato original do áudio que deseja converter
    Formato final:
        Radio button com opções de WAV ou MP3. Formato FINAL do áudio (output)
    Caminho:
        Caminho completo da pasta no seu computador. Ex: C:/User/local/audios
    Botão Go:
        Botão para iniciar a operação.
    
    Resultado:
        LCD DISPLAY que vai atualizando em números conforme os áudios são convertidos.
    
    Manipulação de arquivos
    Arquivos:
      Radio button com opções de mp3, wav ou nmf para manipulação: copiar, mover ou deletar
    Copiar ou Mover:
      Radio Button com as opções de Copiar ou Mover
    Remover Copiados:
      Radio button com opção para deletar os arquivos do local original que foram copiados
    
    Origem e Destino
      Local onde se informa a origem e destino no seu computador dos áudios para serem manipulados
    
    Remover arquivos:
      Radio button com opção de mp3, wav, nmf exclusiva para remover os áudios com o formato selecionado.
      Caminho dos arquivos:
      Local no seu computador onde se encontra os arquivos para serem deletados.
    
 Aba Consulta
      Mês e Ano para consulta
        Dropdown com opção de mês 1 até 12
        Dropdown com opção de ano 2018, 2019 e 2020
      
      ID's
        PlainText para ser inseridos o(s) id's que deseja consultar no banco.
      
      Dropdown de seleção do Banco
      Botão Consultar para iniciar a operação
    
    Contém também um textBrownser para exibir o resultado da consulta realizada.
 
      
   


| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | **Conversor para URA de áudios nmf/wav para mp3 ou wav. Consulta sql dos id's das ligações**
| :label: Tecnologias | python

<!-- Inserir imagem com a #vitrinedev ao final do link -->
![](#vitrinedev)

## Detalhes do projeto

Textos e imagens que descrevam seu projeto, suas conquistas, seus desafios, próximos passos, etc...
