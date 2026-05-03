import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  // Desactivar caché para siempre obtener datos frescos
  res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate')
  res.setHeader('Pragma', 'no-cache')
  res.setHeader('Expires', '0')

  const employees = [
    { id: "E001", nombre: "Juan García", area: "Producción", turno: "Mañana" },
    { id: "E002", nombre: "María López", area: "Almacén", turno: "Tarde" },
    { id: "E003", nombre: "Carlos Ruiz", area: "Empaque", turno: "Noche" },
    { id: "E004", nombre: "Jaime Lopez", area: "Inlet", turno: "Mañana" },
    { id: "E005", nombre: "Gabriel Varela", area: "Inlet", turno: "Mañana" },
    { id: "E006", nombre: "Freddy Rivera", area: "TAR", turno: "Mañana" },
    { id: "E007", nombre: "Alexander James", area: "Inlet", turno: "Mañana" },
    { id: "E008", nombre: "Maria Pinzon", area: "Inlet", turno: "Mañana" },
    { id: "E009", nombre: "Diana Donato", area: "Inlet", turno: "Mañana" },
    { id: "E010", nombre: "Camilo Vallejo", area: "Inlet", turno: "Mañana" },
    { id: "E011", nombre: "Sandra Soto", area: "Inlet", turno: "Mañana" },
    { id: "E013", nombre: "Gabriela Rivera", area: "Inlet", turno: "Mañana" },
    { id: "E014", nombre: "Mario Dueñas", area: "Inlet", turno: "Mañana" },
    { id: "E015", nombre: "Svetlana Sorocoba", area: "Inlet", turno: "Mañana" },
    { id: "E016", nombre: "Pedro Rivera", area: "Inlet", turno: "Mañana" },
    { id: "E017", nombre: "Alberto Tizon", area: "Inlet", turno: "Mañana" },
    { id: "E018", nombre: "Claudia Lopez", area: "Inlet", turno: "Mañana" },
    { id: "E019", nombre: "Nikolas Storboscoba", area: "Inlet", turno: "Mañana" },
    { id: "E020", nombre: "Camila Balieva", area: "Door TR", turno: "Mañana" },
    { id: "E021", nombre: "Mario Dueñas", area: "Inlet", turno: "Mañana" },  
  ]

  res.status(200).json(employees)
}
