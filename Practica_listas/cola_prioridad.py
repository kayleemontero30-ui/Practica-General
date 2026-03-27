#Crear una cola de prioridad para gestionar pacientes en una sala de emergencias. Cada paciente tiene un
#nivel de urgencia asignado (1 para casos críticos, 5 para casos leves).
#Pasos:
#• Implementar una cola de prioridad que almacene pacientes con su nivel de urgencia.
#• Extraer los pacientes en el orden correcto de atención.4

import heapq

cola_prioridad =[]

heapq.heappush(cola_prioridad, (3, "Nina de 10 anos con alergia severa"))
heapq.heappush(cola_prioridad, (4, "Nino de 5 anos con fiebre alta"))
heapq.heappush(cola_prioridad, (1, "Hombre de 35 anos con todas las fracturas del mundo, tras un accidente de trafico"))
heapq.heappush(cola_prioridad, (5, "Mujer de 90 anos que le quedan 10 minutos de vida"))
heapq.heappush(cola_prioridad, (2, "Mujer de 25 anos con una fractura expuesta en la pierna, tras un accidente de trafico"))

cola_prioridad_critica = []
cola_prioridad_moderada = []
cola_prioridad_leve = []

print("Lista de pacientes en orden de atención:")

while cola_prioridad:
    prioridad, paciente = heapq.heappop(cola_prioridad)
    if prioridad <= 2:
        cola_prioridad_critica.append((prioridad, paciente))
    elif prioridad == 3:
        cola_prioridad_moderada.append((prioridad, paciente))
    else:
        cola_prioridad_leve.append((prioridad, paciente))


print("\nPacientes en estado crítico:")
for prioridad, paciente in cola_prioridad_critica:
    print(f"Nivel de Urgencia {prioridad} - {paciente}")

print("\nPacientes en estado moderado:")
for prioridad, paciente in cola_prioridad_moderada:
    print(f"Nivel de Urgencia {prioridad} - {paciente}")

print("\nPacientes que sobreviven:")
for prioridad, paciente in cola_prioridad_leve:
    print(f"Nivel de Urgencia {prioridad} - {paciente}")