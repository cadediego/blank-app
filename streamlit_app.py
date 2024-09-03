import streamlit as st
import pandas as pd
import datetime

# Configuração básica do aplicativo
st.title('Aplicativo de Agendamento')

# Entrada de dados para o agendamento
st.header('Agende um compromisso')

# Coletando informações do usuário
name = st.text_input('Seu Nome:')
date = st.date_input('Data do Compromisso:', datetime.date.today())
time = st.time_input('Hora do Compromisso:', datetime.time(9, 0))
service = st.selectbox('Tipo de Serviço:', ['Corte de Cabelo', 'Manicure', 'Massagem', 'Outros'])

if st.button('Agendar'):
    # Salvando as informações de agendamento
    new_appointment = {'Nome': name, 'Data': date, 'Hora': time, 'Serviço': service}
    st.write(f"Agendamento realizado para {name} no dia {date} às {time} para {service}.")
    # Aqui você pode adicionar código para salvar no banco de dados ou enviar uma confirmação por WhatsApp

# Visualizando os compromissos agendados (apenas um exemplo básico)
st.header('Compromissos Agendados')
appointments = pd.DataFrame([
    {'Nome': 'João', 'Data': '2024-09-03', 'Hora': '09:00', 'Serviço': 'Corte de Cabelo'},
    {'Nome': 'Maria', 'Data': '2024-09-03', 'Hora': '10:00', 'Serviço': 'Manicure'}
])
st.table(appointments)
