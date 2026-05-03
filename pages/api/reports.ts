import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  // Desactivar caché
  res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate')
  res.setHeader('Pragma', 'no-cache')
  res.setHeader('Expires', '0')

  res.status(200).json({
    total_employees: 30,
    total_hours: 120.5,
    overtime_hours: 12.0,
    alerts: 5
  })
}
