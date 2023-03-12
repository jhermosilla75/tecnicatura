import calendar

# Creamos un diccionario de eventos
eventos = {
    4: 'Reunión de equipo',
    10: 'Cumpleaños de Juan',
    20: 'Entrega de proyecto'
}

# Obtenemos el calendario del mes actual
calendario = calendar.monthcalendar(2023, 3)

# Imprimimos el calendario con los eventos marcados
print('{:^20}'.format('Marzo 2023'))
print('Lun Mar Mie Jue Vie Sab Dom')
for semana in calendario:
    fila = ''
    for dia in semana:
        if dia == 0:
            fila += '   '
        elif dia in eventos:
            fila += '{:^3}'.format(str(dia)+'*')
        else:
            fila += '{:^3}'.format(dia)
    print(fila)
