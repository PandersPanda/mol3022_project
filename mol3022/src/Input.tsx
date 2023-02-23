import React, { useEffect, useState } from 'react'
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import axios from 'axios';

function Input() {

  const [getMessage, setGetMessage] = useState('')

  useEffect(()=>{
    axios.get('http://localhost:5000/flask/hello').then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response.data.message)
    }).catch(error => {
      console.log(error)
    })

  }, [])

  return (
    <div>
    <Box
    component="form"
    sx={{
      '& > :not(style)': { m: 1, width: '25ch' },
    }}
    noValidate
    autoComplete="off"
  >
    <TextField 
      label="Input for AI model" 
      color="secondary" 
      focused />
  </Box>

    {/* div that retrieves the message from getMessage */} 
    <div>{getMessage}</div>


  
  

  </div>
  )
}

export default Input