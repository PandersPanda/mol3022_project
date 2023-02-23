import React from 'react'
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';

function Input() {
  return (
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
  )
}

export default Input