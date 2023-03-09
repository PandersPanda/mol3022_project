import React, { useEffect, useState } from 'react'
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import axios from 'axios';

function Input() {

  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');

  const handleInputChange = (event: { target: { value: React.SetStateAction<string>; }; }) => {
    setInput(event.target.value);
  };

  const handleSubmit = async () => {
    try {
        /* http://localhost:5000/input
            Will return a reversed string */
      const response = await axios.post('http://localhost:5000/predict', { input });
      setOutput(response.data.predictions);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div>
    <Box
    component="form"
    sx={{
      /* input text color */
      '& .MuiInputBase-input': { color: 'white' },
    }}
    noValidate
    autoComplete="off"
  >
    <TextField 
      label="Input for AI model" 
      color="secondary" 
      value={input}
      onChange={handleInputChange}
      focused />

    {/* MaterialUI submit button */}
    <Button variant="contained" onClick={handleSubmit} color="secondary">Submit</Button>
  </Box>

    {/* div that retrieves the message from getMessage */} 
    <div>{output}</div>

  </div>
  )
}

export default Input