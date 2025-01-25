'use client'

import React, {useState} from 'react';
import axios from 'axios';

export default function SignUp() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const createAccount = async () => {
        //check if either feild is empty
        //check if username is the same as others
        //check if valid password

        //hash passowrd
        //const bcrypt = require("bcrypt");
        //const hashedPassword = await bcrypt.hash(password, 10);

        //create account
        await axios.post('http://localhost:5000/signUp' , {user: username, password: password});

        
    };

    return(
        <div className="flex flex-col justify-center w-3/4 h-screen bg-slate-400 absolute left-1/2 -translate-x-1/2">
            <input type='text' onChange={(e)=>setUsername(e.target.value)} value={username}/>
            <input type='text' onChange={(e)=>setPassword(e.target.value)} value={password}/>
            <button onClick={createAccount}>
                Sign Up
            </button>
        </div>
    );
};
