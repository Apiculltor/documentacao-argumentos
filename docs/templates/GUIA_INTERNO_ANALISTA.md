# Guia Interno do Analista: Processamento do Kit de Onboarding

**Objetivo:** Padronizar o recebimento, verificação e catalogação dos dados enviados pelo cliente.
**Responsável:** Analista de Sucesso do Cliente / SDR Técnico.

---

## 1. Protocolo de Envio (Como apresentar o Kit)

Ao enviar o kit para o cliente (Distribuidor), use o seguinte script base para garantir que ele entenda o valor do trabalho.

**Assunto:** Início do Projeto - Kit de Engenharia de Argumentos

> "Olá, [Nome do Cliente].
>
> Para criarmos os argumentos de venda blindados que prometemos, precisamos alimentar nossa inteligência com dados técnicos da sua operação.
>
> Preparamos um **Kit de Onboarding** com 3 formulários simples. Eles são o mapa que nos guiará na criação dos materiais.
>
> **Por favor, siga a ordem sugerida no arquivo `KIT_ONBOARDING_README.md`.**
>
> *Dica:* Peça para o seu Responsável Técnico preencher o Formulário 2. É o mais importante."

---

## 2. Checklist de Verificação (Quality Assurance)

Ao receber os arquivos de volta, **NÃO** inicie a pesquisa antes de validar os itens abaixo. Se houver erro, devolva para o cliente.

### 2.1. Validação do Formulário 1 (Empresa)
- [ ] **CNPJ:** Consulte no site da Receita Federal. O CNAE principal bate com o informado? A situação cadastral está "Ativa"?
- [ ] **Regime Tributário:** Se ele marcou "Lucro Real", peça uma comprovação simples (ex: cabeçalho de um balancete) se tiver dúvida. Isso muda todo o cálculo de ROI.

### 2.2. Validação do Formulário 2 (Produtos)
- [ ] **FISPQ:**
    - [ ] Está datada?
    - [ ] A data é posterior a 2015 (Norma GHS)?
    - [ ] O nome do produto no arquivo é IDÊNTICO ao da tabela?
- [ ] **Notificação ANVISA:**
    - [ ] O número informado existe no site da ANVISA? (Consulte em: `consultas.anvisa.gov.br`)
    - [ ] O vencimento do registro está válido?

### 2.3. Validação do Formulário 3 (Compliance)
- [ ] **AFE:** Se ele disse que tem, ele mandou o número? Consulte na ANVISA.
- [ ] **Licença Ambiental:** Verifique a data de validade.

### 2.4. Validação do Formulário 4 (Comercial)
- [ ] **Matriz de Objeções:** O cliente preencheu pelo menos as 3 principais? (Se estiver em branco, o agente não saberá argumentar).
- [ ] **Política de Desconto:** Está claro até onde o agente pode negociar? (Evita prejuízo).
- [ ] **Scripts:** Eles enviaram exemplos reais ou apenas genéricos? (Peça gravações se possível).

---

## 3. Protocolo de Catalogação (Taxonomia)

Organize os arquivos recebidos na nossa nuvem seguindo estritamente este padrão. Isso facilita a automação futura.

**Estrutura de Pastas:**
`/CLIENTES/[NOME_CLIENTE]/01_INPUTS_CLIENTE/`

**Padrão de Nomenclatura de Arquivos:**

*   **FISPQs:** `FISPQ_[NOME_PRODUTO]_[ANO].pdf`
    *   *Ex: FISPQ_Clorogel_2024.pdf*
*   **Fichas Técnicas:** `FT_[NOME_PRODUTO]_[ANO].pdf`
*   **Laudos:** `LAUDO_[TIPO]_[NOME_PRODUTO].pdf`
    *   *Ex: LAUDO_VIRUCIDA_Clorogel.pdf*
*   **Formulários Preenchidos:** `FORM_[NUMERO]_[NOME_CLIENTE].md` (ou .docx)

---

## 4. Tratamento de Erros (Scripts de Devolutiva)

Se o cliente enviar algo errado, use estes textos para pedir correção sem ser rude.

### Caso 1: FISPQ Desatualizada
> "Recebemos o material. Notei que a FISPQ do produto [Nome] é de [Ano]. Para garantir a segurança jurídica dos argumentos, precisamos de uma versão atualizada (pós-2015, padrão GHS). Conseguem solicitar ao fabricante?"

### Caso 2: Falta de Notificação ANVISA
> "Não localizei o número de notificação ANVISA do produto [Nome]. Sem isso, não podemos criar argumentos para hospitais ou licitações, pois o produto seria considerado irregular. Poderiam verificar?"

### Caso 3: Arquivos Desorganizados (Tudo solto no e-mail)
> "Para garantir que nenhum documento se perca, poderiam por gentileza colocar os arquivos na pasta do Drive que criamos? Isso agiliza nossa análise em 50%."
