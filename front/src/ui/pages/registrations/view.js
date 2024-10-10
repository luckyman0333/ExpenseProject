import React, { useState } from "react";
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Card from '@mui/material/Card';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/material/styles';
import { ObjectInspector } from 'react-inspector';
import { TableWithInfiniteScroll } from '../../components/table.js';

function HealthCheckButton(){
    const [data, setData] = useState(null);
    const handleClick = () => {
	fetch('https://catfact.ninja/fact')
	    .then(response => response.json())
	    .then(json => setData(json));
    };
    return (
	<Stack direction="column">
	    <Stack direction="row">
            <Button onClick={handleClick}>Dummy Fetch</Button></Stack>
	    <ObjectInspector data={data}/>
	</Stack>
    )
}

// temp, use fetch instead of this
const data = [
    {first_name: "KRZYSZTOF",
     last_name: "NOWAK",
     act: "0815\/F",
     card_nr: "4166272",
     work_type: "Fizyczny",
     datetime: "2024-10-04T20:03:48.000Z",
     section: "TME",
     direction: "wy"}
];

const columns = [
    {
        title: 'First Name',
        key: 'first_name',
        width: 100
    },
    {
        title: 'Last Name',
        key: 'last_name',
        width: 100
    },
    {
        title: 'Act',
        key: 'act',
        width: 100
    },
    {
        title: 'Card Number',
        key: 'card_nr',
        width: 100
    },
    {
        title: 'Work Type',
        key: 'work_type',
        width: 100
    },
    {
        title: 'Date/Time',
        key: 'datetime',
        width: 100
    },
    {
        title: 'Section',
        key: 'section',
        width: 100
    },
    {
        title: 'Direction',
        key: 'direction',
        width: 100
    }
];

// temp solution, to do, move it to themes
const ContentStyle = styled('Paper')(({ theme }) => ({
    maxWidth: '100%',
    margin: 'auto',
    display: 'flex',
    justifyContent: 'center',
    textAlign: 'center',
    alignItems: 'center',
    flexDirection: 'column'

}))
// how to write correct args??
function RegistrationsView() {
    return (
	<Stack direction="column" spacing={1} sx={{p: 2}}>
	<Typography variant="h4">Registration Page</Typography>
        <ContentStyle>
        <Paper>
        <TableWithInfiniteScroll columns = {columns} rows = {data} />
        </Paper>
        </ContentStyle>
	</Stack>
    );
}

export default RegistrationsView;
