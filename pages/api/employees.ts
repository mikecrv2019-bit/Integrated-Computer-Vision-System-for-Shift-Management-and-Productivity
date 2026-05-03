import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const employees = [
    { id: "E001", nombre: "Juan García", area: "Producción", turno: "Mañana" },
    { id: "E002", nombre: "María López", area: "Almacén", turno: "Tarde" },
    { id: "E003", nombre: "Carlos Ruiz", area: "Empaque", turno: "Noche" },
    { id: "E004", nombre: "Jaime Lopez", area: "Inlet", turno: "Mañana" },
    { id: "E005", nombre: "Gabriel Varela", area: "Inlet", turno: "Mañana" }
{ id: "E006", nombre: "Freddy Rivera", area: "TAR", turno: "Mañana" }
{ id: "E007", nombre: "Alexander James", area: "Inlet", turno: "Mañana" }
{ id: "E008", nombre: "Maria Pinzon", area: "Inlet", turno: "Mañana" }
 { id: "E009", nombre: "Diana Donato", area: "Inlet", turno: "Mañana" }   
  ]
  res.status(200).json(employees)
}
