# Delart Remastered — Projeto de PSI

## Nome do Projeto
**Delart Estética Automotiva**

## Tema Escolhido
Sistema de lavagem de carros e motos.

## Integrantes do Grupo e Responsabilidades Principais
- **Christian Kallil Dantas Farah**: Templates
- **Davi Lucas Sousa e Medeiros Silva**: Rotas
- **Moisés Lopes Nóbrega**: Models e banco de dados

## Descrição do Sistema
O **Delart Remastered** é o funcionamento de uma estética automotiva (lava-jato), permitindo o cadastro e a listagem de clientes, o cadastro e a listagem de funcionários e o agendamento de lavagens de veículos (carros e motos) vinculando o cliente solicitante, o funcionário responsável, o veículo, o tipo de lavagem e a data/horário do serviço.

## Entidades do Sistema
1. **Cliente (`clientes`)**: Representa o proprietário do veículo que solicita o serviço. Possui `id`, `nome`, `email` (único) e `senha`.
2. **Funcionário (`funcionarios`)**: Representa o colaborador responsável por realizar as lavagens. Possui `id`, `nome`, `email` (único) e `senha`.
3. **Lavagem (`lavagens`)**: Representa o agendamento/registro de um serviço de lavagem. Possui `id`, `tipo`, `nome_veiculo`, `data`, além das referências ao cliente e ao funcionário.

## Explicação do Relacionamento 1:N
- **Cliente → Lavagem (1:N)**: Um cliente pode agendar várias lavagens ao longo do tempo, mas cada lavagem agendada está vinculada a um único cliente (`cliente_id` na tabela `lavagens` referenciando `clientes.id`).

## Explicação do Relacionamento N:N
- **Funcionário ↔ Lavagem (N:N)**: Funcionários podem trabalhar em várias lavagens registradas no sistema e os serviços de lavagem podem envolver múltiplos atendimentos de funcionários da estética automotiva.

## Instruções para Instalar Dependências

1. Clone o repositório e acesse a pasta do projeto:
   ```bash
   git clone https://github.com/MoisesLN/Delart-Remastered.git
   cd delart-remastered
   ```

2. Crie e ative um ambiente virtual (`venv`):
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Instale as dependências listadas no `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Instruções para Criar ou Popular o Banco
O banco de dados SQLite (`database.db`) é criado automaticamente na inicialização da aplicação em app.py por meio da função `inicializar_banco()`

Para popular o banco:
1. Acesse `/clientes/novo` e cadastre um ou mais clientes.
2. Acesse `/funcionarios/novo` e cadastre um ou mais funcionários.
3. Acesse `/lavagens/nova` e agende uma lavagem selecionando o cliente, o funcionário, o veículo, o tipo e a data/horário.

## Instruções para Executar o Sistema

Com o ambiente virtual ativado, execute o arquivo principal:
```bash
python app.py
```

Em seguida, abra o navegador e acesse:
```text
http://127.0.0.1:5000
```

## Principais Dificuldades Encontradas
- Configuração dos relacionamentos e `back_populates` entre os modelos no SQLAlchemy 2.0, evitando erros de carregamento (`DetachedInstanceError`) ao fechar a sessão antes de renderizar os templates.
- Tratamento e conversão dos valores de data e horário enviados pelo input HTML `datetime-local` para objetos `datetime` do Python aceitos pelo SQLAlchemy.
- Tratamento de exceções de integridade (`IntegrityError`) para impedir o cadastro de clientes ou funcionários com e-mails duplicados.
- Coordenação do trabalho em equipe via Git/GitHub integrando templates, blueprints e modelos.

## Declaração de Autoria
Declaro que desenvolvi este projeto compreendendo o código entregue e que sou
capaz de explicar e modificar suas partes principais. <br>
Uso de IA: 
```
[ ] Não utilizei IA generativa.
[ X ] Utilizei IA generativa e descrevo abaixo onde e como foi utilizada.
Descrição do uso, se houver:
Utilizamos IA para ajeitar erros gerais da plataforma (como o do input de data)
```