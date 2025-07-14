import {Navigate} from 'react-router-dom'
import { jwtDecode } from 'jwt-decode'
import api from '../api'
import { REFRESH_TOKEN, ACCESS_TOKEN } from '../constants'
import { useEffect, useState } from 'react'


function ProtectedRoutes({children}:any){
    const [isAuthorised, setIsAuthorised] : any = useState(null);

    useEffect(()=> {
            auth().catch(() => setIsAuthorised(false))
        }, [])


    const refreshToken = async() => {
        const refreshToken = localStorage.getItem(REFRESH_TOKEN)


        try{
            const response = await api.post('/api/token/refresh/', {
                refresh: refreshToken,
            });
 
            if (response.status === 200){
                localStorage.setItem(ACCESS_TOKEN, response.data.access)
                setIsAuthorised(true)
            }
            else{
                setIsAuthorised(false);
            }
        }
        catch (error){
            console.log(error)
            setIsAuthorised(false)
        }

    }

    const auth = async() => {
        const token = localStorage.getItem(ACCESS_TOKEN)
        
        if (!token){
            setIsAuthorised(false)
            return
        }
        const decoded = jwtDecode(token)
        const tokenexp : any = decoded.exp
        const today = Date.now() / 100

        if (tokenexp < today){
            await refreshToken()
        }
        else{
            setIsAuthorised(true)
        }
    }

    if (isAuthorised === null){
        return <div>Loading ......</div>
    }
    return isAuthorised ? children : <Navigate to="/login"/>
}

export default ProtectedRoutes