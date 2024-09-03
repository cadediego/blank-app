import streamlit as st
from streamlit_calendar import calendar

# Defina eventos no formato JSON, semelhante ao FullCalendar
events = [
    {"title": "Evento 1", "start": "2024-09-05T10:00:00", "end": "2024-09-05T12:00:00"},
    {"title": "Evento 2", "start": "2024-09-06T14:00:00", "end": "2024-09-06T16:00:00"},
]

st.title("Calendário de Agendamento")

# Renderize o calendário
selected = calendar(events=events, defaultView='dayGridMonth')

st.write("Evento selecionado:", selected)
