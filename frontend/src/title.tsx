import { Typography } from '@mui/material';
import { useEffect } from 'react';

function Title() {
    useEffect(() => {
        document.title = 'Protein Secondary Structure Prediction';
    }, []);

    return (
        <Typography variant="h4">
            Protein Secondary Structure Prediction
        </Typography>
    )
}

export default Title