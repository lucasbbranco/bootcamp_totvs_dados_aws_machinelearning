# 🎮 Xbox Game Pass — Sales Dashboard 2024

Dashboard de vendas desenvolvido em Excel/Python para análise do desempenho de assinaturas do Xbox Game Pass ao longo de 2024. O projeto transforma dados brutos de assinantes em visualizações interativas, permitindo a tomada de decisões baseada em dados.

---

### Abas do arquivo Excel

| Aba | Descrição |
|-----|-----------|
| `A̳ssets` | Paleta de cores oficial da marca Xbox usada no design |
| `B̳ases` | Base de dados bruta com os 295 registros de assinantes |
| `C̳álculos` | Tabelas intermediárias com agregações que alimentam os gráficos |
| `D̳ashboard` | Painel visual interativo com KPIs, gráficos e tabelas |

---

## 📊 Dados Utilizados

### Fonte
Base de dados fictícia com **295 assinantes** do Xbox Game Pass referente ao período de **janeiro a dezembro de 2024**.

### Colunas da base (`B̳ases`)

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `Subscriber ID` | Inteiro | Identificador único do assinante |
| `Name` | Texto | Nome do assinante |
| `Plan` | Texto | Plano contratado: `Core`, `Standard` ou `Ultimate` |
| `Start Date` | Data | Data de início da assinatura |
| `Auto Renewal` | Texto | Renovação automática ativa: `Yes` / `No` |
| `Subscription Price` | Inteiro | Preço base da assinatura (R$) |
| `Subscription Type` | Texto | Periodicidade: `Monthly`, `Quarterly` ou `Annual` |
| `EA Play Season Pass` | Texto | Possui add-on EA Play: `Yes` / `No` |
| `EA Play Season Pass Price` | Inteiro | Valor do add-on EA Play (R$) |
| `Minecraft Season Pass` | Texto | Possui add-on Minecraft: `Yes` / `No` |
| `Minecraft Season Pass Price` | Inteiro | Valor do add-on Minecraft (R$) |
| `Coupon Value` | Inteiro | Valor de desconto por cupom (R$) |
| `Total Value` | Inteiro | Valor total pago pelo assinante (R$) |

### Resumo dos dados

- **Total de assinantes:** 295
- **Faturamento total 2024:** R$ 7.633
- **Período:** 01/01/2024 a 16/12/2024
- **Planos disponíveis:** Core (R$ 5), Standard (R$ 10), Ultimate (R$ 15)
- **Tipos de assinatura:** Mensal, Trimestral, Anual

---

## 📈 O que o Dashboard Apresenta

### KPIs (indicadores no topo)
- Faturamento total do ano
- Total de assinantes ativos
- Receita do plano Ultimate
- Quantidade de assinantes com renovação automática
- Receita combinada de add-ons (EA Play + Minecraft)

### Gráficos
1. **Faturamento Mensal** — barras verticais mostrando a evolução da receita mês a mês
2. **Faturamento por Plano** — pizza com a participação de Core, Standard e Ultimate
3. **Tipo de Assinatura** — barras horizontais comparando Mensal, Trimestral e Anual
4. **Renovação Automática** — pizza dos planos anuais com e sem auto renovação

### Tabelas
- **Desempenho por Plano:** assinantes, faturamento, ticket médio e % do total
- **Detalhamento de Add-ons:** receita de EA Play, Minecraft e total de descontos por cupom

---

### Passo a passo — reprodução manual no Excel

1. **Abra o arquivo** `dashboard_xbox_vendas_2024.xlsx`
2. Navegue até a aba **`B̳ases`** para visualizar os dados brutos
3. A aba **`C̳álculos`** contém as tabelas de apoio — não edite as células com fórmulas
4. O painel principal está na aba **`D̳ashboard`**

---

### Passo a passo — reprodução via Python (openpyxl)
 
Caso queira recriar o dashboard a partir do zero com Python:
 
**1. Instale as dependências**
```bash
pip install openpyxl pandas
```
 
**2. Leia a base de dados**
```python
import pandas as pd
 
df = pd.read_excel('dashboard_xbox_vendas_2024.xlsx', sheet_name='B̳ases')
df['Start Date'] = pd.to_datetime(df['Start Date'])
```
 
**3. Calcule as métricas principais**
```python
# Faturamento total
total_revenue = df['Total Value'].sum()  # R$ 7.633
 
# Por plano
by_plan = df.groupby('Plan')['Total Value'].sum()
 
# Por tipo de assinatura
by_type = df.groupby('Subscription Type')['Total Value'].sum()
 
# Mensal
monthly = df.groupby(df['Start Date'].dt.month)['Total Value'].sum()
 
# Renovação automática (somente anuais)
annual_renewal = (df[df['Subscription Type'] == 'Annual']
                  .groupby('Auto Renewal')['Total Value'].sum())
```
É possível criar o Excel completamente com Python, mas fiz a estilização manualmente.
---

## 🎨 Design

O dashboard segue a identidade visual da marca **Xbox**:

| Cor | Hex | Uso |
|-----|-----|-----|
| Verde lima | `#9BC848` | Destaque principal, barras, KPIs |
| Verde médio | `#22C55E` | Plano Ultimate, acentos |
| Verde menta | `#2AE6B1` | Menus, gráfico de tipo de assinatura |
| Verde escuro | `#107C10` | Cabeçalhos, botões de tabela |
| Fundo escuro | `#0D1117` | Background do dashboard |
| Cinza card | `#161B22` | Fundo dos cards e gráficos |

---

## 📋 Perguntas de Negócio Respondidas

1. **Qual o faturamento total de vendas considerando todas as assinaturas?** → R$ 7.633
2. **Qual o faturamento separado por plano?** → Core R$ 444 | Standard R$ 1.801 | Ultimate R$ 5.388
3. **Qual o desempenho por tipo de assinatura?** → Mensal lidera com R$ 3.571 (46,8%)
4. **Qual o faturamento anual separado por auto renovação?** → Com renovação R$ 1.537 | Sem renovação R$ 217
5. **Qual a receita gerada pelos add-ons?** → EA Play R$ 2.940 | Minecraft R$ 3.880 | Cupons -R$ 2.122

---

*Projeto desenvolvido como desafio de criação de dashboard de vendas em Excel.*