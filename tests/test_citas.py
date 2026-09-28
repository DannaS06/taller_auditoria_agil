import pytest
from datetime import datetime, timedelta
from src.citas import CitaMedica, validar_y_agendar_cita


def test_agendar_cita_exitosamente():
    """Valida la creación correcta de una cita con parámetros válidos."""
    fecha_futura = datetime.now() + timedelta(days=2)
    cita = validar_y_agendar_cita("PAC-01", "DOC-10", fecha_futura, [])
    assert cita.paciente_id == "PAC-01"
    assert cita.doctor_id == "DOC-10"
    assert cita.fecha_hora == fecha_futura


def test_error_fecha_pasada():
    """Valida que no se permitan citas en fechas u horas pasadas."""
    fecha_pasada = datetime.now() - timedelta(days=1)
    with pytest.raises(ValueError, match="No se pueden agendar citas en fechas pasadas."):
        validar_y_agendar_cita("PAC-01", "DOC-10", fecha_pasada, [])


def test_error_conflicto_horario_doctor():
    """Valida que un doctor no tenga dos citas a la misma hora."""
    fecha_cita = datetime.now() + timedelta(days=1)
    cita_previa = CitaMedica("PAC-01", "DOC-10", fecha_cita)
    with pytest.raises(ValueError, match="El doctor ya tiene una cita asignada en ese horario."):
        validar_y_agendar_cita("PAC-02", "DOC-10", fecha_cita, [cita_previa])
