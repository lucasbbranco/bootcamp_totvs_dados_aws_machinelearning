# RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS

Data: 09 de abril de 2026
Empresa: Abstergo Industries
Responsável: Lucas Branco

## Introdução
Este relatório apresenta o processo de implementação de ferramentas na empresa Abstergo Industries, realizado por Lucas Branco. O objetivo do projeto foi elencar 3 serviços AWS, com a finalidade de realizar diminuição de custos imediatos.

## Descrição do Projeto
O projeto de implementação de ferramentas foi dividido em 3 etapas, cada uma com seus objetivos específicos. A seguir, serão descritas as etapas do projeto:

Etapa 1:
- **Amazon EC2 com Auto Scaling e Instâncias Reservadas**
- Foco: Otimização de custos com computação em nuvem
- A Abstergo Industries mantinha servidores on-premises superdimensionados que operavam 24/7, mesmo em horários de baixa demanda. Com a migração para Amazon EC2 utilizando Auto Scaling, a infraestrutura passa a escalar automaticamente conforme a demanda real, eliminando o desperdício de recursos ociosos. Além disso, para cargas de trabalho previsíveis e constantes, a adoção de Instâncias Reservadas (Reserved Instances) oferece descontos de até 72% em comparação com instâncias sob demanda. Isso reduz drasticamente os custos operacionais com servidores.

Etapa 2:
- **Amazon S3 com políticas de ciclo de vida (Lifecycle Policies)**
- Foco: Redução de custos com armazenamento de dados
- A empresa armazena grandes volumes de dados como relatórios, backups e logs históricos. Com o Amazon S3, é possível configurar políticas de ciclo de vida que movem automaticamente dados acessados com pouca frequência para classes de armazenamento mais baratas, como S3 Infrequent Access (IA) ou S3 Glacier. Dados raramente acessados podem ser arquivados no S3 Glacier Deep Archive, com custo até 95% menor que o armazenamento padrão. Isso elimina a necessidade de manter storage físico local e reduz significativamente os gastos com armazenamento.

Etapa 3:
- **AWS Lambda (Computação Serverless)**
- Foco: Eliminação de custos com servidores para processos pontuais
- A Abstergo Industries executa diversos processos internos que rodam de forma periódica ou sob demanda, como processamento de relatórios, integrações entre sistemas e envio de notificações. Com o AWS Lambda, esses processos passam a ser executados em um modelo serverless, onde a empresa paga apenas pelo tempo de execução efetivo (cobrado por milissegundo), sem precisar manter servidores ligados continuamente. Para processos que rodam poucas vezes ao dia ou por curtos períodos, a economia pode ultrapassar 90% em relação a uma instância EC2 dedicada.

## Conclusão
A implementação de ferramentas na empresa Abstergo Industries tem como esperado a redução significativa de custos operacionais com infraestrutura de TI, estimada entre 40% a 70% dependendo do cenário de uso. A combinação de EC2 com Auto Scaling e Instâncias Reservadas, S3 com Lifecycle Policies e Lambda serverless aumentará a eficiência e a produtividade da empresa. Recomenda-se a continuidade da utilização das ferramentas implementadas e a busca por novas tecnologias que possam melhorar ainda mais os processos da empresa.

## Anexos

- [Documentação oficial AWS EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/)
- [Guia de classes de armazenamento Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
- [Guia de boas práticas AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)

Assinatura do Responsável pelo Projeto:

Lucas Branco
