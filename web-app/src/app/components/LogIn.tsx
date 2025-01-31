'use client'

import React, {useState, useEffect, useRef} from 'react';
import axios from 'axios';
import { useRouter } from 'next/navigation';

export default function LogIn() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isUsernameEmpty, setIsUsernameEmpty] = useState(null);
    const [isPasswordEmpty, setIsPasswordEmpty] = useState(null);
    const [usernameNotFound, setUsernameNotFound] = useState(null);
    const [passwordNotVerified, setPasswordNotVerified] = useState(null);
    const isFirstRender = useRef(true);
    const router = useRouter();
    
    

    const checkFields = () => {
        //setIsUsernameEmpty(null);
        //setIsPasswordEmpty(null);

        if(username.trim().length===0 || username.length===0){
            console.log("username is empty")
            setIsUsernameEmpty(true);
        }
        else{
            console.log("username is not empty")
            setIsUsernameEmpty(false);
        }

        if(password.trim().length===0 || password.length===0){
            console.log("passwod is empty")
            setIsPasswordEmpty(true);
        }
        else{
            console.log("password is not empty")
            setIsPasswordEmpty(false);
        }
        
        //setIsUsernameEmpty(null);
        //setIsPasswordEmpty(null);

    }

    useEffect(() => {

        console.log("usernameempty:", isUsernameEmpty);
        console.log("password empty:", isPasswordEmpty);
        console.log("isfirstrender", isFirstRender.current);

        if(!isFirstRender.current){
            const logIn = async() => {
                //if(!(isUsernameEmpty || isPasswordEmpty) && !(isUsernameEmpty==null || isPasswordEmpty==null)){
                if(!(isUsernameEmpty || isPasswordEmpty)){
                        const response = await axios.post('http://localhost:5000/logIn' , {user: username, password: password});

                        console.log("username exists:", response.data.isUsernameExisting)
                        console.log("password verified:", response.data.isPasswordVerified)

                        setUsernameNotFound(false)
                        setPasswordNotVerified(false)

                        if(!response.data.isUsernameExisting){
                            setUsernameNotFound(true);
                            console.log("username is not found")
                        }
                        else if(!response.data.isPasswordVerified){
                            setPasswordNotVerified(true);
                            console.log("password is not verified")
                        }
                        else{
                            setUsernameNotFound(false);
                            setPasswordNotVerified(false);
                            console.log("logged in");
                            router.push('/dashboard?isAccountCreated=${encodeURIComponent(isAccountCreated)}`');
                            //get jwt token
                
                        }
                }
            }
            logIn();
        }

        //setUsernameNotFound(false);
        //setPasswordNotVerified(false);
        setIsUsernameEmpty(null);
        setIsPasswordEmpty(null);

        isFirstRender.current = false;
        console.log("isfirstrender2:", isFirstRender.current);
    //},[isUsernameEmpty, isPasswordEmpty, usernameNotFound, passwordNotVerified]);
    },[isUsernameEmpty, isPasswordEmpty]);


    return(
        <div className="flex flex-col justify-center w-3/4 h-screen bg-slate-400 absolute left-1/2 -translate-x-1/2">
            <input type='text' onChange={(e)=>setUsername(e.target.value)} value={username}/>
            {isUsernameEmpty && (
                <span>
                    Username required
                </span>
            )}
            <input type='text' onChange={(e)=>setPassword(e.target.value)} value={password}/>
            {isPasswordEmpty && (
                <span>
                    Password required
                </span>
            )}
            <button onClick={checkFields}>Log In</button>
            {usernameNotFound && (
                <span>
                    Username does not exist
                </span>
            )}
            {passwordNotVerified && (
                <span>
                    Incorrect password
                </span>
            )}
        </div>
    )
}