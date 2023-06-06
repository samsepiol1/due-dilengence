# Sistema de Due-Dilengence

## Vulnerabilidade do reCAPTCHA no site https://pje.trt4.jus.br/primeirograu

Ao realizar uma análise de segurança no site https://pje.trt4.jus.br/primeirograu, foi encontrado um problema de segurança relacionado ao uso do reCAPTCHA. 

Os seguintes parâmetros foram encontrados na requisição:

- `chaveDeSiteDoCaptcha`: "6LeFj3QaAAAAAIhQt27bGh0XQks00PmVXz_kYQRN"
- `urlDoLoginNoPrimeiroGrau`: "https://pje.trt4.jus.br/primeirograu"
- `urlDoLoginNoSegundoGrau`: "https://pje.trt4.jus.br/segundograu"

Ao analisar a solicitação, foi descoberto que o reCAPTCHA estava sendo validado diretamente pela API do Google, sem a validação do domínio da página do site. Isso significa que um atacante poderia realizar uma solicitação para a API do reCAPTCHA com a chave de site e obter a verificação, ignorando assim a validação do domínio.

Essa vulnerabilidade pode permitir que um atacante mal-intencionado realize ataques de phishing ou roubo de informações dos usuários do site, já que o reCAPTCHA não estaria protegendo adequadamente o login do site.

Recomenda-se que a validação do domínio seja adicionada ao uso do reCAPTCHA no site para evitar a exploração dessa vulnerabilidade.
