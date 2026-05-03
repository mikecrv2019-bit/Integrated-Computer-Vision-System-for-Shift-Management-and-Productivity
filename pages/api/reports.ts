import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  // Desactivar caché
  res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate')
  res.setHeader('Pragma', 'no-cache')
  res.setHeader('Expires', '0')

  // Simulación de datos dinámicos basados en 21 empleados
  const totalEmployees = 21
  const averageHoursPerEmployee = 8.5  // Promedio de horas trabajadas por empleado
  const totalHours = Number((totalEmployees * averageHoursPerEmployee).toFixed(1))
  const overtimePercentage = 0.10  // 10% de horas son extras
  const overtimeHours = Number((totalHours * overtimePercentage).toFixed(1))

  res.status(200).json({
    total_employees: totalEmployees,
    total_hours: totalHours,
    overtime_hours: overtimeHours,
    alerts: 8  // Actualizado a 8 alertas (conforme a las alertas en alerts.ts)
  })
}
