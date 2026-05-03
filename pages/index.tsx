import React, { useEffect, useState } from 'react'
import Head from 'next/head'
import { Pie, Bar, Line } from 'react-chartjs-2'
import {
  Chart as ChartJS,
  ArcElement,
  BarElement,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend,
} from 'chart.js'

ChartJS.register(ArcElement, BarElement, CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Legend)

interface Employee {
  id: string
  nombre: string
  area: string
  turno: string
}

interface Alert {
  id: number
  type: string
  message: string
  timestamp: string
}

export default function Home() {
  const [employees, setEmployees] = useState<Employee[]>([])
  const [alerts, setAlerts] = useState<Alert[]>([])
  const [loading, setLoading] = useState(true)
  const [stats, setStats] = useState({ total_employees: 0, total_hours: 0, overtime_hours: 0, alerts: 0 })

  useEffect(() => {
    fetchData()
  }, [])

  const fetchData = async () => {
    try {
      const [empRes, alertRes, reportRes] = await Promise.all([
        fetch('/api/employees').then(r => r.json()),
        fetch('/api/alerts').then(r => r.json()),
        fetch('/api/reports').then(r => r.json()),
      ])
      setEmployees(empRes)
      setAlerts(alertRes)
      setStats(reportRes)
    } catch (error) {
      console.error('Error fetching data:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleCheckIn = async (employeeId: string) => {
    try {
      const res = await fetch(`/api/checkin?employee_id=${employeeId}`)
      const data = await res.json()
      alert(`✓ ${data.message}`)
      fetchData()
    } catch (error) {
      console.error('Error:', error)
      alert('Error en check-in')
    }
  }

  const handleCheckOut = async (employeeId: string) => {
    try {
      const res = await fetch(`/api/checkout?employee_id=${employeeId}`)
      const data = await res.json()
      alert(`✓ ${data.message}`)
      fetchData()
    } catch (error) {
      console.error('Error:', error)
      alert('Error en check-out')
    }
  }

  // Calcular estadísticas de alertas
  const alertStats = {
    CRITICAL: alerts.filter(a => a.type === 'CRITICAL').length,
    WARNING: alerts.filter(a => a.type === 'WARNING').length,
    INFO: alerts.filter(a => a.type === 'INFO').length,
  }

  // Datos para Pie Chart (Alertas)
  const pieChartData = {
    labels: ['Críticas', 'Advertencias', 'Información'],
    datasets: [
      {
        data: [alertStats.CRITICAL, alertStats.WARNING, alertStats.INFO],
        backgroundColor: [
          '#dc2626',
          '#f59e0b',
          '#3b82f6',
        ],
        borderColor: [
          '#991b1b',
          '#d97706',
          '#1e40af',
        ],
        borderWidth: 2,
      },
    ],
  }

  // Datos para Bar Chart (Empleados por Área)
  const areaStats = employees.reduce((acc, emp) => {
    acc[emp.area] = (acc[emp.area] || 0) + 1
    return acc
  }, {} as Record<string, number>)

  const barChartData = {
    labels: Object.keys(areaStats),
    datasets: [
      {
        label: 'Empleados por Área',
        data: Object.values(areaStats),
        backgroundColor: [
          '#3b82f6',
          '#10b981',
          '#f59e0b',
          '#ef4444',
          '#8b5cf6',
          '#ec4899',
        ],
        borderColor: [
          '#1e40af',
          '#065f46',
          '#d97706',
          '#991b1b',
          '#6d28d9',
          '#be185d',
        ],
        borderWidth: 2,
      },
    ],
  }

  // Datos para Line Chart (Horas por Día)
  const lineChartData = {
    labels: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
    datasets: [
      {
        label: 'Horas Trabajadas',
        data: [8.2, 8.5, 8.1, 8.8, 8.3, 4.2, 0],
        borderColor: '#3b82f6',
        backgroundColor: 'rgba(59, 130, 246, 0.1)',
        borderWidth: 3,
        tension: 0.4,
        fill: true,
        pointRadius: 5,
        pointBackgroundColor: '#3b82f6',
        pointBorderColor: '#1e40af',
        pointBorderWidth: 2,
      },
    ],
  }

  // Datos para Line Chart (Horas por Empleado)
  const employeeHours = employees.slice(0, 10).map((emp, idx) => ({
    id: emp.id,
    nombre: emp.nombre,
    horas: 8 + Math.random() * 2,
    overtime: Math.random() * 2,
  }))

  const employeeChartData = {
    labels: employeeHours.map(e => e.nombre),
    datasets: [
      {
        label: 'Horas Trabajadas',
        data: employeeHours.map(e => e.horas),
        borderColor: '#3b82f6',
        backgroundColor: 'rgba(59, 130, 246, 0.1)',
        borderWidth: 3,
        tension: 0.4,
        fill: true,
        pointRadius: 6,
        pointBackgroundColor: '#3b82f6',
        pointBorderColor: '#1e40af',
        pointBorderWidth: 2,
      },
      {
        label: 'Horas Overtime',
        data: employeeHours.map(e => e.overtime),
        borderColor: '#ef4444',
        backgroundColor: 'rgba(239, 68, 68, 0.1)',
        borderWidth: 3,
        tension: 0.4,
        fill: true,
        pointRadius: 6,
        pointBackgroundColor: '#ef4444',
        pointBorderColor: '#991b1b',
        pointBorderWidth: 2,
      },
    ],
  }

  // Datos para Turnos (Doughnut)
  const turnoStats = {
    Mañana: employees.filter(e => e.turno === 'Mañana').length,
    Tarde: employees.filter(e => e.turno === 'Tarde').length,
    Noche: employees.filter(e => e.turno === 'Noche').length,
  }

  if (loading) return (
    <div className="flex items-center justify-center h-screen bg-gray-100">
      <div className="text-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
        <p className="text-gray-600">Cargando...</p>
      </div>
    </div>
  )

  return (
    <>
      <Head>
        <title>AssistantTrack 4D</title>
        <meta name="description" content="Sistema de control laboral con Computer Vision" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>

      <main className="min-h-screen bg-gray-50">
        <header className="bg-gradient-to-r from-blue-600 to-blue-800 text-white p-6 shadow-lg">
          <div className="max-w-7xl mx-auto">
            <h1 className="text-4xl font-bold">🎯 AssistantTrack 4D</h1>
            <p className="text-blue-100 text-lg">Sistema de Control Laboral con Computer Vision</p>
          </div>
        </header>

        <section className="max-w-7xl mx-auto p-6">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
            <div className="bg-white rounded-lg shadow p-6 hover:shadow-lg transition">
              <h3 className="text-gray-600 text-sm font-medium">👥 Empleados</h3>
              <p className="text-3xl font-bold text-blue-600">{stats.total_employees}</p>
            </div>
            <div className="bg-white rounded-lg shadow p-6 hover:shadow-lg transition">
              <h3 className="text-gray-600 text-sm font-medium">⏱️ Horas Totales</h3>
              <p className="text-3xl font-bold text-green-600">{stats.total_hours.toFixed(1)}h</p>
            </div>
            <div className="bg-white rounded-lg shadow p-6 hover:shadow-lg transition">
              <h3 className="text-gray-600 text-sm font-medium">⚡ Horas Extra</h3>
              <p className="text-3xl font-bold text-orange-600">{stats.overtime_hours.toFixed(1)}h</p>
            </div>
            <div className="bg-white rounded-lg shadow p-6 hover:shadow-lg transition">
              <h3 className="text-gray-600 text-sm font-medium">🚨 Alertas</h3>
              <p className="text-3xl font-bold text-red-600">{alerts.length}</p>
            </div>
          </div>

          {/* GRÁFICOS */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
            {/* Pie Chart - Alertas */}
            <div className="bg-white rounded-lg shadow p-6">
              <div className="border-b border-gray-200 pb-4 mb-4">
                <h2 className="text-xl font-bold text-gray-800">📊 Distribución de Alertas</h2>
              </div>
              <div className="flex justify-center">
                <div style={{ width: '100%', height: '300px' }}>
                  <Pie
                    data={pieChartData}
                    options={{
                      responsive: true,
                      maintainAspectRatio: false,
                      plugins: {
                        legend: {
                          position: 'bottom',
                          labels: { padding: 15, font: { size: 12 } },
                        },
                      },
                    }}
                  />
                </div>
              </div>
            </div>

            {/* Bar Chart - Empleados por Área */}
            <div className="bg-white rounded-lg shadow p-6">
              <div className="border-b border-gray-200 pb-4 mb-4">
                <h2 className="text-xl font-bold text-gray-800">📊 Empleados por Área</h2>
              </div>
              <div style={{ width: '100%', height: '300px' }}>
                <Bar
                  data={barChartData}
                  options={{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                      legend: {
                        labels: { font: { size: 12 } },
                      },
                    },
                    scales: {
                      y: {
                        beginAtZero: true,
                        ticks: { stepSize: 1 },
                      },
                    },
                  }}
                />
              </div>
            </div>
          </div>

          {/* Line Chart - Horas por Día */}
          <div className="bg-white rounded-lg shadow p-6 mb-8">
            <div className="border-b border-gray-200 pb-4 mb-4">
              <h2 className="text-xl font-bold text-gray-800">📈 Horas Trabajadas por Día</h2>
            </div>
            <div style={{ width: '100%', height: '350px' }}>
              <Line
                data={lineChartData}
                options={{
                  responsive: true,
                  maintainAspectRatio: false,
                  plugins: {
                    legend: {
                      labels: { font: { size: 12 } },
                    },
                  },
                  scales: {
                    y: {
                      beginAtZero: true,
                      ticks: { stepSize: 2 },
                    },
                  },
                }}
              />
            </div>
          </div>

          {/* Line Chart - Horas por Empleado (Comparativo) */}
          <div className="bg-white rounded-lg shadow p-6 mb-8">
            <div className="border-b border-gray-200 pb-4 mb-4">
              <h2 className="text-xl font-bold text-gray-800">📊 Horas Trabajadas vs Overtime por Empleado (Top 10)</h2>
            </div>
            <div style={{ width: '100%', height: '400px' }}>
              <Line
                data={employeeChartData}
                options={{
                  responsive: true,
                  maintainAspectRatio: false,
                  plugins: {
                    legend: {
                      labels: { font: { size: 12 } },
                    },
                  },
                  scales: {
                    y: {
                      beginAtZero: true,
                      ticks: { stepSize: 1 },
                      title: {
                        display: true,
                        text: 'Horas',
                      },
                    },
                  },
                }}
              />
            </div>
          </div>

          {/* Resumen de Alertas */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <div className="bg-red-50 rounded-lg shadow p-6 border-l-4 border-red-500">
              <p className="text-gray-600 text-sm font-medium">🔴 Alertas Críticas</p>
              <p className="text-3xl font-bold text-red-600 mt-2">{alertStats.CRITICAL}</p>
            </div>
            <div className="bg-yellow-50 rounded-lg shadow p-6 border-l-4 border-yellow-500">
              <p className="text-gray-600 text-sm font-medium">🟡 Advertencias</p>
              <p className="text-3xl font-bold text-yellow-600 mt-2">{alertStats.WARNING}</p>
            </div>
            <div className="bg-blue-50 rounded-lg shadow p-6 border-l-4 border-blue-500">
              <p className="text-gray-600 text-sm font-medium">🔵 Información</p>
              <p className="text-3xl font-bold text-blue-600 mt-2">{alertStats.INFO}</p>
            </div>
          </div>

          {/* Tabla de Empleados */}
          <div className="bg-white rounded-lg shadow mb-8 overflow-hidden">
            <div className="p-6 border-b border-gray-200 bg-gray-50">
              <h2 className="text-2xl font-bold text-gray-800">📋 Empleados</h2>
            </div>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-gray-100 border-b">
                  <tr>
                    <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">ID</th>
                    <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Nombre</th>
                    <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Área</th>
                    <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Turno</th>
                    <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Acciones</th>
                  </tr>
                </thead>
                <tbody>
                  {employees.length > 0 ? employees.map((emp) => (
                    <tr key={emp.id} className="border-b hover:bg-gray-50">
                      <td className="px-6 py-4 text-sm text-gray-700 font-mono">{emp.id}</td>
                      <td className="px-6 py-4 text-sm text-gray-900 font-medium">{emp.nombre}</td>
                      <td className="px-6 py-4 text-sm text-gray-700">{emp.area}</td>
                      <td className="px-6 py-4 text-sm text-gray-700">{emp.turno}</td>
                      <td className="px-6 py-4 text-sm space-x-2">
                        <button
                          onClick={() => handleCheckIn(emp.id)}
                          className="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded text-xs font-medium transition"
                        >
                          ✓ Check-in
                        </button>
                        <button
                          onClick={() => handleCheckOut(emp.id)}
                          className="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded text-xs font-medium transition"
                        >
                          ✗ Check-out
                        </button>
                      </td>
                    </tr>
                  )) : (
                    <tr>
                      <td colSpan={5} className="px-6 py-8 text-center text-gray-500">No hay empleados cargados</td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </div>

          {/* Alertas */}
          <div className="bg-white rounded-lg shadow overflow-hidden">
            <div className="p-6 border-b border-gray-200 bg-gray-50">
              <h2 className="text-2xl font-bold text-gray-800">🚨 Alertas del Sistema</h2>
            </div>
            <div className="p-6 space-y-4">
              {alerts.length > 0 ? alerts.map((alert) => (
                <div
                  key={alert.id}
                  className={`p-4 rounded border-l-4 ${
                    alert.type === 'CRITICAL' ? 'bg-red-50 border-red-500' :
                    alert.type === 'WARNING' ? 'bg-yellow-50 border-yellow-500' :
                    'bg-blue-50 border-blue-500'
                  }`}
                >
                  <div className="flex justify-between items-start">
                    <div>
                      <p className="font-medium text-gray-800">{alert.message}</p>
                      <p className="text-sm text-gray-600 mt-1">{new Date(alert.timestamp).toLocaleString('es-ES')}</p>
                    </div>
                    <span className={`text-xs font-bold px-3 py-1 rounded whitespace-nowrap ${
                      alert.type === 'CRITICAL' ? 'bg-red-200 text-red-800' :
                      alert.type === 'WARNING' ? 'bg-yellow-200 text-yellow-800' :
                      'bg-blue-200 text-blue-800'
                    }`}>
                      {alert.type}
                    </span>
                  </div>
                </div>
              )) : (
                <p className="text-gray-500 text-center py-8">No hay alertas activas</p>
              )}
            </div>
          </div>
        </section>
      </main>
    </>
  )
}
