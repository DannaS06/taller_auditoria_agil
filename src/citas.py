from datetime import datetime


class CitaMedica:
    def __init__(self, paciente_id: str, doctor_id: str, fecha_hora: datetime):
        self.paciente_id = paciente_id
        self.doctor_id = doctor_id
        self.fecha_hora = fecha_hora


def validar_y_agendar_cita(
    paciente_id: str, doctor_id: str, fecha_hora: datetime, citas_existentes: list[CitaMedica]
) -> CitaMedica:
    """Valida reglas de negocio y agenda una cita médica."""
    if not paciente_id or not doctor_id:
        raise ValueError("El identificador del paciente y del doctor son obligatorios.")

    if fecha_hora < datetime.now():
        raise ValueError("No se pueden agendar citas en fechas pasadas.")

    for cita in citas_existentes:
        if cita.doctor_id == doctor_id and cita.fecha_hora == fecha_hora:
            raise ValueError("El doctor ya tiene una cita asignada en ese horario.")

    return CitaMedica(paciente_id=paciente_id, doctor_id=doctor_id, fecha_hora=fecha_hora)
