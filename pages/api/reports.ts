import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.status(200).json({
    total_employees: 3,
    total_hours: 120.5,
    overtime_hours: 12.0,
    alerts: 5
  })
}
