import React, { useState } from "react";
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { ObjectInspector } from 'react-inspector';

function CardsView() {
    return (
	<Stack direction="column" spacing={1} sx={{p: 2}}>
	    <Typography variant="h4">Cards Page</Typography>
	</Stack>
    );
}

export default CardsView;
