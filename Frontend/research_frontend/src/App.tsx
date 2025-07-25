import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import NotFound from './pages/NotFound'
import ProtectedRoutes from "./components/ProtectedRoutes"
import react from 'react'
import Register from './pages/Register'

function Logout (){
  localStorage.clear()
  return <Navigate to='/login'/>
}

function RegisterAndLogout (){
  localStorage.clear()
  return <Register />
}

function App() {
  
  return (
    <BrowserRouter >
      <Routes>
        <Route
          path='/'
          element={
          <ProtectedRoutes>
            <Home/>
          </ProtectedRoutes>
          }
        />

        <Route path='/login' element={<Login/>}/>
        <Route path='/logout' element={<Logout/>}/>
        <Route path='/register' element={<RegisterAndLogout/>}/>
        <Route path='*' element={<NotFound/>}/>
      </Routes>
       
    </BrowserRouter>
  )
}

export default App

