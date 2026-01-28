# Calculador de Desconto em Python

Este é um projeto prático desenvolvido para consolidar conhecimentos em manipulação de tipos numéricos e formatação de dados em Python. A ferramenta automatiza o cálculo de 5% de desconto sobre o valor de qualquer item informado pelo usuário.

## Objetivo do Projeto
O foco principal foi aplicar conceitos de aritmética aplicada e tratamento de saídas de dados, garantindo que o programa:
1. Receba um valor monetário.
2. Processe a redução percentual de forma precisa.
3. Exiba o resultado final formatado no padrão financeiro.

## Funcionalidades
*   **Entrada de Dados:** Captura do preço do produto via terminal.
*   **Cálculo Matemático:** Aplicação da fórmula de desconto ($Valor \times 0.05$).
*   **Saída Formatada:** Exibição do valor economizado e do preço final com duas casas decimais (padrão `R$ 0.00`).

## Tecnologias Utilizadas
*   **Python 3**
*   **VS Code**

## Aprendizados
Durante o desenvolvimento, reforcei os seguintes conceitos:
- **Casting de Dados:** Conversão obrigatória do input (string) para `float` para permitir operações matemáticas.
- **Operadores Aritméticos:** Uso do operador de multiplicação para cálculo percentual.
- **F-Strings:** Utilização de máscaras de formatação (`:.2f`) para exibir valores monetários corretamente, garantindo uma melhor interface para o usuário.

## Como executar
1. Certifique-se de ter o Python instalado.
2. Clone o repositório ou baixe o arquivo `.py`.
3. No terminal, execute:
   ```bash
   python desconto.py
