import React, { useState } from "react";
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { ObjectInspector } from 'react-inspector';


function HealthCheckButton(){
    const [data, setData] = useState(null);
    const handleClick = () => {
	fetch('https://catfact.ninja/fact')
	    .then(response => response.json())
	    .then(json => setData(json));
    };
    return (
	<Stack direction="column">
	    <Stack direction="row"> <Button onClick={handleClick}>Dummy Fetch</Button></Stack>
	    <ObjectInspector data={data}/>
	</Stack>
    )
}

function RegistrationsView() {
    return (
	<Stack direction="column" spacing={1} sx={{p: 2}}>
	    <Typography variant="h4">Registration Page</Typography>
	    <HealthCheckButton/>
	</Stack>
    );
}

export default RegistrationsView;
