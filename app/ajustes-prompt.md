# AJUSTES PARA SEREM FEITOS NO PROMPT @prompt-agente.md

1. Sempre solicitar o nome do lead se for o primeiro contato (essa regra deve ser absoluta, precisa funcionar SEMPRE)
2. Remover o sdr_team.py pois agora estamos usando os services e nao mais o teams, entao precisamos alterar isso no prompt
3. Na seçao “4.1 TIPO 1: LEMBRETES DE REUNIÃO” precisamos fazer com que o sistema extraia o link da reunião e envie para o lead no lembrete de reunião.
4. Em todos os Fluxos A, B, C e D, precisa inserir que… ao final de todos os fluxos de conversação com o lead, ao finalizar, propõem o agendamento de reunião com o Leonardo, caso o lead confirme que quer o agendamento de reunião, consulta o Google Calendar para verificar horários disponiveis, envia os horários disponíveis extraídos do google calendar, aguarda o lead confirmar o horário que ele quer fazer a reunião, pede o email para o lead e o email de alguém que va participar também da reunião, após isso executa novamente o google calendar para criar o evento da reunião com todos os emails dos participantes e cria o evento no calendar com google meet e depois envia as informações de agendamento para o lead. Ex genérico apenas para ilustrar: “reunião agendada para o dia 14/08 as 10h, aqui está o link para voce participar.”
5. O “6.7 ESTÁGIO 2: QUALIFICAÇÃO DETALHADA” está conflitando com o ESTÁGIO 1. Por que aqui segue um outro modelo de conversação, mas no geral o padrão de qualificação é este independente do estágio ou dos fluxos, o lead tem que passar por essa qualificação SEMPRE em qualquer tipo de situação: 
1. Contas acima de R$4.000,00
2. Reunião com o decisor
3. Não ter usina própria (A não ser no caso dele querer montar uma nova)
4. Não ter contrato de fidelidade com nenhuma outra empresa
5. Ter interesse no desconto ou na montagem da usina própria
Corrija isso no prompt.
6. “ESTÁGIO 3: APRESENTAÇÃO DA SOLUÇÃO PERSONALIZADA” este estágio ficou redundante, pois em cada FLUXO A, B, C ou D já tem tudo que o Agente precisa para seguir a conversa com o lead. Apenas os <differentials> eu acho interessante reaproveitar e inserir em outra seção do prompt da melhor forma possível.
7. Acredito também que este ESTÁGIO ficou redundante “6.9 ESTÁGIO 5: FECHAMENTO E AGENDAMENTO”, pois em todos os FLUXOS A, B, C ou D já temos tudo que precisamos para direcionar a conversa e agendar uma reunião no final.
8. “6.10 ESTÁGIO 6: PÓS-AGENDAMENTO” é redundante, o pós-agendamento é apenas para dizer ao lead que o agendamento foi confirmado, enviar dia, horário e link da reunião, apenas isso de forma humanizada como a Helen.
9. “SEÇÃO 7: BASE DE CONHECIMENTO SOLAR PRIME” esta seção também fica redundante, pois o Agente deve consultar sempre o knowledge_base EM TODAS AS interações para consultar todo o conhecimento e informações.
10. “8.4 USO NATURAL DO NOME” acredito que esta seção está redundante, já se fala isso várias vezes no prompt.
11. “10.1 🚨 REGRA CRÍTICA: RESPOSTA INSTANTÂNEA COM DADOS” acredito que esta seção está redundante, veja o que voce pode fazer, pois já tem informações dessa seção em outra parte do prompt.
12. Esta seção “10.8 🚨 TRATAMENTO DE ARQUIVOS DOCX E VÍDEOS (NOVO - CRÍTICO)” ficou redundante, já tem outra seção que fala sobre isso no prompt, mantenha uma das duas seções.