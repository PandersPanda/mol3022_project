import React, { useEffect, useState } from 'react'
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import axios from 'axios';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';

import CustomText from './CustomText';
import { margin } from '@mui/system';

function Input() {

  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');

  const handleInputChange = (event: { target: { value: React.SetStateAction<string>; }; }) => {
    setInput(event.target.value);
  };

  const handleSubmit = async () => {
    try {
        /* http://localhost:5000/input
            Will return a reversed string FOR TESTING ONLY */
      const response = await axios.post('http://localhost:5000/predict', { input });
      setOutput(response.data.predictions);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div style={{display: 'flex', justifyContent: 'center', flexDirection: 'column', width: '60%'}}>
    <h1 style={{color: 'white'}}>Protein Secondary Structure Prediction</h1>
    {/* MaterialUI alert box with new line for each letter */}
    <Alert severity="info" style={{ maxWidth: '600px'}}>
      <AlertTitle>Info</AlertTitle>
      
      <div style={{display: 'flex', flexDirection: 'row'}}>
        <div style={{marginRight: '20px'}}>
          <p>In the predictions</p>
          <p><strong> H </strong> represents <strong> Alpha-helix </strong></p>
          <p><strong> E </strong> represents <strong> Beta-sheet </strong></p>
          <p><strong> C </strong> represents <strong> Random coil </strong></p>
        </div>
        <div>
          <p>Max input sequence is <strong>128</strong> characters</p>
          <p>Here are some example sequences to try</p>
          <ul style={{ maxWidth: '300px', overflow: 'auto'}}>
            <li>MGDKPIWEQIGSSFINHYYQLFDNDRTQLGAIYIDASCLTWEGQQFQGKAAIVEKLSSLPFQKIQHSITAQDHQPTPDSCIISMVVGQLKADEDPIMGFHQEFLLKNINDAWVCTNDMFRLALHNFG</li>
            <li>MKEEKRSSTGFLVKQRAFLKLYMITMTEQERLYGLKLLKVLQSEFKEIGFKPNHTEVYRSLHELLDDGILKQIKVKKEGAKLQEVVLYQFKDYEAAKLYKKQLKVELDRCKKLIEKALSDNF</li>
            <li>YCQKWMWTCDEERKCCEGLVCRLWCKRIINM</li>
          </ul>
        </div>
      </div>
    </Alert>
    <Box
    component="form"
    sx={{
      '& .MuiInputBase-input': { color: 'white' },
      display: 'flex', justifyContent: 'center', width: '80%', paddingTop: '10%',
    }}
    noValidate
    autoComplete="off"
  >
    <TextField 
      sx={{ width: '100%', minWidth: '220px', maxWidth: '700px'}}
      label="Input amino acid sequence" 
      color="secondary" 
      multiline
      value={input}
      onChange={handleInputChange}
      focused />

    {/* MaterialUI submit button */}
    <Button sx={{ marginLeft: '5%', minWidth: '80px', maxHeight: '60px'}} variant="contained" onClick={handleSubmit} color="secondary">Predict</Button>
  </Box>

  <Card sx={{ width: '100%', minWidth: '300px', marginTop: '5%', backgroundColor: '#555555', display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
    <CardContent>
      <Typography sx={{ fontSize: 18, color: 'white'}} color="text.secondary" gutterBottom>
        HEC-Prediction
      </Typography>
      <Typography component="div">
        <Box sx={{ fontSize: 16, fontWeight: 'bold' }}>
          <CustomText t={output} />
        </Box>
      </Typography>
    </CardContent>
  </Card>


  </div>
  )
}

export default Input