import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const employees = [
    { id: "E001", nombre: "Juan García", area: "Producción", turno: "Mañana" },
    { id: "E002", nombre: "María López", area: "Almacén", turno: "Tarde" },
    { id: "E003", nombre: "Carlos Ruiz", area: "Empaque", turno: "Noche" },
  ]
  res.status(200).json(employees)
}
