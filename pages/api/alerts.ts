import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  // Desactivar caché
  res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate')
  res.setHeader('Pragma', 'no-cache')
  res.setHeader('Expires', '0')

  const alerts = [
    { id: 1, type: "CRITICAL", message: "Overtime crítico detectado en E001", timestamp: new Date().toISOString() },
    { id: 2, type: "WARNING", message: "E002 superó 2 horas de overtime", timestamp: new Date().toISOString() },
    { id: 3, type: "INFO", message: "E003 completó su turno normalmente", timestamp: new Date().toISOString() },
    { id: 4, type: "WARNING", message: "Absentismo detectado en E005", timestamp: new Date().toISOString() },
    { id: 5, type: "CRITICAL", message: "Error en registro de check-out E007", timestamp: new Date().toISOString() },
    { id: 6, type: "INFO", message: "E008 inició su turno a las 8:00 AM", timestamp: new Date().toISOString() },
    { id: 7, type: "WARNING", message: "Retraso de 15 minutos - E010", timestamp: new Date().toISOString() },
    { id: 8, type: "INFO", message: "Sistema sincronizado correctamente", timestamp: new Date().toISOString() },
  ]
  res.status(200).json(alerts)
}
