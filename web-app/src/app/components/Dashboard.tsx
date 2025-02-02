'use client'

import React, {useState} from 'react'
import axios from 'axios'
import {useRouter} from 'next/navigation'

export default function Dashboard() {
    const [error, setError] = useState('');
    const router = useRouter();

    const authenticate = async() => {

            const response = await axios.post('http://localhost:5000/authenticate', {}, {withCredentials: true});

            if(response.data.isTokenValid){
                router.push('/bot');
            }
            else{
                setError(response.data.error);
                router.push('/login')
                
            }
    }

    return( 
        <div>
            <div>
                this is the dashboard
            </div>
            <button onClick={authenticate}>New Chat</button>
            <div>{error}</div>
        </div>
    );
}