import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const alerts = [
    { id: 1, type: "WARNING", message: "Overtime detectado en E001", timestamp: new Date().toISOString() },
    { id: 2, type: "INFO", message: "E002 completó su turno", timestamp: new Date().toISOString() },
  ]
  res.status(200).json(alerts)
}
